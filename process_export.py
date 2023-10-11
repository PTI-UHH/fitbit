import json
import os
import re
from datetime import datetime
from typing import Any, Union

import pandas as pd
from pandas import Timestamp

from consts import DIRECTORIES, ROOT, OUTPUT_FILE
from utils import CustomJsonEncoder

files_processed = {}


def parse_timestamp(timestamp: Union[str, Timestamp], timestamp_type: str) -> str:
    if timestamp_type == "timestamp_string_dash":
        transformed = datetime.strptime(str(timestamp), "%Y-%m-%d %H:%M:%S")
    elif timestamp_type == "timestamp_string_slash":
        transformed = datetime.strptime(str(timestamp), "%m/%d/%y %H:%M:%S")
    elif timestamp_type == "iso_8601_partial":
        transformed = datetime.fromisoformat(timestamp)
    elif timestamp_type == "iso_8601":
        transformed = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    elif timestamp_type == "unix":
        transformed = datetime.utcfromtimestamp(int(timestamp))
    elif timestamp_type == "datetime_string":
        transformed = datetime.strptime(timestamp, "%a %b %d %H:%M:%S UTC %Y")
    elif timestamp_type == "iso_8601_utc":
        transformed = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
    elif timestamp_type == "iso_8601_utc_no_z":
        transformed = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")
    elif timestamp_type == "iso_8601_ms":
        transformed = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f")
    elif timestamp_type == "iso_8601_ms_z":
        transformed = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
    elif timestamp_type == "iso_8601_with_offset":
        transformed = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f%z")
    else:
        raise Exception("Unhandled timestamp type")

    if transformed.utcoffset():
        transformed -= transformed.utcoffset()
    transformed = transformed.replace(tzinfo=None)

    return str(transformed)


def process_files_in_directory(
        directory_config: dict[str, Any]
) -> list[dict[str, Any]]:
    directory_name = directory_config["name"]
    files_to_read = directory_config["files"]
    ignore_prefix = directory_config.get("ignore_prefix") or []
    events_data = []

    for root, dirs, files in os.walk(ROOT + directory_name):
        for filename in files:
            # Track read files
            if filename.endswith(("csv", "json")):
                ignore = False
                for prefix in ignore_prefix:
                    if filename.startswith(prefix):
                        ignore = True
                if not ignore:
                    files_processed[os.path.join(directory_name, filename)] = "MUST READ"
                else:
                    files_processed[os.path.join(directory_name, filename)] = "IGNORE"

            # Start processing
            for file_config in files_to_read:
                prefix = file_config["prefix"]
                timestamp_column_name = file_config["timestamp_column_name"]
                timestamp_type = file_config["timestamp_type"]
                file_extension = file_config["type"]

                if filename.startswith(prefix) and filename.endswith(
                        f".{file_extension}"
                ):
                    file_path = os.path.join(root, filename)
                    print(f"Processing {file_path}...")
                    files_processed[os.path.join(directory_name, filename)] = "READ"

                    if file_extension == "csv":
                        # Remove commas that don't separate columns
                        with open(file_path, "r") as file:
                            file_content = file.read()
                        lines = []
                        for line in file_content.split("\n"):
                            to_edit = re.findall(r"{.*=.*,.*}", line)
                            for element in to_edit:
                                line = line.replace(
                                    element, element.replace(",", "<break>")
                                )
                            lines.append(line)
                        with open(file_path, "w") as file:
                            file.write("\n".join(lines))

                        df = pd.read_csv(file_path)

                    elif file_extension == "json":
                        df = pd.read_json(file_path)

                    else:
                        raise Exception("Unsupported file type")

                    # TODO: Handle events with start + update / end time
                    # TODO: Handle daily events (e.g. timestamp = August 25, 00:00)
                    # TODO: i.e. __timestamp_regular, __timestamp_start etc.
                    df["__timestamp"] = df[timestamp_column_name].apply(
                        lambda x: parse_timestamp(x, timestamp_type)
                    )
                    df = df.drop(timestamp_column_name, axis=1)
                    df["__file"] = prefix
                    df["__directory"] = directory_name

                    events_data.append(df.to_dict(orient="records"))

    return [event for event_list in events_data for event in event_list]


def main():
    all_events_data = []
    for directory_config in DIRECTORIES:
        events_data = process_files_in_directory(directory_config)
        all_events_data.extend(events_data)

    events_by_timestamp = {}
    for event in all_events_data:
        event_without_timestamp = {key: value for key, value in event.items() if key != "__timestamp"}
        if events_by_timestamp.get(event["__timestamp"]):
            events_by_timestamp[event["__timestamp"]].append(event_without_timestamp)
        else:
            events_by_timestamp[event["__timestamp"]] = [event_without_timestamp]

    with open(OUTPUT_FILE, "w") as json_file:
        json.dump(events_by_timestamp, json_file, indent=2, cls=CustomJsonEncoder)


if __name__ == "__main__":
    main()

    print("-----")
    for f, message in files_processed.items():
        if message == "IGNORE":
            print(f"Ignored {f}.")

    print("-----")
    for f, message in files_processed.items():
        if message == "MUST READ":
            print(f"Warning: Did not read {f}. Add configuration to consts.py > DIRECTORIES.")

    print("-----")
    print("Done!")

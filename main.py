#!/usr/bin/env python3
import json
import os
import sys
from typing import Any
from urllib.parse import urlparse

import mysql.connector
from dotenv import load_dotenv

from process_export import run_process_export


class Database:
    def __init__(self):
        load_dotenv()
        connection_string = os.environ.get("DATABASE_URL")
        url = urlparse(connection_string)
        self.db_config = {
            'user': url.username,
            'password': url.password,
            'host': url.hostname,
            'port': url.port,
            'database': url.path[1:]
        }
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(**self.db_config)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection.is_connected():
            self.connection.close()

    def insert(self, table_name: str, columns: list[str], rows: list[list[Any]]):
        values = ", ".join(["%s" for _ in columns])
        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({values})"
        try:
            self.connect()
            res = self.cursor.executemany(query, rows)
            self.connection.commit()
            return res
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
        finally:
            self.disconnect()

    def query(self, query):
        try:
            self.connect()
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            print(f"Error: {e}")
            self.connection.rollback()
        finally:
            self.disconnect()


if __name__ == '__main__':
    db = Database()
    _, user_id, fitbit_path = sys.argv
    processed_data = run_process_export(fitbit_path)

    rows = []
    for timestamp, data in processed_data.items():
        rows.append([user_id, json.dumps(data), timestamp])

    db.insert(
        table_name="FitbitData",
        columns=["userId", "data", "timestamp"],
        rows=rows
    )

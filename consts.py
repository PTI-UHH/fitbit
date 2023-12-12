DIRECTORIES = [
    {
        "name": "Account Changes",
        "files": [
            {
                "prefix": "Account_Management_Events",
                "timestamp_column_name": "timestamp",
                "timestamp_type": "datetime_string",
                "type": "csv",
            }
        ],
        "ignore_prefix": ["Account_Access_Events"],
    },
    {
        "name": "Active Zone Minutes (AZM)",
        "files": [
            {
                "prefix": "Active Zone Minutes",
                "timestamp_column_name": "date_time",
                "timestamp_type": "iso_8601_partial",
                "type": "csv",
            }
        ],
    },
    {
        "name": "Activity Goals",
        "files": [
            {
                "prefix": "Activity Goals",
                "timestamp_column_name": "created_on",
                "timestamp_type": "iso_8601",
                "type": "csv",
            }
        ],
    },
    {
        "name": "Atrial Fibrillation ECG",
        "files": [
            {
                "prefix": "afib_ecg_reading",
                "timestamp_column_name": "reading_time",
                "timestamp_type": "datetime_string",
                "type": "csv",
            }
        ],
    },
    {"name": "Biometrics", "files": []},
    {
        "name": "Daily Readiness",
        "files": [
            {
                "prefix": "Daily Readiness User Properties",
                "timestamp_column_name": "last_update",
                "timestamp_type": "iso_8601",
                "type": "csv",
            }
        ],
    },
    {
        "name": "Discover",
        "files": [],
    },
    {
        "name": "Fitbit Care or Programs",
        "files": [],
    },
    {
        "name": "Fitbit Premium",
        "files": [],
        "ignore_prefix": ["User Premium Transactions", "User Premium Subscriptions"],
    },
    {
        "name": "Global Export Data",
        "files": [
            {
                "prefix": "altitude",
                "timestamp_column_name": "dateTime",
                "timestamp_type": "timestamp_string_dash",
                "type": "json",
            },
            {
                "prefix": "calories",
                "timestamp_column_name": "dateTime",
                "timestamp_type": "timestamp_string_dash",
                "type": "json",
            },
            {
                "prefix": "demographic_vo2_max",
                "timestamp_column_name": "dateTime",
                "timestamp_type": "timestamp_string_dash",
                "type": "json",
            },
            {
                "prefix": "distance",
                "timestamp_column_name": "dateTime",
                "timestamp_type": "timestamp_string_dash",
                "type": "json",
            },
            {
                "prefix": "estimated_oxygen_variation",
                "timestamp_column_name": "timestamp",
                "timestamp_type": "timestamp_string_slash",
                "type": "csv",
            },
            {
                "prefix": "exercise",
                "timestamp_column_name": "startTime",
                "timestamp_type": "timestamp_string_slash",
                "type": "json",
            },
            {
                "prefix": "heart_rate",
                "timestamp_column_name": "dateTime",
                "timestamp_type": "timestamp_string_dash",
                "type": "json",
            },
            {
                "prefix": "height",
                "timestamp_column_name": "dateTime",
                "timestamp_type": "timestamp_string_dash",
                "type": "json",
            },
            {
                "prefix": "lightly_active_minutes",
                "timestamp_column_name": "dateTime",
                "timestamp_type": "timestamp_string_dash",
                "type": "json",
            },
            {
                "prefix": "moderately_active_minutes",
                "timestamp_column_name": "dateTime",
                "timestamp_type": "timestamp_string_dash",
                "type": "json",
            },
            {
                "prefix": "resting_heart_rate",
                "timestamp_column_name": "dateTime",
                "timestamp_type": "timestamp_string_dash",
                "type": "json",
            },
            {
                "prefix": "sedentary_minutes",
                "timestamp_column_name": "dateTime",
                "timestamp_type": "timestamp_string_dash",
                "type": "json",
            },
            {
                "prefix": "sleep",
                "timestamp_column_name": "startTime",
                "timestamp_type": "iso_8601_ms",
                "type": "json",
            },
            {
                "prefix": "steps",
                "timestamp_column_name": "dateTime",
                "timestamp_type": "timestamp_string_dash",
                "type": "json",
            },
            {
                "prefix": "swim_lengths_data",
                "timestamp_column_name": "dateTime",
                "timestamp_type": "timestamp_string_dash",
                "type": "json",
            },
            {
                "prefix": "time_in_heart_rate_zones",
                "timestamp_column_name": "dateTime",
                "timestamp_type": "timestamp_string_dash",
                "type": "json",
            },
            {
                "prefix": "very_active_minutes",
                "timestamp_column_name": "dateTime",
                "timestamp_type": "timestamp_string_dash",
                "type": "json",
            },
            {
                "prefix": "weight",
                "timestamp_column_name": "date",
                "timestamp_type": "timestamp_string_dash",
                "type": "json",
            },
        ],
        "ignore_prefix": ["badge"],
    },
    {
        "name": "Guided Programs",
        "files": [],
    },
    {
        "name": "Heart Rate",
        "files": [
            {
                "prefix": "Heart Rate Notifications Alerts",
                "timestamp_column_name": "start_timestamp",
                "timestamp_type": "?",
                "type": "csv",
            }
        ],
        "ignore_prefix": ["Heart Rate Notifications Profile"],
    },
    {
        "name": "Heart Rate Variability",
        "files": [
            {
                "prefix": "Daily Heart Rate Variability Summary",
                "timestamp_column_name": "timestamp",
                "timestamp_type": "iso_8601_utc_no_z",
                "type": "csv",
            },
            {
                "prefix": "Daily Respiratory Rate Summary",
                "timestamp_column_name": "timestamp",
                "timestamp_type": "iso_8601_utc_no_z",
                "type": "csv",
            },
            {
                "prefix": "Heart Rate Variability Details",
                "timestamp_column_name": "timestamp",
                "timestamp_type": "iso_8601_utc_no_z",
                "type": "csv",
            },
            {
                "prefix": "Heart Rate Variability Histogram",
                "timestamp_column_name": "timestamp",
                "timestamp_type": "iso_8601_utc_no_z",
                "type": "csv",
            },
            {
                "prefix": "Respiratory Rate Summary",
                "timestamp_column_name": "timestamp",
                "timestamp_type": "iso_8601_utc_no_z",
                "type": "csv",
            }
        ],
    },
    {
        "name": "Journal Log",
        "files": [
            {
                "prefix": "journal_entries",
                "timestamp_column_name": "log_time",
                "timestamp_type": "iso_8601_partial",
                "type": "csv",
            }
        ],
    },
    {
        "name": "Menstrual Health",
        "files": [
            {
                "prefix": "menstrual_health_birth_control",
                "timestamp_column_name": "event_date",
                "timestamp_type": "?",
                "type": "csv",
            },
            {
                "prefix": "menstrual_health_cycles",
                "timestamp_column_name": "cycle_start_date",
                "timestamp_type": "?",
                "type": "csv",
            },
            {
                "prefix": "menstrual_health_symptoms",
                "timestamp_column_name": "timestamp",
                "timestamp_type": "?",
                "type": "csv",
            },
        ],
        "ignore_prefix": ["menstrual_health_settings"],
    },
    {
        "name": "Mindfulness",
        "files": [
            {
                "prefix": "mindfulness_eda_data_sessions",
                "timestamp_column_name": "timestamp",
                "timestamp_type": "unix",
                "type": "csv",
            },
            {
                "prefix": "mindfulness_goals",
                "timestamp_column_name": "date",
                "timestamp_type": "datetime_string",
                "type": "csv",
            },
            {
                "prefix": "mindfulness_sessions",
                "timestamp_column_name": "start_date_time",
                "timestamp_type": "iso_8601",
                "type": "csv",
            },
        ],
    },
    {
        "name": "Oxygen Saturation (SpO2)",
        "files": [
            {
                "prefix": "Daily SpO2",
                "timestamp_column_name": "timestamp",
                "timestamp_type": "iso_8601_utc",
                "type": "csv",
            },
            {
                "prefix": "Minute SpO2",
                "timestamp_column_name": "timestamp",
                "timestamp_type": "iso_8601",
                "type": "csv",
            },
        ],
    },
    {
        "name": "Paired Devices",
        "files": [
            {
                "prefix": "iOS App Notification Settings",
                "timestamp_column_name": "created_on",
                "timestamp_type": "iso_8601",
                "type": "csv",
            },
            {
                "prefix": "Trackers",
                "timestamp_column_name": "heart_rate_tracking_update_time",
                "timestamp_type": "iso_8601_ms_z",
                "type": "csv",
            },
        ],
        "ignore_prefix": ["Devices", "Scales", "Tracker Optional Configuration"],
    },
    {
        "name": "Sleep Score",
        "files": [
            {
                "prefix": "sleep_score",
                "timestamp_column_name": "timestamp",
                "timestamp_type": "iso_8601",
                "type": "csv",
            },
        ],
    },
    {"name": "Snore and Noise Detect", "files": []},
    {"name": "Social", "files": []},
    {
        "name": "Stress Journal",
        "files": [
            {
                "prefix": "CEDA Data",
                "timestamp_column_name": "timestamp",
                "timestamp_type": "iso_8601_with_offset",
                "type": "csv",
            }
        ],
    },
    {
        "name": "Stress Score",
        "files": [
            {
                "prefix": "Stress Score",
                "timestamp_column_name": "UPDATED_AT",
                "timestamp_type": "iso_8601_ms",
                "type": "csv",
            },
        ],
    },
    {
        "name": "Temperature",
        "files": [],
        "ignore_prefix": ["Computed Temperature", "Device Temperature", "Wrist Temperature"],
    },
    {
        "name": "Transactions",
        "files": [],
    },
    {
        "name": "User Security Data",
        "files": [],
        "ignore_prefix": ["User_Retired_Password", "User_Email_Audit_Entry"],
    },
    {
        "name": "Your Profile",
        "files": [],
        "ignore_prefix": ["Profile"],
    },
]

import os
import json
import datetime
from typing import List

# ------------------------------
# Mocked External Dependencies
# ------------------------------

# Simulate mlpass.get_env and mlpass.get_secret
def get_env(key: str, default=None):
    return os.environ.get(key, default)

def get_secret(key: str):
    return f"mocked-secret-for-{key}"

# Simulated BigQuery Client
def query_bigquery(query: str):
    print("Executing BigQuery query:", query)
    return [{"bug_id": "BUG-001", "summary": "Sample Bug", "priority": "High"}]

# Simulated JIRA Client
class MockJiraClient:
    def issue(self, key):
        return {
            "key": key,
            "fields": {
                "summary": f"Mocked summary for {key}",
                "priority": {"name": "High"},
                "status": {"name": "To Do"},
                "assignee": {"displayName": "Mocked User"},
            },
        }

def get_jira_client():
    return MockJiraClient()

# Simulated Slack Notifier
def notify_slack(channel: str, message: str):
    print(f"[Slack Notification to {channel}] {message}")

# Simulated Google Sheets Writer
def write_to_sheet(sheet_name: str, data: List[dict]):
    print(f"[Writing to Google Sheet: {sheet_name}]")
    for row in data:
        print(row)

# Main Report Logic

def generate_bug_report():
    print("Generating bug report...")

    # Fetch credentials (mocked)
    db_credentials = get_secret("bigquery-credentials")
    jira_client = get_jira_client()

    # Fetch data (mocked query)
    bugs = query_bigquery("SELECT * FROM bugs WHERE priority='High'")

    # Enrich with JIRA data
    enriched_bugs = []
    for bug in bugs:
        issue_data = jira_client.issue(bug["bug_id"])
        enriched_bugs.append({
            "ID": issue_data["key"],
            "Summary": issue_data["fields"]["summary"],
            "Priority": issue_data["fields"]["priority"]["name"],
            "Status": issue_data["fields"]["status"]["name"],
            "Assignee": issue_data["fields"]["assignee"]["displayName"],
        })

    # Output to Google Sheet (mocked)
    write_to_sheet("Bug Report", enriched_bugs)

    # Notify on Slack (mocked)
    notify_slack("#bug-reports", f"Bug report generated with {len(enriched_bugs)} entries.")

    print("Done.")

# Entry Point

if __name__ == "__main__":
    generate_bug_report()

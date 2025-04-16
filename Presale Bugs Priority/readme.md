# JIRA Bug Report Generator (Mocked)

This project is a mock-based version of an internal automation tool designed to update bugs priority directly on JIRA tickets and generate reports from JIRA, BigQuery, and other internal systems, and output results to Google Sheets and Slack.

## 🔧 Purpose
Automate the extraction, enrichment, and reporting of high-priority bugs from JIRA and BigQuery, simulating integration with:
- **BigQuery** for data retrieval
- **JIRA** for issue details
- **Google Sheets** for reporting
- **Slack** for notifications

## 🧪 Local Mock Environment
All external dependencies have been replaced with mocked equivalents for local development and public sharing purposes.

## 🛠️ Tech Stack
- Python 3.9+
- Mocked versions of:
  - BigQuery
  - Atlassian JIRA
  - Google Sheets
  - Slack API
  - Secret management via `mlpass`

## ▶️ How to Run
```bash
python jira_bug_report_generator.py
```
This will:
1. Run a mocked query to BigQuery
2. Enrich with mocked JIRA issue data
3. Output to a simulated Google Sheet
4. Send a Slack-style console notification

## 📂 Project Structure
```
.
├── jira_bug_report_generator.py  # Main script with mock integrations
└── README.md                     # This file
```

## 📋 Example Output
```
[Writing to Google Sheet: Bug Report]
{'ID': 'BUG-001', 'Summary': 'Mocked summary for BUG-001', 'Priority': 'High', 'Status': 'To Do', 'Assignee': 'Mocked User'}
[Slack Notification to #bug-reports] Bug report generated with 1 entries.
```

---

This project is for portfolio purposes. No real credentials or internal logic are exposed.


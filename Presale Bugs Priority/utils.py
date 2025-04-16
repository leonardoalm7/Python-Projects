import requests
from mock_env import mlpass

def get_url_base(service_name="internal-api"):
    return f"https://{service_name}.mockcompany.com" if melipass.get_env("SECRET_LOCAL") == "True" else f"http://{service_name}.mockcompany.com"

def get_request(url, headers=None):
    headers = headers or {}
    # Simulate secure request tunnel
    return {"api_response_body": requests.get(url, headers=headers).json()}

def post_slack_message(text):
    import json
    slack_url = base64.b64decode(melipass.get_secret("SLACK_WEBHOOK")).decode("utf-8")
    payload = json.dumps({"text": text})
    headers = {"Content-Type": "application/json"}
    return requests.post(slack_url, data=payload, headers=headers)

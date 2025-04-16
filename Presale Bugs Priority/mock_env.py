import base64
import os
import requests

class MockSecretsManager:
    def __init__(self):
        self.local = os.getenv("SECRET_LOCAL", "True") == "True"
        self.secrets_store = {
            "TOKEN_JIRA": "mock_token",
            "USER_JIRA": "mock_user",
            "BQ_CREDENTIALS": "mock_bigquery_credentials",
            "SLACK_WEBHOOK": base64.b64encode(b"https://hooks.slack.com/mock-webhook").decode("utf-8"),
        }

    def get_env(self, key):
        return str(self.local)

    def get_secret(self, key):
        return self.secrets_store.get(key, "")

    def fetch_credentials(self, params: str):
        # Simulate secret fetching based on environment
        return {
            param: f"mock_{param.lower()}" for param in params.split("=")[-1].split(",")
        }

mlpass = MockSecretsManager()

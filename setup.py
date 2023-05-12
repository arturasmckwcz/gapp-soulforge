import os


class setup:
    host = os.environ.get("RABBITMQ_HOST") or "rabbitmq"
    exchange = "timepulse"
    user = "gapp"
    password = "gapp"

    api_url = os.environ.get("GAPP_API_URL") or "http://api:3000/graphql"

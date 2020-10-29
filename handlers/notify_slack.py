import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json

from common.secrets_manager import get_secret

logger = logging.getLogger()
logger.setLevel(logging.INFO)

credentials = json.loads(get_secret())

client = WebClient(token=credentials["slack_token"])


def app(event: dict, context: dict) -> None:
    logger.info(event)

    for record in event["Records"]:
        message = json.loads(record["Sns"]["Message"])

        try:
            response = client.chat_postMessage(channel=message["channel"], text=message["output"])
            logger.info(response)
        except SlackApiError as e:
            logger.error(e.response["error"])

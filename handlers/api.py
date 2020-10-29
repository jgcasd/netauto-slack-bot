import json
import logging
import os
from urllib.parse import parse_qs
import boto3


logger = logging.getLogger()
logger.setLevel(logging.INFO)

sqs = boto3.client("sqs")
queue_url = os.getenv("queue_url", "")


def create_task(message: dict) -> dict:
    return sqs.send_message(QueueUrl=queue_url, MessageBody=json.dumps(message))


def show_interface(event: dict, context: dict) -> dict:
    logger.info(event)
    query_params = parse_qs(event["body"])

    try:
        create_task(
            {
                "slack_command": "show-interface",
                "command_type": "command",
                "args": {
                    "device": query_params["text"][0].split()[0],
                    "interface": query_params["text"][0].split()[1],
                },
                "channel": query_params["channel_id"][0],
            }
        )
        return {"statusCode": 200, "body": json.dumps("Processing request...")}
    except Exception as error:
        logger.error(error)
        return {"statusCode": 400, "body": json.dumps("Failed to process request. Check arguments and try again.")}


def show_routes(event: dict, context: dict) -> dict:
    logger.info(event)
    query_params = parse_qs(event["body"])

    try:
        create_task(
            {
                "slack_command": "show-routes",
                "command_type": "command",
                "args": {"device": query_params["text"][0].split()[0]},
                "channel": query_params["channel_id"][0],
            }
        )
        return {"statusCode": 200, "body": json.dumps("Processing request...")}
    except Exception as error:
        logger.error(error)
        return {"statusCode": 400, "body": json.dumps("Failed to process request. Check arguments and try again.")}


def show_version(event: dict, context: dict) -> dict:
    logger.info(event)
    query_params = parse_qs(event["body"])

    try:
        create_task(
            {
                "slack_command": "show-version",
                "command_type": "command",
                "args": {"device": query_params["text"][0].split()[0]},
                "channel": query_params["channel_id"][0],
            }
        )
        return {"statusCode": 200, "body": json.dumps("Processing request...")}
    except Exception as error:
        logger.error(error)
        return {"statusCode": 400, "body": json.dumps("Failed to process request. Check arguments and try again.")}


def switchport_enable(event: dict, context: dict) -> dict:
    logger.info(event)
    query_params = parse_qs(event["body"])

    try:
        create_task(
            {
                "slack_command": "switchport-enable",
                "command_type": "config",
                "args": {
                    "device": query_params["text"][0].split()[0],
                    "interface": query_params["text"][0].split()[1],
                },
                "channel": query_params["channel_id"][0],
            }
        )
        return {"statusCode": 200, "body": json.dumps("Processing request...")}
    except Exception as error:
        logger.error(error)
        return {"statusCode": 400, "body": json.dumps("Failed to process request. Check arguments and try again.")}


def switchport_disable(event: dict, context: dict) -> dict:
    logger.info(event)
    query_params = parse_qs(event["body"])

    try:
        create_task(
            {
                "slack_command": "switchport-disable",
                "command_type": "config",
                "args": {
                    "device": query_params["text"][0].split()[0],
                    "interface": query_params["text"][0].split()[1],
                },
                "channel": query_params["channel_id"][0],
            }
        )
        return {"statusCode": 200, "body": json.dumps("Processing request...")}
    except Exception as error:
        logger.error(error)
        return {"statusCode": 400, "body": json.dumps("Failed to process request. Check arguments and try again.")}

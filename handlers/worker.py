from jinja2 import Template
import logging
import os
import json
import boto3
from drivers.netmiko_driver import Netmiko
from common.device_lookup import load_devices
from common.secrets_manager import get_secret

logger = logging.getLogger()
logger.setLevel(logging.INFO)

arn = os.getenv("sns_arn", "")

client = boto3.client("sns")

# add new commands and their corresponding jinja2 templates here
commands = {
    "switchport-enable": "switchport_enable.j2",
    "switchport-disable": "switchport_disable.j2",
    "show-version": "show_version.j2",
    "show-routes": "show_routes.j2",
    "show-interface": "show_interface.j2",
}


def render_config(slack_command: str, args: dict, device_type: str) -> str:
    template_name = "templates/{0}/{1}".format(device_type, commands.get(slack_command))
    with open(template_name, "r") as f:
        config = Template(f.read())
        return config.render(**args)


def app(event: dict, context: dict) -> None:
    logger.info(event)

    credentials = json.loads(get_secret())
    devices = load_devices()

    for record in event["Records"]:
        logger.info(record["body"])

        data = json.loads(record["body"])

        device = devices.get(data["args"]["device"])

        netmiko = Netmiko(
            **{
                "device_type": device["device_type"],
                "hostname": device["ip_address"],
                "username": credentials["router_username"],
                "password": credentials["router_password"],
            }
        )

        config = render_config(data["slack_command"], data["args"], device["device_type"])

        message = {"channel": data["channel"]}

        try:
            if data.get("command_type") == "config":
                message["output"] = netmiko.send_config(config.split("\n"))

            elif data.get("command_type") == "command":
                message["output"] = netmiko.send_command(config)

            else:
                message["output"] = "Command type not recognized"
        except Exception as error:
            logger.error(error)
            message["output"] = error

        response = client.publish(
            TargetArn=arn,
            Message=json.dumps({"default": json.dumps(message)}),
            Subject="slack_command output",
            MessageStructure="json",
        )
        logger.info(response)

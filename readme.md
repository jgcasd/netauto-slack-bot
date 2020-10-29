# NetAuto SlackBot
A serverless Slack bot that allows network operators to manage their network.

# Motivation
This project serves as a demonstration of how to implement a highly-available, highly-scalable, low-cost,
serverless network focused chatops style Slack bot for managing your network.

# Build Status

# Screenshots
![Slash Command](https://github.com/jgcasd/netauto-slack-bot/blob/main/docs/slash-command.png)
![Command Result](https://github.com/jgcasd/netauto-slack-bot/blob/main/docs/slash-command-result.png)

# Code Style
* Code formatter: black
* Code Linting: flake8
* Max line length set to 119

# Tech/framework
* Python3.x
* Netmiko
* AWS API Gateway
* AWS SQS
* AWS SNS
* AWS Lambda
* AWS Secrets Manager

# Installation
* Ensure serverless framework has been installed
* Create a JSON formatted secret in secrets manager with your credentials:
```json
{
  "slack_token": "01234567890",
  "router_username": "admin",
  "router_password": "admin"
}
```
* Create config.yml in the root of your directory with the following parameters:
```yaml
secret_name: slack-bot-creds # name of your credentials in secrets manager
account_name: 01234567890 # aws account id
```
* Populate your device configs under configs/devices.yml
```yaml
# list of devices
router01:
  ip_address: 192.168.1.1
  device_type: cisco_ios
router02:
  ip_address: 192.168.1.2
  device_type: cisco_ios
```

* Create an .env file with your AWS credentials
```bash
AWS_ACCESS_KEY_ID=XXXXXXXXXXXXXX
AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXXX
AWS_DEFAULT_REGION=us-west-2
```

* Deploy the code: ```make deploy```


# Supported Commands
* switchport-enable ```device``` ```interface```
* switchport-disable  ```device``` ```interface```
* show-version ```device```
* show-routes ```device```
* show-interface ```device``` ```interface```


# Contribute
1) Install requirements: ```pip install flake8 black```
2) Fork this repository
3) Create a branch: ```git checkout -b <branch name>```
4) Make your changes and commit them: ```git commit -m <commit message>```
5) Push to the original branch: ```git push origin <project_name>/<location>```
6) Create the pull request.

# Todo
* Add support for running scripts rather than jinja2 templates (this would allow for more complex workflows)
* Add support for retrieving device vars from external source (S3, DynamoDB, Netbox)
* Add more commands
* Improve error handling
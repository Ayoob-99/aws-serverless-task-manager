# AWS Serverless Task Manager

A serverless REST API built using AWS services and Python. The application allows users to create, view, update and delete tasks using HTTP requests.

## Architecture

Client → API Gateway → AWS Lambda → DynamoDB

CloudWatch is used to monitor Lambda executions and logs.

## Technologies

- Python
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch
- boto3
- Git / GitHub

## Features

- Create tasks using POST requests
- Retrieve tasks using GET requests
- Update tasks using PUT requests
- Delete tasks using DELETE requests
- Store task data in DynamoDB
- Serverless backend using AWS Lambda
- API exposed through Amazon API Gateway
- Least-privilege IAM execution role
- Lambda monitoring through CloudWatch

## Example Task

```json
{
  "taskId": "2",
  "title": "Test API Gateway",
  "status": "todo"
}
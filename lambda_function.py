import boto3
import json

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Tasks")


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }


def lambda_handler(event, context):

    # Support API Gateway HTTP API and REST API formats
    method = event.get("httpMethod")

    if not method:
        method = (
            event.get("requestContext", {})
            .get("http", {})
            .get("method")
        )

    body = event.get("body")

    if body:
        if isinstance(body, str):
            body = json.loads(body)
    else:
        body = {}

    # GET - list all tasks
    if method == "GET":

        result = table.scan()

        return response(200, {
            "tasks": result.get("Items", [])
        })

    # POST - create task
    elif method == "POST":

        task = {
            "taskId": body["taskId"],
            "title": body["title"],
            "status": body.get("status", "todo")
        }

        table.put_item(Item=task)

        return response(201, {
            "message": "Task created successfully",
            "task": task
        })

    # PUT - update task
    elif method == "PUT":

        result = table.update_item(
            Key={
                "taskId": body["taskId"]
            },
            UpdateExpression="SET #title = :title, #status = :status",
            ExpressionAttributeNames={
                "#title": "title",
                "#status": "status"
            },
            ExpressionAttributeValues={
                ":title": body["title"],
                ":status": body["status"]
            },
            ReturnValues="ALL_NEW"
        )

        return response(200, {
            "message": "Task updated successfully",
            "task": result["Attributes"]
        })

    # DELETE - delete task
    elif method == "DELETE":

        table.delete_item(
            Key={
                "taskId": body["taskId"]
            }
        )

        return response(200, {
            "message": "Task deleted successfully"
        })

    return response(400, {
        "message": "Unsupported request"
    })
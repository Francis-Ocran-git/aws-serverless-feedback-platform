import json
import uuid
from datetime import datetime

import boto3

# AWS Clients
comprehend = boto3.client("comprehend")
sns = boto3.client("sns")
dynamodb = boto3.resource("dynamodb")

# DynamoDB Table
table = dynamodb.Table("cloudwithshad-feedback")

# SNS Topic ARN
TOPIC_ARN = "arn:aws:sns:us-east-1:533595510871:negative-feedback-alerts"

# CORS Headers
CORS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
}


def lambda_handler(event, context):
    """
    Handles customer feedback:
    1. Receives feedback from API Gateway
    2. Detects sentiment using Amazon Comprehend
    3. Extracts entities
    4. Sends SNS email for negative feedback
    5. Saves feedback to DynamoDB
    """

    # Handle CORS preflight request
    if event.get("httpMethod") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": CORS,
            "body": ""
        }

    try:
        # Parse request body
        body = json.loads(event["body"])

        name = body.get("name", "").strip()
        email = body.get("email", "").strip()
        message = body.get("message", "").strip()[:5000]

        if not message:
            return {
                "statusCode": 400,
                "headers": CORS,
                "body": json.dumps({
                    "error": "Message cannot be empty."
                })
            }

        # Detect sentiment
        sentiment = comprehend.detect_sentiment(
            Text=message,
            LanguageCode="en"
        )

        # Extract entities
        entities_response = comprehend.detect_entities(
            Text=message,
            LanguageCode="en"
        )

        entities = [
            {
                "text": entity["Text"],
                "type": entity["Type"]
            }
            for entity in entities_response["Entities"][:10]
        ]

        sentiment_name = sentiment["Sentiment"]

        sentiment_score = sentiment["SentimentScore"][
            sentiment_name.title()
        ]

        # Send email only for negative feedback
        if sentiment_name == "NEGATIVE":

            sns.publish(
                TopicArn=TOPIC_ARN,
                Subject="New Negative Customer Feedback",
                Message=f"""
A new negative customer feedback has been received.

Name:
{name}

Email:
{email}

Message:
{message}

Sentiment:
{sentiment_name}

Please review this feedback.
"""
            )

        # Generate Feedback ID
        feedback_id = str(uuid.uuid4())

        # Save to DynamoDB
        table.put_item(
            Item={
                "feedback_id": feedback_id,
                "name": name,
                "email": email,
                "message": message,
                "sentiment": sentiment_name,
                "sentiment_score": str(sentiment_score),
                "entities": entities,
                "submitted_at": datetime.utcnow().isoformat()
            }
        )

        return {
            "statusCode": 200,
            "headers": CORS,
            "body": json.dumps({
                "success": True,
                "feedback_id": feedback_id,
                "sentiment": sentiment_name
            })
        }

    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "headers": CORS,
            "body": json.dumps({
                "error": "Invalid JSON received."
            })
        }

    except Exception as e:
        print(f"ERROR: {str(e)}")

        return {
            "statusCode": 500,
            "headers": CORS,
            "body": json.dumps({
                "error": "Internal server error.",
                "details": str(e)
            })
        }
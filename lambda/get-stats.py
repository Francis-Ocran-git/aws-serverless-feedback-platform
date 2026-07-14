import boto3
import json
from collections import Counter
from decimal import Decimal

dynamo = boto3.resource('dynamodb')
table = dynamo.Table('cloudwithshad-feedback')

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)

def lambda_handler(event, context):
    # Scan all feedback (fine for small datasets)
    response = table.scan()
    items = response['Items']

    # Aggregate sentiment counts
    sentiment_counts = Counter(item['sentiment'] for item in items)

    # Top entities
    entity_counts = Counter()
    for item in items:
        for e in item.get('entities', []):
            entity_counts[e['text']] += 1
    top_entities = entity_counts.most_common(10)

    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({
            'total': len(items),
            'sentiment_breakdown': dict(sentiment_counts),
            'top_entities': top_entities,
            'recent': sorted(items, key=lambda x: x.get('submitted_at', ''), reverse=True)[:10]
        }, cls=DecimalEncoder)
    }
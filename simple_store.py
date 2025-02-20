import json

def lambda_handler(event, context):
    store_events = [
        {"id": 1, "name": "Black Friday Sale", "date": "2025-11-28", "location": "Main Store"},
        {"id": 2, "name": "Summer Clearance", "date": "2025-07-15", "location": "Online"}
    ]

    # API Gateway usa "resource" em vez de "path"
    path = event.get('path') or event.get('resource')
    method = event.get('httpMethod')

    if path == '/events' and method == 'GET':
        return {
            "statusCode": 200,
            "body": json.dumps({"events": store_events}),
            "headers": {"Content-Type": "application/json"}
        }
    else:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "Rota não encontrada"}),
            "headers": {"Content-Type": "application/json"}
        }

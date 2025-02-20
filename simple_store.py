import json

def lambda_handler(event, context):
    store_events = [
        {"id": 1, "name": "Black Friday Sale", "date": "2025-11-28", "location": "Main Store"},
        {"id": 2, "name": "Summer Clearance", "date": "2025-07-15", "location": "Online"}
    ]

    if event.get('path') == '/events' and event.get('httpMethod') == 'GET':
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

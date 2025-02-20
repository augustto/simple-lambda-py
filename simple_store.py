import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f"Evento recebido: {json.dumps(event, indent=2)}")

    store_events = [
        {"id": 1, "name": "Black Friday Sale", "date": "2025-11-28", "location": "Main Store"},
        {"id": 2, "name": "Summer Clearance", "date": "2025-07-15", "location": "Online"}
    ]

    # Ajusta a captura do método HTTP para REST API e HTTP API
    path = event.get("rawPath", event.get("path", "N/A"))
    method = event.get("httpMethod", event.get("requestContext", {}).get("http", {}).get("method", "N/A"))

    logger.info(f"Path recebido: {path}, Method: {method}")

    if path == "/events" and method == "GET":
        return {
            "statusCode": 200,
            "body": json.dumps({"events": store_events}),
            "headers": {"Content-Type": "application/json"}
        }
    else:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": f"Rota não encontrada. Path: {path}, Method: {method}"}),
            "headers": {"Content-Type": "application/json"}
        }
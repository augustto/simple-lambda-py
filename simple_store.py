import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f"Evento recebido: {json.dumps(event)}")  # Log do evento completo

    store_events = [
        {"id": 1, "name": "Black Friday Sale", "date": "2025-11-28", "location": "Main Store"},
        {"id": 2, "name": "Summer Clearance", "date": "2025-07-15", "location": "Online"}
    ]

    # Capturar corretamente o caminho e método HTTP
    path = event.get("rawPath") or event.get("path") or "N/A"
    method = event.get("httpMethod", "N/A")

    logger.info(f"Path recebido: {path}, Method: {method}")

    if "/events" in path and method == "GET":
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

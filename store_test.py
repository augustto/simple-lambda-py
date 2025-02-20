import simple_store  # Importa o arquivo onde está o lambda_handler

# Simula um evento de entrada (como um evento do API Gateway)
event = {
    "path": "/events",
    "httpMethod": "GET",
    "body": None  # Pode ser um JSON para POST, PUT, etc.
}

# Simula o contexto (opcional, mas útil para testes mais realistas)
class MockContext:
    def __init__(self):
        self.function_name = "store-events-api"
        self.memory_limit_in_mb = 128
        self.invoked_function_arn = "arn:aws:lambda:us-east-1:123456789012:function:store-events-api"
        self.aws_request_id = "12345678-1234-1234-1234-1234567890ab"

# Chama a função lambda_handler com o evento e contexto simulados
context = MockContext()
result = simple_store.lambda_handler(event, context)

# Exibe o resultado para depuração
print("Resultado do Lambda:", result)
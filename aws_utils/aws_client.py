import boto3

class ClienteAWS():

    def __init__(self, servico: str, access_key: str, secret_key: str) -> None:
        self.servico = servico
        self.access_key = access_key
        self.secret_key = secret_key
    
    def retorna_cliente(self):
        cliente = boto3.client(
            self.servico,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key   
        )
        return cliente
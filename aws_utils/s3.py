from aws_client import ClienteAWS
import os

class ManipulaS3():
    def __init__(self, cliente: ClienteAWS) -> None:
        self.cliente = cliente.retorna_cliente()

    def upload_arquivo(self, nome_arquivo: str, bucket: str, nome_objeto=None) -> bool:
        # If S3 object_name was not specified, use file_name
        if nome_objeto is None:
            nome_objeto = os.path.basename(nome_arquivo)

        # Upload the file
        try:
            response = self.cliente.upload_file(nome_arquivo, bucket, nome_objeto)
        except Exception as e:
            print(e)
            return False
        return True
    


if __name__ == '__main__':
    import configparser

    config = configparser.ConfigParser()
    config.read('config.cfg')
    aws_access_key_id=config['aws-credentials']['ACCESS_KEY']
    aws_secret_access_key=config['aws-credentials']['SECRET_KEY']

    cliente = ClienteAWS('s3',aws_access_key_id,aws_secret_access_key)

    s3 = ManipulaS3(cliente)
    s3.upload_arquivo('README.md','meu-projetob3-bucket','raw/readme.md')

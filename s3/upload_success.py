from s3.my_script import upload_file
def upload_success(nome_arquivo):

    # Chamando a função para fazer o upload do arquivo
    bucket = 'trabalho-finaldemodulo-ada-aws'
    upload_success = upload_file(nome_arquivo,bucket)

    if upload_success:
        print("Arquivo enviado para o S3 com sucesso!")
    else:
        print("Houve um erro ao enviar o arquivo para o S3.")

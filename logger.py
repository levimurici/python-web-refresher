import argparse
from time import sleep

url_default = 'https://rowie-static.s3.us-east-2.amazonaws.com/nfts/k9-temp/k9-club/'
file_read = "logger.txt"

parser = argparse.ArgumentParser(description='Script para atualização automatica de urls')
parser.add_argument('-r', '--read', default=file_read, type=str, help='Nome do arquivo com logs')
parser.add_argument('-w', '--write', default='k9_reg', type=str, help='Nome do arquivo para salvar formatado')
parser.add_argument('-u', '--url', default=url_default, type=str, help='Url de acesso')

args = parser.parse_args()

file_save = args.read
file_read = args.write
url_parsed = args.url

with open(file_read, "r") as f:
    for number in f:
        line = number
        with open(file_save, "a+") as w:
            to_write = url_parsed+str(line)+".jpeg"
            w.write(to_write)
            print(to_write)
            w.close()
f.close()

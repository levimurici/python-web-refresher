import argparse
import re
from time import sleep


url_default = 'https://rowie-static.s3.us-east-2.amazonaws.com/nfts/k9-temp/k9-club/'
file_read = "logger.txt"

parser = argparse.ArgumentParser(description='Script para atualização automatica de urls')
parser.add_argument('-r', '--read', default=file_read, type=str, help='Nome do arquivo com logs')
parser.add_argument('-w', '--write', default='k9_reg', type=str, help='Nome do arquivo para salvar formatado')
parser.add_argument('-u', '--url', default=url_default, type=str, help='Url de acesso')
args = parser.parse_args()

file_read = args.read
file_save = args.write
url_parsed = args.url

if __name__ == '__main__':
    with open(file_read, "r") as f:
        for number in f:
            line = re.search("^[0-9]", number)
            with open(file_save, "a+") as w:
                to_write = url_parsed+str(line)+".jpeg\n"
                w.write(to_write)
                print(to_write)
                w.close()
    f.close()
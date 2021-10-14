from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse
from time import sleep

url_default = 'https://rowie-static.s3.us-east-2.amazonaws.com/nfts/k9-temp/k9-club/'
parser = argparse.ArgumentParser(description='Script para atualização automatica de urls')

parser.add_argument('-u', '--url', default=url_default, type=str, help='Url de acesso')
parser.add_argument('-r', '--range', type=int, help='Range de contagem')
parser.add_argument('-d', '--delay', type=int, help='Tempo de espera para carregamento da página')
args = parser.parse_args()

browser= webdriver.Chrome()
url_parsed = args.url
counter = args.range
wait_time = args.delay

while True:
    for i in range(counter+1):
        # browser.get(f'https://rowie-static.s3.us-east-2.amazonaws.com/nfts/k9-temp/k9-club/{i}.jpeg')
        browser.get(url_parsed+str(i)+'.jpeg')
        sleep(wait_time)
        browser.refresh()
        url_last = str(url_parsed+str(i)+'.jpeg')
    print('Leitura finalizada\n'\
          f'Última página lida: {url_last}')       
    break
    

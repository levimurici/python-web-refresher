import keyboard
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

loop_control = True

filename = 'url_log'+str(counter)+'.txt'

def file_write(url):
    f = open(filename, 'a')
    print('Url salva: ')
    print(url)
    f.write(url)
    f.close()

while True:
    for i in range(counter+1):
        browser.get(url_parsed+str(i)+'.jpeg')
        sleep(wait_time)
        browser.refresh()
        url_last = str(url_parsed+str(i)+'.jpeg')

        if keyboard.is_pressed('p'):
            file_write(url_last)
            sleep(.5)
        elif keyboard.is_pressed('c'):
            print('Loop interrompido\n')
            print(f'Última página lida: {url_last}')
            break
    print('Leitura finalizada\n'\
        f'Última página lida: {url_last}')
import requests


url = 'https://qr.ioi.tw/pt/'

with open('numeros.txt') as f:
    for line in f:
        print(line, end='')


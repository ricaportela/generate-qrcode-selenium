#!/usr/bin/env python
# coding: utf-8
# 200px, fronteira:1, raio:0, correção: 30%(H)
# dimensão: 4
# central
# central
""" Automatic QRCODE."""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
url = 'https://qr.ioi.tw/pt/'

driver.get(url)
time.sleep(5) # Let the user actually see something!
raw = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[8]/a')
driver.execute_script("arguments[0].click()", raw)                   
txtarea = driver.find_element_by_id('text')
txtarea.clear()
txtarea.send_keys('parametro de geração')
time.sleep(5) # Let the user actually see something!

btn_tamanho_cor = driver.find_element_by_xpath('//*[@id="s1"]')
driver.execute_script("arguments[0].click()", btn_tamanho_cor)
tamanho_imagem = driver.find_element_by_id('qrsi')
driver.execute_script("arguments[0].setAttribute('value','200')", tamanho_imagem)
tamanho_fronteira = driver.find_element_by_xpath('//*[@id="borderr"]/label[2]') 
driver.execute_script("arguments[0].click()", tamanho_fronteira)
correcao_erros = driver.find_element_by_xpath('//*[@id="errr"]/label[4]') 
driver.execute_script("arguments[0].click()", correcao_erros)
element = driver.find_element_by_xpath('//*[@id="radiusr"]/label[2]')
driver.execute_script("arguments[0].click()", element)

time.sleep(5) # Let the user actually see something!

btn_mais_logotipo = driver.find_element_by_xpath('//*[@id="s2"]')
driver.execute_script("arguments[0].click()", btn_mais_logotipo)
fotos = driver.find_element_by_xpath('//*[@id="labelmode"]/label[3]')
driver.execute_script("arguments[0].click()", fotos)
seleciona_foto = driver.find_element_by_id('image')
seleciona_foto.send_keys('/home/ricardo/dev/renivandro/tabelionato_xisto.jpeg')
dimensao = driver.find_element_by_xpath('//*[@id="fontsize"]/label[4]')
driver.execute_script("arguments[0].click()", dimensao)
time.sleep(5) # Let the user actually see something!

# <input type="file" class="custom-file-input" id="image">
# <img id="img-buffer" src="../dummy.png" style="display: none;">

param = "arguments[0].setAttribute('download','"+ "teste2.png" +"')"
baixa_qrcode = driver.find_element_by_id('dlbtn')
driver.execute_script(param, baixa_qrcode)
baixa_qrcode.click()


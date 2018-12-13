#!/usr/bin/env python
# coding: utf-8
# 200px, fronteira:1, raio:0, correção: 30%(H)
# dimensão: 4
# central
# central
""" Automatic Generate Qrcode from website."""
import logging
import os
import sys
from time import sleep, time
from datauri import DataURI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options as FireFoxoptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class GenerateQR():
    URLs = {
        "url": "https://qr.ioi.tw/pt/",
    }

    def __init__(self, headless=False, browser='Chrome'):  # change to true in production

        # self.driver = webdriver.PhantomJS(executable_path="../bin/phantomjs")

        if browser == 'Chrome':
            options = Options()
            options.add_argument('--no-sandbox')
            # options.add_argument('--window-size=1420,1080')
            options.add_argument('--disable-gpu')
            # options.add_argument('--disable-setuid-sandbox')
            # options.add_argument("--proxy-server='direct://'")
            # options.add_argument("--proxy-bypass-list=*")
            # options.add_argument("--disable-software-rasterizer")
            # options.add_argument("--mute-audio")
            # options.add_argument("--hide-scrollbars")
            # options.add_argument("--remote-debugging-port=9222")
            options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")
            # options.add_argument("--log-path=chromedriver.log")
            # options.add_argument("--verbose")

            if headless:
                options.add_argument('--headless')

            self.driver = webdriver.Chrome(
                executable_path="bin/chromedriver.exe", options=options)
        else:
            if browser == 'Firefox':
                options = FireFoxoptions()
                if headless:
                    options.add_argument('-headless')
                self.driver = webdriver.Firefox(
                    executable_path="bin/geckodriver", firefox_options=options)

   
        self.driver.set_page_load_timeout(930)
        try:
            self.driver.get(GenerateQR.URLs["url"])
        except TimeoutException:
            print("Timeout!!!")
            return
        except ValueError:
            return

    def parameters(self, line):
        self.driver.implicitly_wait(5)        
        self.findbyxpath('/html/body/div[2]/div/div[1]/ul/li[8]/a') # xpath para RAW button
        self.findbyxpath('//*[@id="s1"]')                           # xpath para definir tamanho e cor button
                                  
        txtarea = self.driver.find_element_by_id('text')
        txtarea.clear()
        txtarea.send_keys(str(line).strip()) # line: string - enviada a linha do arquivo texto para o campo 
                                             # para geração do qr code na web

        tamanho_imagem = self.driver.find_element_by_id('qrsi')
        self.driver.execute_script(
            "arguments[0].setAttribute('value','200')", tamanho_imagem)

        self.findbyxpath('//*[@id="borderr"]/label[2]')   # xpath para tamanho da fronteira
        self.findbyxpath('//*[@id="errr"]/label[4]')      # xpath para correcao de cor
        self.findbyxpath('//*[@id="radiusr"]/label[2]')   # xpath para tamanho do raio
        self.findbyxpath('//*[@id="s2"]')                 # xpath para definir logotipo
        self.findbyxpath('//*[@id="labelmode"]/label[3]') # xpath para definir foto
        
        sel_photo = self.driver.find_element_by_id('image')
        sel_photo_path = 'C:/dev/generate-qrcode-selenium/img/tabelionato_xisto.jpeg'
        sel_photo.send_keys(sel_photo_path)

        self.findbyxpath('//*[@id="fontsize"]/label[4]')  # xpath para dimensoes

        imagem = (line.split('=')[1].strip()) + '.png' # separando a URL e o numero para 
                                             # o nome do arquivo de imagem(PNG)
        param = "arguments[0].setAttribute('download','" + imagem + "')"
        self.driver.implicitly_wait(5)        

        baixa_qrcode = self.driver.find_element_by_id('dlbtn')
        self.driver.execute_script(param, baixa_qrcode)

        self.driver.implicitly_wait(5) 

        baixa_qrcode.click()

        self.datauri(baixa_qrcode, imagem)

    def datauri(self, baixa_qrcode, imagem):
        """ Salva imagem com URI Basecode64."""
        self.driver.implicitly_wait(5) 
        url = baixa_qrcode.get_property('href')
        uri = DataURI(url)
        with open("C:/dev/generate-qrcode-selenium/qrcodes_imgs" + imagem, 'wb') as f:
            f.write(uri.data)

    def findbyxpath(self, param_xpath):
        """ Encontra elemento html com xpath."""
        self.driver.implicitly_wait(5)        
        try:
            element = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, param_xpath)))
        finally:
            self.driver.execute_script("arguments[0].click()", element)

    def close(self):
        self.driver.quit()
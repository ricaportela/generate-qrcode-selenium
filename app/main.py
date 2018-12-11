#!/usr/bin/env python
# coding: utf-8
# 200px, fronteira:1, raio:0, correção: 30%(H)
# dimensão: 4
# central
# central
""" AutomGenerate Qrcode form website."""
import logging
import os
import sys
import time
from datauri import DataURI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FireFoxoptions
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
            options.add_argument('--window-size=1420,1080')
            options.add_argument('--disable-gpu')
            if headless:
                options.add_argument('--headless')

            self.driver = webdriver.Chrome(
                executable_path="bin/chromedriver.exe", options=options, 
                service_args=['--verbose', '--log-path=chromedriver.log'])
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

    def parameters(self, numero):
        time.sleep(2)  # Let the user actually see something!
        self.newmethod555('/html/body/div[2]/div/div[1]/ul/li[8]/a')

        txtarea = self.driver.find_element_by_id('text')
        txtarea.clear()
        txtarea.send_keys('parametro de geração')
        # time.sleep(2)  # Let the user actually see something!

        btn_tamanho_cor_xpath = '//*[@id="s1"]'
        btn_tamanho_cor = self.driver.find_element_by_xpath(
            btn_tamanho_cor_xpath)
        self.driver.execute_script("arguments[0].click()", btn_tamanho_cor)

        tamanho_imagem = self.driver.find_element_by_id('qrsi')
        self.driver.execute_script(
            "arguments[0].setAttribute('value','200')", tamanho_imagem)

        size_frontier_xpath = '//*[@id="borderr"]/label[2]'
        size_frontier = self.driver.find_element_by_xpath(size_frontier_xpath)
        self.driver.execute_script("arguments[0].click()", size_frontier)

        error_cor_xpath = '//*[@id="errr"]/label[4]'
        error_cor = self.driver.find_element_by_xpath(error_cor_xpath)
        self.driver.execute_script("arguments[0].click()", error_cor)

        radius_xpath = '//*[@id="radiusr"]/label[2]'
        radius = self.driver.find_element_by_xpath(radius_xpath)
        self.driver.execute_script("arguments[0].click()", radius)

        # time.sleep(2)  # Let the user actually see something!

        btn_mais_logotipo = self.driver.find_element_by_xpath('//*[@id="s2"]')
        self.driver.execute_script("arguments[0].click()", btn_mais_logotipo)

        photo_xpath = '//*[@id="labelmode"]/label[3]'
        photo = self.driver.find_element_by_xpath(photo_xpath)
        self.driver.execute_script("arguments[0].click()", photo)

        sel_photo = self.driver.find_element_by_id('image')
        sel_photo_path = 'C:/dev/generate-qrcode-selenium/img/tabelionato_xisto.jpeg'
        sel_photo.send_keys(sel_photo_path)

        dimension_xpath = '//*[@id="fontsize"]/label[4]'
        dimension = self.driver.find_element_by_xpath(dimension_xpath)
        self.driver.execute_script("arguments[0].click()", dimension)

        # time.sleep(2)  # Let the user actually see something!

        # <input type="file" class="custom-file-input" id="image">
        # <img id="img-buffer" src="../dummy.png" style="display: none;">
        # time.sleep(5)  # Let the user actually see something!

        # image_src = self.driver.find_element_by_id('img-buffer')
        # image_src = "arguments[0].setAttribute('src','" + \
        #     "images/teste2.png" + "')"

        imagem = str(numero.strip() + '.png')
        print(imagem)
        param = "arguments[0].setAttribute('download','" + imagem + "')"
        baixa_qrcode = self.driver.find_element_by_id('dlbtn')
        self.driver.execute_script(param, baixa_qrcode)

        time.sleep(5)  # Let the user actually see something!

        baixa_qrcode.click()

        url = baixa_qrcode.get_property('href')
        uri = DataURI(url)
        with open("c:/xisto/" + imagem, 'wb') as f:
            f.write(uri.data)

    def newmethod555(self, param_xpath):
        element = self.driver.find_element_by_xpath(param_xpath)
        self.driver.execute_script("arguments[0].click()", element)

        # time.sleep(5)  # Let the user actually see something!

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    qr = GenerateQR()
    qr.parameters('1123123123332')
    qr.close()
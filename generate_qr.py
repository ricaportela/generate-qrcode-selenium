#!/usr/bin/env python
# coding: utf-8
# 200px, fronteira:1, raio:0, correção: 30%(H)
# dimensão: 4
# central
# central
""" Automatic QRCODE."""
import time
from selenium import webself.driver
from selenium.webself.driver.common.by import By
from selenium import webself.driver
from selenium.common.exceptions import TimeoutException
from selenium.webself.driver.chrome.options import Options
from selenium.webself.driver.common.by import By
from selenium.webself.driver.firefox.options import Options as FireFoxoptions
from selenium.webself.driver.support import expected_conditions as EC
from selenium.webself.driver.support.ui import Webself.driverWait


class GenerateQR():
    URLs = {
        "url": "https://qr.ioi.tw/pt/",
    }

    def __init__(self, headless=False, browser='Chrome'):  # em producao TRUE

        # self.self.driver = webself.driver.PhantomJS(executable_path="../bin/phantomjs")

        if browser == 'Chrome':
            options = Options()
            if headless:
                options.add_argument('--headless')
            self.self.driver = webself.driver.Chrome(
                executable_path="bin/chromeself.driver", chrome_options=options)
        else:
            if browser == 'Firefox':
                options = FireFoxoptions()
                if headless:
                    options.add_argument('-headless')
                self.self.driver = webself.driver.Firefox(
                    executable_path="bin/geckoself.driver", firefox_options=options)

        # self.driver = webself.driver.Chrome('./chromeself.driver')  # Optional argument, if not specified will search path.

        # self.driver.get(url)
        time.sleep(5)  # Let the user actually see something!
        raw = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[1]/ul/li[8]/a')
        self.driver.execute_script("arguments[0].click()", raw)
        txtarea = self.driver.find_element_by_id('text')
        txtarea.clear()
        txtarea.send_keys('parametro de geração')
        time.sleep(5)  # Let the user actually see something!

        btn_tamanho_cor = self.driver.find_element_by_xpath('//*[@id="s1"]')
        self.driver.execute_script("arguments[0].click()", btn_tamanho_cor)
        tamanho_imagem = self.driver.find_element_by_id('qrsi')
        self.driver.execute_script(
            "arguments[0].setAttribute('value','200')", tamanho_imagem)
        tamanho_fronteira = self.driver.find_element_by_xpath(
            '//*[@id="borderr"]/label[2]')
        self.driver.execute_script("arguments[0].click()", tamanho_fronteira)
        correcao_erros = self.driver.find_element_by_xpath(
            '//*[@id="errr"]/label[4]')
        self.driver.execute_script("arguments[0].click()", correcao_erros)
        element = self.driver.find_element_by_xpath(
            '//*[@id="radiusr"]/label[2]')
        self.driver.execute_script("arguments[0].click()", element)

        time.sleep(5)  # Let the user actually see something!

        btn_mais_logotipo = self.driver.find_element_by_xpath('//*[@id="s2"]')
        self.driver.execute_script("arguments[0].click()", btn_mais_logotipo)
        fotos = self.driver.find_element_by_xpath(
            '//*[@id="labelmode"]/label[3]')
        self.driver.execute_script("arguments[0].click()", fotos)
        seleciona_foto = self.driver.find_element_by_id('image')
        seleciona_foto.send_keys(
            '/home/ricardo/dev/renivandro/tabelionato_xisto.jpeg')
        dimensao = self.driver.find_element_by_xpath(
            '//*[@id="fontsize"]/label[4]')
        self.driver.execute_script("arguments[0].click()", dimensao)
        time.sleep(5)  # Let the user actually see something!

        # <input type="file" class="custom-file-input" id="image">
        # <img id="img-buffer" src="../dummy.png" style="display: none;">

        param = "arguments[0].setAttribute('download','" + "teste2.png" + "')"
        baixa_qrcode = self.driver.find_element_by_id('dlbtn')
        self.driver.execute_script(param, baixa_qrcode)
        baixa_qrcode.click()

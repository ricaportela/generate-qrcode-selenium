#!/usr/bin/env python
# coding: utf-8
# 200px, fronteira:1, raio:0, correção: 30%(H)
# dimensão: 4
# central
# central
""" AutomGenerate Qrcode form website."""
import time
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
            if headless:
                options.add_argument('--headless')
                # options.add_argument("--start-maximized")
                # options.add_argument("download.default_directory=C:/xisto")
                options.add_argument('--ignore-certificate-errors')
                options.add_argument("--test-type")

            self.driver = webdriver.Chrome(
                executable_path="bin/chromedriver.exe", chrome_options=options)
        else:
            if browser == 'Firefox':
                options = FireFoxoptions()
                if headless:
                    options.add_argument('-headless')
                self.driver = webdriver.Firefox(
                    executable_path="bin/geckodriver", firefox_options=options)

    def main(self):
        print("Opening qrcode page")
        self.driver.set_page_load_timeout(930)
        try:
            self.driver.get(GenerateQR.URLs["url"])
        except TimeoutException:
            print("Timeout!!!")
            return
        except ValueError:
            return
        time.sleep(2)  # Let the user actually see something!
        raw_xpath = '/html/body/div[2]/div/div[1]/ul/li[8]/a'
        raw = self.driver.find_element_by_xpath(raw_xpath)
        self.driver.execute_script("arguments[0].click()", raw)

        txtarea = self.driver.find_element_by_id('text')
        txtarea.clear()
        txtarea.send_keys('parametro de geração')
        time.sleep(2)  # Let the user actually see something!

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

        time.sleep(2)  # Let the user actually see something!

        btn_mais_logotipo = self.driver.find_element_by_xpath('//*[@id="s2"]')
        self.driver.execute_script("arguments[0].click()", btn_mais_logotipo)

        photo_xpath = '//*[@id="labelmode"]/label[3]'
        photo = self.driver.find_element_by_xpath(photo_xpath)
        self.driver.execute_script("arguments[0].click()", photo)

        sel_photo = self.driver.find_element_by_id('image')
        sel_photo_path = 'c:/xisto/tabelionato_xisto.jpeg'
        sel_photo.send_keys(sel_photo_path)

        dimension_xpath = '//*[@id="fontsize"]/label[4]'
        dimension = self.driver.find_element_by_xpath(dimension_xpath)
        self.driver.execute_script("arguments[0].click()", dimension)

        time.sleep(2)  # Let the user actually see something!

        # <input type="file" class="custom-file-input" id="image">
        # <img id="img-buffer" src="../dummy.png" style="display: none;">
        time.sleep(5)  # Let the user actually see something!

        image_src =  self.driver.find_element_by_id('img-buffer')
        image_src = "arguments[0].setAttribute('src','" + "images/teste2.png" + "')"


        param = "arguments[0].setAttribute('download','" + "teste2.png" + "')"
        baixa_qrcode = self.driver.find_element_by_id('dlbtn')
        self.driver.execute_script(param, baixa_qrcode)
        baixa_qrcode.click()

        time.sleep(5)  # Let the user actually see something!

        self.close()

    def close(self):
        self.driver.quit()

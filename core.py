#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Main program execute generate_qr_code."""
from app.generate_qr import GenerateQR
from time import sleep, time


if __name__ == "__main__":
    print('Inicio Geração QRCODE')
    start_time = time()
    qr = GenerateQR()
    with open('numeros.txt') as f:
        for line in f:
            qr.parameters(str(line).strip())
    qr.close()
    end_time = time()
    elapsed_time = end_time - start_time
    print(f'Fim geração - Tempo: {elapsed_time} segundos')
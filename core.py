#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Main program execute generate_qr_code."""
from app.generate_qr import GenerateQR


if __name__ == "__main__":
    qr = GenerateQR()
    qr.main()
    with open('numeros.txt') as f:
         for line in f:
             qr.parameters(str(line).strip())
    #qr.parameters("111111111111")
    qr.close()
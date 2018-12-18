import qrcode
from time import time
from PIL import Image


def create_qrcode(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    img = img.convert("RGBA")
    
    icon = Image.open('img/tabelionato_xisto.jpeg')
    w, h = img.size
    factor = 4
    size_w = int(w / factor)
    size_h = int(h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    w = int((w - icon_w) / 2)
    h = int((h - icon_h) / 2)
    icon = icon.convert("RGBA")
    newimg = Image.new("RGBA", (icon_w + 8, icon_h + 8), (255, 255, 255))
   
    img.paste(newimg, (w-4, h-4), newimg)
    img.paste(icon, (w, h), icon)
    img.format ='BMP'
    
    qr_imagem = img.save('qr_imgs/' + imagem + '.bmp', 'bmp', quality=100)
    return qr_imagem


if __name__ == "__main__":
    print('Inicio Geração das images com os QR codes...')
    start_time = time()
    with open('input_data.txt') as f: # 
        for line in f:
            data = line
            imagem = (line.split('=')[1].strip())
            create_qrcode(data, imagem)
    
    end_time = time()
    elapsed_time = end_time - start_time
    print(f'Fim geração - Tempo: {elapsed_time} segundos')
    
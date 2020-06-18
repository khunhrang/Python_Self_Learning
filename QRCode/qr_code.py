import qrcode

def basic():
    txt = "Atinon Jongrag QRCode"
    img = qrcode.make(txt)
    img.show()

def adv():
    qr = qrcode.QRCode(box_size=5, border=2)
    qr.add_data("https://www.foodpanda.co.th/restaurant/f7jz/kanom-krok-singapore-by-krua-khun-lang?r=1&utm_source=facebook&utm_medium=display&utm_campaign=smartly_rma_and_mix_aut_app_foodpanda_th_dpa_fb_mix_ct-xxx#")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    #img.show()
    img.save("qr.png")

if __name__ == '__main__':
    #basic()
    adv()
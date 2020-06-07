Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import songline
>>> token = 'PQQKK4EptkiKM9QAl1YHcdaKXi4rShQIxlBj7Ogznpa'
>>> messenger = songline.Sendline(token)
>>> messenger.sendtext('สวัสดีจร้า')
<Response [400]>
>>> messenger.sendtext('สวัสดีจร้า')
<Response [200]>
>>> messenger.sticker(629,4)
<Response [200]>
>>> messenger.sendimage('https://www.thebangkokinsight.com/wp-content/uploads/2019/05/%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%A7%E0%B8%B4%E0%B8%95%E0%B8%A3175621.jpg')
<Response [200]>
>>> 
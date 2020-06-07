#temperature.py
#GroupFamily = 'PQQKK4EptkiKM9QAl1YHcdaKXi4rShQIxlBj7Ogznpa'
#GroupBall = 'G3xy6c1vv9BYAVgSGpwmWQuauTxysbOPf0luKYVRcNz'

from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

def Temperature(pvid):
    try:
        # 1- URL
        url = 'https://www.tmd.go.th/province.php?id=' + str(pvid)
        #pvid = province id from website

        # 2- Request URL
        webopen = req(url)
        page_html = webopen.read()
        webopen.close()

        # 3- Convert page_html to Soup Object
        #print(page_html)
        data = soup(page_html,'html.parser')
        #print(data)

        # 4- Find Element ( td:'strokeme')
        temp = data.findAll('td',{'class':'strokeme'})
        province = data.findAll('span',{'class':'title'})
        pv = province[0].text.replace(' ','')
        result = temp[0].text

        print(f'จังหวัด: {pv} อุณหภูมิ: {result}')
        text = f'จังหวัด: {pv} อุณหภูมิ: {result}'
        return text
    except:
        print('No Result')
        return 'No Result'

    
for i in range(1,77):
    import songline
    token = 'hAVupcYnMyOalL45LZR3NjYkLyrLWmOww60gHNABWkp'
    myprovince=Temperature(i)
    messenger = songline.Sendline(token)  
    messenger.sendtext(myprovince)

'''
    import songline
    token = 'PQQKK4EptkiKM9QAl1YHcdaKXi4rShQIxlBj7Ogznpa'
    messenger = songline.Sendline(token)  
    messenger.sendtext(myprovince)          
'''


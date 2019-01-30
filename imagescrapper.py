import requests
import bs4
import bs4
import  matplotlib.pyplot as plt
from PIL import Image
n=input("enter your link:")
p=input("Enter your File name:")
res=requests.get(n)
soup=bs4.BeautifulSoup(res.text,"lxml")
#print(soup)
#soup.title
img=soup.find_all('img')
for i in range (len(img)):
    try:
        response=requests.get(img[i]['src'],stream=True)
        img_op=Image.open(response.raw)
        plt.imshow(img_op)
        img_op.save(r.format(str(i)))
    except:
        KeyError
    else:
        pass
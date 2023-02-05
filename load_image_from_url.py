from tkinter import *
from PIL import ImageTk, Image
from io import BytesIO
import requests
import parsel

root = Tk()

def getRequest(html_url):
    # 發送請求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
    }
    response = requests.get(url=html_url, headers=headers)
    return response.text

def getResponse(html_url):
    response = getRequest(html_url)
    data = parsel.Selector(response)
    model_img_url = data.xpath('//div[@class="model"]/div/a/img/@src').extract()
    # model_img_url_1 = model_img_url[0]
    return model_img_url

def getModelName(html_url):
    response = getRequest(html_url)
    data = parsel.Selector(response)
    model_name = data.xpath('//div[@class="model_name"]/text()').extract()
    # model_name_1 = model_name[0]
    return model_name

url = 'https://ggjav.com/main/all_censored_model'

url1 = getResponse(url)

model_name = getModelName(url)
# print(model_name[0])



# image_url = "https://cdn-1.ggjav.com/media/model/5.jpg"
r = requests.get(url1[0])
pilImage = Image.open(BytesIO(r.content))
pilImage = pilImage.resize((100,100))

image = ImageTk.PhotoImage(pilImage)
label = Button(root, text=model_name[0] ,image=image, compound = TOP, padx=5, pady=5)
label.pack()

root.mainloop()


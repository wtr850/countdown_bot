# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import requests
from requests_oauthlib import OAuth1
import json
import datetime

class Twitter:
    #これから書くよ
    
def countdown():
    today = datetime.today()
    sotsubu_day = datetime.date(2019, 12, 10)
    days_left = sotsubu_day - today

    return days_left

days = countdown()
#初期設定
img = Image.open("sotsubu.png")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("Font/Arial.ttf", 170)

#文字の入力
draw.text((855, 790), str(days), fill=(0, 0, 0),font=font)

img.save("cat_text.png")
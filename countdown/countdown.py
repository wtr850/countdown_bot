# -*- coding: utf-8 -*-
import os, datetime, csv, json
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import requests
from requests_oauthlib import OAuth1

class CreateImage:
	def __init__(self, size): #logっていう変数消したよ
		self.imgSize = size
		self.img = Image.new("RGB", size, (255, 255, 255))
		self.text = { "font" : None, "size" : None, "rgba" : None }

	def addNext(self,r,g,b):
		self.nextImg = Image.new("RGBA", (10000,10000), (r, g, b, 0))
		return self

	def addImage(self, pos = (0, 0) , size = None):
		size = size if size else self.imgSize
		#size = (100000,1000000)
		self.img.paste(self.nextImg, pos, self.nextImg)

	def nextImage(self, src, pos = (0, 0) , size = None):
		size = size if size else self.imgSize
		img = Image.open(src).resize(size)
		self.nextImg.paste(img, pos)
		del img
		return self

	def nextText(self, text, pos, rgba = None, font = None, size = None): 
		rgbaSet = rgba if rgba else self.text["rgba"]
		color = (rgbaSet[0], rgbaSet[1], rgbaSet[2], round(rgbaSet[3] * 255))
		fontSet = font if font else self.text["font"]
		sizeSet = size if size else self.text["size"]
		imagefont = ImageFont.truetype(font = fontSet , size = sizeSet , encoding = "unic")

		draw = ImageDraw.Draw(self.nextImg)
		draw.text(pos, text = text, imagefont = fontSet, fill = color)
		del draw
		return self
	
	def save(self):
		self.img.save("unko.png")
	
if __name__ == "__main__":
	imgSize = (600, 500)
	textColor = (255, 255, 255, 1.0)
	fontSrc = {
		"ShinGo-EL" : "Fonts/Arial.ttf",
		"Gotham-Thin" : "Fonts/Arial.ttf",
	}
	imgSrc = {
		"template" : "img/sotsubu.png",
		#"template-date" : "img/template-date.png",
	}
	
	img = CreateImage(imgSize)
	img.addNext(255, 255, 255).nextImage(imgSrc["template"]).addImage()
	#img.addNext(255, 255, 255).nextImage(imgSrc["template-date"]).addImage()
	img.text["rgba"] = textColor
	img.text["font"] = fontSrc["ShinGo-EL"]
	img.addNext(255, 255, 255).nextText("AAAAAA", (100,450), size =10000000).addImage(size = 100000)

	x = 704
	y = 194
	img.text["size"] = 120
	img.addNext(255, 255, 255).nextText("00", (x, y - 150))
	img.nextText("00", (x, y))
	img.nextText("00", (x, y + 150)).addImage()
	
	img.save()
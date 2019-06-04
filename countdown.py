from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

class CreateImage:
	def __init__(self, size, log):
		self.imgSize = size
		self.img = Image.new("RGB", size, (255, 255, 255))
		self.text = { "font" : None, "size" : None, "rgba" : None }

    def addNext(self,r,g,b):
	    self.nextImg = Image.new("RGBA", self.imgSize, (r, g, b, 0))
	    return self

    def addImage(self, pos = (0, 0) , size = None):
	    size = size if size else self.imgSize
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

    if __name__ == "__main__"
	    imgSize = (1000, 500)
	    textColor = (255, 255, 255, 1.0)
	    fontSrc = {
		    "ShinGo-EL" : フォントファイルのパス,
	    	"Gotham-Thin" : フォントファイルのパス
	    }
	    imgSrc = {
    		"template" : "img/sotsubu.png",
    		#"template-date" : "img/sotsubu-date.png",
    	}
	
    	img = CreateImage(imgSize, log)
    	img.addNext(255, 255, 255).nextImage(imgSrc["sotsubu"]).addImage()
    	#img.addNext(255, 255, 255).nextImage(imgSrc["template-date"]).addImage()
    	img.text["rgba"] = textColor
       	img.text["font"] = fontSrc["ShinGo-EL"]
    	img.addNext(255, 255, 255).nextText("金", (311,380), size = 70).addImage()
# Author: 	Achilleas Papakonstantinou (A.S.M. 1490003982013)
# Date:		5/7/2019
# INFO:	

from PIL import Image, ImageDraw, ImageFont, ImageFilter

ranks=['Στρατηγός', 'Αντιστράτηγος', 'Υποστράτηγος', 'Ταξίαρχος', 'Συνταγματάρχης', 'Αντισυνταγματάρχης', 'Ταγματάρχης', 'Λοχαγός', 'Υπολοχαγός', 'Ανθυπολοχαγός', 'Δόκιμος Έφεδρος Αξιωματικός', 'Ανθυπασπιστής', 'Αρχιλοχίας', 'Επιλοχίας','Λοχίας', 'Δεκανέας', 'Υποδεκανέας']
name = input("ΔΩΣΕ ΟΝΟΜΑ: ")

for i in range (0,len(ranks)):
	print(str(i+1) + ": " +ranks[i])

rank = int(input("ΕΠΙΛΕΞΕ ΒΑΘΜΟ: "))
oplo = input("ΟΠΛΟ (πχ. ΠΒ): ")
#font_size = int(input("ΜΕΓΕΘΟΣ ΓΡΑΜΜΑΤΟΣΕΙΡΑΣ (πχ. 90): "))
font_size = 70

x = int(input("ΔΙΑΣΤΑΣΗ x (πχ. 980): "))
y = int(input("ΔΙΑΣΤΑΣΗ y (πχ. 550): "))

img = Image.new('RGBA', (1344, 265), color = (73, 109, 137))
d = ImageDraw.Draw(img)
img.save('test.png')

img = Image.open("bg.png")

# draw = ImageDraw.Draw(img)
img = img.convert("RGBA")

tmp = Image.new('RGBA', img.size, (0,0,0,0))

# Create a drawing context for it.
draw = ImageDraw.Draw(tmp)

# Alpha composite the two images together.
img = Image.alpha_composite(img, tmp)
img = img.convert("RGB") # Remove alpha for saving in jpg format.
img.save('test.png')

unicode_font_big = ImageFont.truetype("C:\Windows\Fonts\Tahoma.ttf", font_size)

d = ImageDraw.Draw(img)

w, h = draw.textsize(name, font=unicode_font_big)
d.text(( ((1344-w)/2) + 30, 30), name, font=unicode_font_big, fill=(0,0,0))
w, h = draw.textsize(ranks[rank-1], font=unicode_font_big)
d.text(( ((1344-w)/2) + 30, 130), ranks[rank-1], font=unicode_font_big, fill=(0,0,0))

img.save('test.png')

background = Image.open("test.png")
foreground = Image.open("vathmoi/"+ranks[rank-1]+".png")
background.paste(foreground, (1200, 5), foreground)
background.save('test.png')


background = Image.open("test.png")
foreground = Image.open("opla/"+oplo+".png")

size = 250, 250
foreground.thumbnail(size, Image.ANTIALIAS)
foreground.save("opla/"+oplo+"_resized.png")
foreground = Image.open("opla/"+oplo+"_resized.png")

background.paste(foreground, (20, 10), foreground)

background.save('test.jpg')

size = x,y
final = Image.open("test.jpg")
final.thumbnail(size, Image.ANTIALIAS)
final.save("final.jpg")

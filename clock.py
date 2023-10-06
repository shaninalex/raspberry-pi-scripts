# Display clock for OLED 0.91 display in format
# Friday, 06.10.2023
# 20:38:42

import time
import subprocess
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

disp.fill(0)
disp.show()

width = disp.width
height = disp.height
image = Image.new("1", (width, height))

draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=0)
padding = -2
top = padding
bottom = height - padding
x = 0

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)

while True:
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    current_time = time.strftime("%A, %d.%m.%Y")
    draw.text((x, top + 0), current_time, font=font, fill=255)

    text = time.strftime("%X")
    draw.text((0, 12), text, font=font2, fill=255)

    disp.image(image)
    disp.show()
    time.sleep(0.1)

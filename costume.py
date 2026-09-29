import sys
from PIL import Image #library used for pictures called pillow

images = []
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costume.gif",save_all = True,append_images =[images[1]]
    duration = 200,loop = 0
)
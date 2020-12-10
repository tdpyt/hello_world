
import glob
import os
from PIL import Image
files = (glob.glob('../**/', recursive=True))
for file in files:
    print(file)
#
# files = glob.glob('*.jpg')
# for file in files:
#     im = Image.open(file)
#     print(file)
#     im.show()
#
#

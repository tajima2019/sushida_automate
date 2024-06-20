import cv2
import pyocr
import pyocr.builders
from PIL import Image

tools = pyocr.get_available_tools()
tool = tools[0]
img_org = Image.open('./img/string_img.png')
builder = pyocr.builders.TextBuilder(tesseract_layout=10)
result = tool.image_to_string(img_org, lang="eng", builder=builder)
print(result)

from PIL import Image, ImageEnhance, ImageOps
from pytesseract import pytesseract
import urllib.request
from io import BytesIO

class imageReader:
    def __init__(self):
        path = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        pytesseract.tesseract_cmd = path
    
    def extract_text(self, url):
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(req) as ImgUrl:
            imageData = ImgUrl.read()
        
        img = Image.open(BytesIO(imageData)).convert("RGB")

        img = img.convert("L")
        img = ImageEnhance.Contrast(img).enhance(3)
        img = ImageEnhance.Brightness(img).enhance(1.5)
        img = img.point(lambda x: 0 if x < 128 else 225, '1')

        imageConvert = BytesIO()
        img.save(imageConvert, format="PNG")
        imageConvert.seek(0)

        extracted_text = pytesseract.image_to_string(Image.open(imageConvert), lang="eng")
        return extracted_text
    
# if __name__ == "__main__":
#     ir = imageReader()
#     text = ir.extract_text()
#     print(text)
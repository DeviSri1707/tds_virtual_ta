import base64
from PIL import Image
from io import BytesIO
import pytesseract

def extract_text_from_image(image_b64):
    image = Image.open(BytesIO(base64.b64decode(image_b64)))
    text = pytesseract.image_to_string(image)
    return text

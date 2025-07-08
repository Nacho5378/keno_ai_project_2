import easyocr
import numpy as np
from PIL import Image
import tempfile

reader = easyocr.Reader(['en'], gpu=False)

def extract_numbers_from_image(image_file):
    img = Image.open(image_file).convert("RGB")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        img.save(tmp.name)
        result = reader.readtext(tmp.name, detail=0)

    digits = []
    for item in result:
        for part in item.split():
            if part.isdigit():
                num = int(part)
                if 1 <= num <= 80:
                    digits.append(num)

    return sorted(list(set(digits)))

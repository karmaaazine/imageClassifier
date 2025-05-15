from PIL import Image
import io

def read_imagefile(file) -> Image.Image:
    image = Image.open(io.BytesIO(file))
    image = image.convert("RGB")
    image = image.resize((224, 224))
    return image

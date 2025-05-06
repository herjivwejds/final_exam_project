from PIL import Image
import os

# Webp rasmlar saqlangan papka yo‘li
input_dir = 'media/products/'   # Django media yo‘li
output_format = 'JPEG'  # Yoki 'PNG'

for filename in os.listdir(input_dir):
    if filename.lower().endswith('.webp'):
        img_path = os.path.join(input_dir, filename)
        img = Image.open(img_path).convert('RGB')
        new_filename = filename.replace('.webp', '.jpg')
        new_path = os.path.join(input_dir, new_filename)
        img.save(new_path, output_format)
        print(f"{filename} → {new_filename}")

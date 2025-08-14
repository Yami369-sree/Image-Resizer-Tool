import os
from PIL import Image

# ----------- Settings -----------
input_folder = "images_input"   # Folder containing original images
output_folder = "images_output" # Folder to save resized images
new_size = (800, 800)           # Width, Height in pixels
output_format = "JPEG"          # Options: "JPEG", "PNG", etc.
# --------------------------------

def resize_images():
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.gif')):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            # Resize image
            img_resized = img.resize(new_size)

            # Save in output folder
            base_name = os.path.splitext(filename)[0]
            save_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")
            img_resized.save(save_path, output_format)
            print(f"✅ Resized and saved: {save_path}")

if __name__ == "__main__":
    resize_images()
    print("🎯 All images resized successfully!")

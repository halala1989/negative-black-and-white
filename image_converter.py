import os
from PIL import Image
from tqdm import tqdm

def process_image(image_path):
    try:
        with Image.open(image_path) as img:
            # Convert to grayscale
            gray_img = img.convert('L')
            # Invert colors
            inverted_img = Image.eval(gray_img, lambda x: 255 - x)
            # Overwrite original file
            inverted_img.save(image_path)
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def process_directory(directory):
    for root, _, files in os.walk(directory):
        jpg_files = [f for f in files if f.lower().endswith('.jpg')]
        for file in tqdm(jpg_files, desc="Processing images"):
            file_path = os.path.join(root, file)
            process_image(file_path)

if __name__ == "__main__":
    print("Starting image processing...")
    current_dir = os.getcwd()
    process_directory(current_dir)
    print("Processing complete!")
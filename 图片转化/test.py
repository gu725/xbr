import os
from PIL import Image

# Define the source and target directories
source_folder = r"C:\Users\17978\Desktop\museum-master (2)\待处理图片"  # Replace with the folder containing your images
target_folder = r"C:\Users\17978\Desktop\museum-master (2)\处理后图片"  # Replace with the folder where processed images will be saved

# Create target folder if it doesn't exist
os.makedirs(target_folder, exist_ok=True)

# Define the target size
target_size = (930, 290)  # Replace with your desired width and height

# Loop through all images in the source folder
for filename in os.listdir(source_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # Open the image
        image_path = os.path.join(source_folder, filename)
        with Image.open(image_path) as img:
            # Resize the image to the target size
            resized_img = img.resize(target_size)

            # Save the processed image to the target folder
            output_path = os.path.join(target_folder, filename)
            resized_img.save(output_path)

print(f"Images have been resized to {target_size} and saved in '{target_folder}'.")

import os
import shutil
from PIL import Image  # Import Pillow

# Settings
source_folder = 'edited_image'          # <<< replace with your source folder path
destination_folder = 'dataset/grizzly_bear/images'  # <<< replace with your destination folder path

# Make sure destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Define the range of original images
start_number = 165
end_number = 260

# Target size
target_size = (994, 738)

# Loop through the range
for idx, original_number in enumerate(range(start_number, end_number + 1), start=1):
    # Build original filename
    original_filename = f"edited_img_{original_number}.png"
    source_path = os.path.join(source_folder, original_filename)

    # Build new filename: frame_00001.jpg etc.
    new_filename = f"frame_{idx:05d}.jpg"
    destination_path = os.path.join(destination_folder, new_filename)

    # Check if source file exists
    if os.path.exists(source_path):
        try:
            # Open image
            with Image.open(source_path) as img:
                # Resize image
                resized_img = img.resize(target_size, Image.LANCZOS)
                # Save as JPG
                resized_img.convert('RGB').save(destination_path, 'JPEG')
            print(f"Resized & saved {original_filename} --> {new_filename}")
        except Exception as e:
            print(f"ERROR processing {original_filename}: {e}")
    else:
        print(f"WARNING: {original_filename} not found!")

print("All done!")

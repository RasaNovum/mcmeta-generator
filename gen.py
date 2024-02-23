import os
import shutil

textures_dir = './textures/'
mcmetas_dir = './mcmetas/'
default_mcmeta = './default.mcmeta'

# Add neccecary folders
if os.path.exists(textures_dir) == False:
    os.makedirs(textures_dir)
if os.path.exists(mcmetas_dir) == False:
    os.makedirs(mcmetas_dir)

# Get all image files in the textures directory
image_files = [f for f in os.listdir(textures_dir) if os.path.isfile(os.path.join(textures_dir, f))]

# For each image file, copy the default.mcmeta file into the mcmetas directory with the same name
for image_file in image_files:
    # Get the base name without the extension
    base_name = os.path.splitext(image_file)[0]
    # Define the destination path
    dest_path = os.path.join(mcmetas_dir, base_name + '.png' + '.mcmeta')
    # Copy the file
    shutil.copyfile(default_mcmeta, dest_path)
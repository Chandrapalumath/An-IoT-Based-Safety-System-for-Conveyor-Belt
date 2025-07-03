import os

# Path to the folder containing images
folder_path = r"C:\Users\ABC\Downloads\Lettuce Images"

# Get list of image files (you can filter for specific extensions if needed)
images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
images.sort()  # Optional: sort alphabetically

# Rename each image
for i, filename in enumerate(images, start=1):
    new_name = f"{i}.jpg"
    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, new_name)
    os.rename(src, dst)

print("Renaming complete.")

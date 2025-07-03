import os

image_dir = r'E:\classified\foreign'      # Folder where your images are stored
label_dir = r'E:\classified\labels'      # Folder where .txt label files are stored
image_exts = ['.jpg', '.png', '.jpeg']  # Allowed image formats

deleted = 0

for img_file in os.listdir(image_dir):
    img_name, ext = os.path.splitext(img_file)
    if ext.lower() not in image_exts:
        continue

    label_file = img_name + '.txt'
    label_path = os.path.join(label_dir, label_file)

    if not os.path.exists(label_path):
        img_path = os.path.join(image_dir, img_file)
        os.remove(img_path)
        deleted += 1

print(f"✅ Deleted {deleted} images with no corresponding label files.")

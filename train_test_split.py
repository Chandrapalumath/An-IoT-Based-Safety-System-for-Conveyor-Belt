import os
import random
import shutil

# 🔧 Update your paths here
images_dir = r"E:\classified\foreign"
labels_dir = r"E:\classified\labels"

output_base = r"C:\Users\ABC\Desktop\foreign_object_dataset_split"
train_images_dir = os.path.join(output_base, 'images', 'train')
val_images_dir = os.path.join(output_base, 'images', 'val')
train_labels_dir = os.path.join(output_base, 'labels', 'train')
val_labels_dir = os.path.join(output_base, 'labels', 'val')

# 📁 Create directories
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# 📷 Get all image files
image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
random.shuffle(image_files)

# 📊 Split 80% train / 20% val
split_idx = int(0.8 * len(image_files))
train_files = image_files[:split_idx]
val_files = image_files[split_idx:]

def move_files(image_list, src_img_dir, src_lbl_dir, dest_img_dir, dest_lbl_dir):
    for img_name in image_list:
        base_name = os.path.splitext(img_name)[0]
        img_path = os.path.join(src_img_dir, img_name)
        lbl_path = os.path.join(src_lbl_dir, base_name + ".txt")

        # Copy image
        shutil.copy2(img_path, os.path.join(dest_img_dir, img_name))
        
        # Copy label if it exists
        if os.path.exists(lbl_path):
            shutil.copy2(lbl_path, os.path.join(dest_lbl_dir, base_name + ".txt"))
        else:
            print(f"[⚠️ Warning] Label missing for image: {img_name}")

# 🚚 Move train and val files
move_files(train_files, images_dir, labels_dir, train_images_dir, train_labels_dir)
move_files(val_files, images_dir, labels_dir, val_images_dir, val_labels_dir)

print("✅ Dataset successfully split into train and validation sets.")

import cv2
import os

# Path settings
img_dir = r"C:\Users\ABC\Desktop\classified\foreign"
output_dir = r"C:\Users\ABC\Desktop\classified\labels"
os.makedirs(output_dir, exist_ok=True)

drawing = False
ix, iy = -1, -1
boxes = []
current_img = None
preview_img = None
scale_x, scale_y = 1.0, 1.0

def resize_for_preview(img, max_size=1000):
    global scale_x, scale_y
    h, w = img.shape[:2]
    if max(h, w) > max_size:
        scale = max_size / max(h, w)
        new_w, new_h = int(w * scale), int(h * scale)
        resized = cv2.resize(img, (new_w, new_h))
        scale_x = w / new_w
        scale_y = h / new_h
        return resized
    else:
        scale_x = scale_y = 1.0
        return img

def draw_box(event, x, y, flags, param):
    global ix, iy, drawing, preview_img, boxes

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp = preview_img.copy()
            cv2.rectangle(temp, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow("Label", temp)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(preview_img, (ix, iy), (x, y), (0, 255, 0), 2)

        x1, y1 = int(ix * scale_x), int(iy * scale_y)
        x2, y2 = int(x * scale_x), int(y * scale_y)

        h, w, _ = current_img.shape
        x_center = ((x1 + x2) / 2) / w
        y_center = ((y1 + y2) / 2) / h
        bbox_width = abs(x2 - x1) / w
        bbox_height = abs(y2 - y1) / h
        boxes.append((0, x_center, y_center, bbox_width, bbox_height))

def label_images():
    global current_img, preview_img, boxes
    images = [f for f in os.listdir(img_dir) if f.lower().endswith((".jpg", ".png"))]

    for img_name in images:
        boxes = []
        path = os.path.join(img_dir, img_name)
        current_img = cv2.imread(path)
        if current_img is None:
            print(f"Could not read: {img_name}")
            continue
        preview_img = resize_for_preview(current_img.copy())

        cv2.namedWindow("Label")
        cv2.setMouseCallback("Label", draw_box)

        while True:
            cv2.imshow("Label", preview_img)
            key = cv2.waitKey(1) & 0xFF

            if key == 13:  # Enter key
                if boxes:
                    label_path = os.path.join(output_dir, img_name.rsplit('.', 1)[0] + ".txt")
                    with open(label_path, "w") as f:
                        for box in boxes:
                            f.write(f"{box[0]} {box[1]:.6f} {box[2]:.6f} {box[3]:.6f} {box[4]:.6f}\n")
                break

            elif key == 27 or key == ord('q'):  # ESC or q to quit
                cv2.destroyAllWindows()
                return

        cv2.destroyAllWindows()

label_images()

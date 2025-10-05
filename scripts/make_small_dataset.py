from PIL import Image
import os

src_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'kodak')
dst_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'kodak_small')
os.makedirs(dst_dir, exist_ok=True)

files = sorted([f for f in os.listdir(src_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
if not files:
    print('No images found in', src_dir)
    raise SystemExit(1)

src_path = os.path.join(src_dir, files[0])
img = Image.open(src_path).convert('RGB')
img_small = img.resize((128, 128), Image.BICUBIC)
dst_path = os.path.join(dst_dir, files[0])
img_small.save(dst_path)
print('Saved small image to', dst_path)

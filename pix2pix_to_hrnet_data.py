import os
import shutil

root = '/data/mtu/datasets/pix2pix_cityscapes'
gt_path = root + '/gtFine/val'
im_path = root + '/leftImg8bit/val'
lst_path = root + '/../list/pix2pix_cityscapes'

# Create directories for storing the image, label pairs and pairing list
if os.path.exists(gt_path):
    shutil.rmtree(gt_path)
if os.path.exists(im_path):
    shutil.rmtree(im_path)
if os.path.exists(lst_path):
    shutil.rmtree(lst_path)
os.mkdir(gt_path)
os.mkdir(im_path)
os.mkdir(lst_path)

# Copy files into directories created
label_dir = "/data/mtu/pytorch-CycleGAN-and-pix2pix/results/cityscapes_pix2pix/test_latest/images/"
for i in range(len(os.listdir(label_dir)) // 3):
    
    label = "{:06d}_real_A.png".format(i)
    image = "{:06d}_fake_B.png".format(i)

    # Copy image and label files
    label = shutil.copy(label_dir + label, gt_path)
    image = shutil.copy(label_dir + image, im_path)

    # Write to pairing list
    with open(lst_path + '/val.lst', 'a') as f:
        f.write("{} {}".format(image, label) + os.linesep)

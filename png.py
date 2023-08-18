# 开发时间：2023/7/29 13:06
from PIL import Image
import numpy as np
import os
import glob

img_path = glob.glob(r"S:\DOWN\result\validation\n01443537")  # 此处img是我存放jpeg图片的文件夹
print(len(img_path))
save_path = 'S:\DOWN\result\validation\n01443537'  # savepic是保存png图片的文件夹

for index in range(len(img_path)):
    img = Image.open(img_path[index])
    img_name = os.path.split(img_path[index])[1]
    img_name = os.path.splitext(img_name)[0]
    img.save(save_path + str(index + 1) + '.png')

    print(img_path[index])


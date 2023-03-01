import os
import shutil
from PIL import Image
from MODNet_entry import get_model, infer2

# 创建一个新文件夹
os.makedirs('抠图后')

# 确定模型
model = get_model('modnet_photographic_portrait_matting.ckpt')

# 获取当前文件所在目录
folder_path = os.getcwd()

# 设置裁剪后的图片大小
# new_size = (512, 512)

# 计数器，用于生成新的文件名
count = 1

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 判断文件是否为图片文件（这里以png和jpg为例）
    if filename.endswith(".png") or filename.endswith(".jpg"):
        # 抠图
        infer2(model, os.path.basename(filename), 'alpha.png', 'new.png')
        # # 裁剪图片
        # image = image.crop((0, 0, new_size[0], new_size[1]))

        # # 打开图片
        # image = Image.open(os.path.join(folder_path, 'new.png' ))
        
        # 生成新的文件名
        new_filename = f"{count:03d}.png"

        # 重命名文件
        os.rename(os.path.join(folder_path, 'new.png'), os.path.join(folder_path, new_filename))

        # 保存裁剪后的图片
        # image.save(os.path.join(folder_path, new_filename))

        # 删除生成的alpha通道图
        os.remove(os.path.join(folder_path, "alpha.png"))

        # 计数器加1
        count += 1
print('count=',count)
# 遍历每个处理后的图片，并复制到新文件夹
for i in range(1, count):
    file_name = f'{i:03d}.png'
    shutil.move(file_name, f'抠图后/{file_name}')
print('图片处理完毕！')

# infer2(model, '001.png', 'alpha.png', 'new_image-001.png')
# os.remove("alpha.png")
# # 生成新的文件名
# new_filename = f"{count:03d}.png"

# # 重命名文件
# os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
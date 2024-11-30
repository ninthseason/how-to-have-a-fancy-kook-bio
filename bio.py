from PIL import Image
from sys import argv

def process(input_path, output_path):
    img = Image.open(input_path)
    single_h = img.size[1] // 5
    if single_h * 5 != img.size[1]:
        print("警告: 图片高度无法被5整除")
    for i in range(5):
        img.crop((0, i * single_h, img.size[0], (i + 1) * single_h)).save(f"{output_path}_{i}.png")


if __name__ == "__main__":
    if len(argv) != 3:
        print("用法: python bio.py <输入图片路径> <生成图片路径>\n示例: python bio.py kookBio.png ./kookBio\nTips: 生成的图片会自动加上后缀, 上例中则是于当前目录下生成 kookBio_0.png, kookBio_1.png ...")
        exit(1)
    process(argv[1], argv[2])

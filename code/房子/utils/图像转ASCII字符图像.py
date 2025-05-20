from PIL import Image

# 将图片转换为字符图像
def 图片转字符图像(图片路径, 输出宽度=100):
    # 打开图片
    img = Image.open(图片路径)
    # 调整图片大小
    宽度, 高度 = img.size
    比例 = 高度 / 宽度 / 1.65  # 调整比例以适配字符高度
    新宽度 = 输出宽度
    新高度 = int(输出宽度 * 比例)
    img = img.resize((新宽度, 新高度))
    # 转为灰度图
    img = img.convert("L")
    # 定义字符集
    字符集 = " .:-=+*#%@"
    像素转字符 = lambda 像素值: 字符集[像素值 * len(字符集) // 256]
    # 将 img.getdata() 转换为列表
    像素数据 = list(img.getdata())
    # 构建字符图像
    字符图像 = "\n".join(
        "".join(像素转字符(像素值) for 像素值 in 像素数据[i:i + 新宽度])
        for i in range(0, len(像素数据), 新宽度)
    )
    # 字符图像 = "\n".join(
    #     "".join(像素转字符(像素值) for 像素值 in img.getdata()[i:i + 新宽度])
    #     for i in range(0, len(img.getdata()), 新宽度)
    # )
    return 字符图像
# 示例：将沙发图片转为字符图像
图片路径 = "images/沙发.png"  # 请确保图片文件存在于当前目录
try:
    字符图像 = 图片转字符图像(图片路径)
    print(字符图像)
except FileNotFoundError:
    print(f"未找到图片文件：{图片路径}")
import base64

# 要解码的 Base64 字符串
encoded_string = "Y2hlbmJvdG9tZUAxNjMuY29t" # 这是 chenbotome@163.com 的 Base64 编码
# encoded_string = "SGVsbG8gd29ybGQh"  # 这是 "Hello world!" 的 Base64 编码


# 进行 Base64 解码
decoded_bytes = base64.b64decode(encoded_string)

# 将字节转换为字符串（假设是 UTF-8 编码）
decoded_string = decoded_bytes.decode('utf-8')

print(decoded_string)

# 备注:
# base64 是一种将二进制数据转换为 ASCII 字符串的编码方式，常用于在网络上安全地传输二进制数据，如图片、文件等。
# 如果解码后是二进制数据（例如图片文件），你不一定需要调用 .decode ()，可以直接保存为文件。
# 进制转换


def dec_to_bin(n):
    """将十进制数转换为二进制字符串"""
    return bin(n)[2:]  # 去掉 '0b' 前缀


def bin_to_dec(b):
    """将二进制字符串转换为十进制数"""
    return int(b, 2)  # 使用 int 函数指定基数为 2


def three_to_dec(t):
    """将三进制字符串转换为十进制数"""
    return int(t, 3)  # 使用 int 函数指定基数为 3


def hex_add(a, b):
    """将两个十六进制字符串相加"""
    return hex(int(a, 16) + int(b, 16))[2:]  # 去掉 '0x' 前缀


if __name__ == "__main__":
    num = 42
    # print(f"{num} 的二进制是: {dec_to_bin(num)}")  # 输出: 42 的二进制是: 101010

    binary_str = "101010"
    # print(f"{binary_str} 的十进制是: {bin_to_dec(binary_str)}")  # 输出: 101010 的十进制是: 42

    three_to_dec_str = "120"
    # print(f"{three_to_dec_str} 的十进制是: {three_to_dec(three_to_dec_str)}")  # 输出: 120 的十进制是: 12

    hex_a = "1a"
    hex_b = "2f"
    # print(f"{hex_a} + {hex_b} = {hex_add(hex_a, hex_b)}")  # 输出: 1a + 2f = 49
    # 或者
    print(hex(0x1A + 0x2F))  # 输出: 49

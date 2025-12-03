
# 显示文件中，一行内容小于5个字符的行
def display_short_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if len(line.strip()) < 5:
                    print(line.strip())
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")




# 使用示例
if __name__ == "__main__":
    file_path = 'file/short_lines.txt'  # 替换为你的文件路径
    display_short_lines(file_path)
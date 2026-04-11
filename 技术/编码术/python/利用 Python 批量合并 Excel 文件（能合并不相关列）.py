import os
import pandas as pd
from pathlib import Path

# This script merges multiple Excel files from a specified directory into two separate sheets in a new Excel file.
# 这个脚本将指定目录中的多个 Excel 文件合并到一个新的 Excel 文件的两个单独工作表中。

def get_filename(file_dir):
    return [file for file in os.listdir(file_dir) if file.endswith('.xls') or file.endswith('.xlsx')]


def merge_xlsx(path, filenames, sheet_num, output_filename):
    data = []
    path_folder = Path(path)
    for filename in filenames:
        file_path = path_folder / filename
        df = pd.read_excel(file_path, sheet_name=sheet_num)
        data.append(df)
    # 自动按列名对齐合并
    content = pd.concat(data, ignore_index=True, sort=False)
    output_path = path_folder / 'output'
    output_filename_xlsx = output_filename + '.xlsx'
    if not os.path.exists(output_path):
        print("output folder not exist, create it")
        os.mkdir(output_path)
    content.to_excel((output_path / output_filename_xlsx), header=True, index=False)
    print("merge success")


if __name__ == "__main__":
    path = r'J:/me/do/file/xlsx'
    filenames = get_filename(path)
    merge_xlsx(path, filenames, 0, "sheet1")
    merge_xlsx(path, filenames, 1, "sheet2")
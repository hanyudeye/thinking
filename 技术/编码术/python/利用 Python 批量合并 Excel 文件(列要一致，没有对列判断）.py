import os
import pandas as pd
from pathlib import Path


def get_filename(file_dir):
    return [file for file in os.listdir(file_dir) if file.endswith('.xls') or file.endswith('.xlsx')]


def merge_xlsx(path, filenames, sheet_num, output_filename):
    data = []
    title = []
    path_folder = Path(path)
    for filename in filenames:
        file_path = path_folder / filename
        # 用 pandas 直接读取指定 sheet
        df = pd.read_excel(file_path, sheet_name=sheet_num)
        if not title:
            title = df.columns.tolist()
        data.append(df)
    content = pd.concat(data, ignore_index=True)
    content.columns = title
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
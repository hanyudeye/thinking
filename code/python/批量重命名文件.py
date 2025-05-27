
import os
import argparse

def batch_rename(folder_path, prefix='', suffix='', new_base_name='', start_index=1):
    files = os.listdir(folder_path)
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
    files.sort()

    for i, filename in enumerate(files, start=start_index):
        name, ext = os.path.splitext(filename)
        new_name = ''

        if new_base_name:
            new_name = f"{new_base_name}{i}{ext}"
        else:
            new_name = f"{prefix}{name}{suffix}{ext}"

        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")

def main():
    parser = argparse.ArgumentParser(description="Batch rename files in a folder.")
    parser.add_argument("folder", help="Path to the folder containing files to rename.")
    parser.add_argument("--prefix", default="", help="Prefix to add to filenames.")
    parser.add_argument("--suffix", default="", help="Suffix to add to filenames.")
    parser.add_argument("--base", default="", help="New base name (overrides original name).")
    parser.add_argument("--start", type=int, default=1, help="Start index for numbering.")

    args = parser.parse_args()

    batch_rename(
        folder_path=args.folder,
        prefix=args.prefix,
        suffix=args.suffix,
        new_base_name=args.base,
        start_index=args.start
    )

if __name__ == "__main__":
    main()

# 示例 1：加前缀和后缀
# python rename_files_cli.py "C:\Users\YourName\Desktop\test_files" --prefix="img_" --suffix="_2025"

# 示例 2：用统一名称
# python rename_files_cli.py "C:\Users\YourName\Desktop\test_files" --base="photo_" --start=10

# 示例 3：仅改后缀
# python rename_files_cli.py "C:\Users\YourName\Desktop\test_files" --suffix="_v2"

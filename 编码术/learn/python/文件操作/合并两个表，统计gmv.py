import pandas as pd


# 输入文件名
input_file = r'f:/me/do/file/input.xlsx'
output_file = r'f:/me/do/file/output.xlsx'

# 读取两个 sheet
sheet1 = pd.read_excel(input_file, sheet_name="Sheet1")
sheet2 = pd.read_excel(input_file, sheet_name="Sheet2")

# 按 id LEFT JOIN（sheet1 为主表）
# how="left" 表示左连接
merged = pd.merge(sheet1, sheet2, on="id", how="left")

# 导出到 sheet3
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    sheet1.to_excel(writer, sheet_name="Sheet1", index=False)
    sheet2.to_excel(writer, sheet_name="Sheet2", index=False)
    merged.to_excel(writer, sheet_name="Sheet3", index=False)

print("合并完成！sheet3 已生成。")


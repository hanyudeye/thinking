# 表格保留分组后某字段同名的第一行

import pandas as pd

df = pd.read_excel('表.xlsx')

# 根据 Name 列保留第一次出现的行
result = df.drop_duplicates(subset='Name', keep='first')

# 保存
result.to_excel('去重后的表.xlsx', index=False)

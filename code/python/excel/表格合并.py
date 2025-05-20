# import pandas as pd

# df1 = pd.read_excel('表1.xlsx')
# df2 = pd.read_excel('表2.xlsx')

# # 根据 ID 合并
# merged = pd.merge(df1, df2, on='商家ID', how='inner')

# # 保存
# merged.to_excel('合并后的表.xlsx', index=False)

import pandas as pd

df1 = pd.read_excel('工作簿1.xlsx')
df2 = pd.read_excel('工作簿2.xlsx')

# 只选取表2的 ID 和 Age 列
# df2_selected = df2[['ID', 'Age']]
df1_selected = df1[['商户名称', '商户ID']]
df2_selected = df2[['服务时间','商家ID']]

# 根据 ID 合并，inner 表示只保留两个表中都有的 ID，left 表示保留表1中的所有 ID
# merged = pd.merge(df1_selected, df2_selected, on='商家ID', how='left')
merged = pd.merge(df1_selected, df2_selected, left_on='商户ID',right_on='商家ID', how='left')
# 合并时指定左右的列名
# merged = pd.merge(df1, df2_selected, left_on='UserID', right_on='ID', how='inner')


# 保存
merged.to_excel('合并后的表.xlsx', index=False)
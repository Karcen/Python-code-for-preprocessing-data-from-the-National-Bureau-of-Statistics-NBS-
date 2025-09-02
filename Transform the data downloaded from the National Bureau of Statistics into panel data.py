# 将国家统计局下载的数据变为面板数据
# Transform the data downloaded from the National Bureau of Statistics into panel data.

import pandas as pd

# 假设你的Excel文件名为'merged.xlsx'
file_path = r".\Total_Pop.xlsx"

# 读取Excel文件中的所有sheet
xls = pd.ExcelFile(file_path)

# 遍历每个sheet
for sheet_name in xls.sheet_names:
    # 读取当前sheet的数据
    df = pd.read_excel(xls, sheet_name=sheet_name)
    
    # 转换为长格式
    df_long = df.melt(id_vars=['Region'], var_name='Year', value_name='Value')
    
    # 保存当前sheet的面板数据到新的Excel文件
    output_file = f'{sheet_name}_panel_data.xlsx'
    df_long.to_excel(output_file, index=False)
    
    print(f"面板数据已保存到 '{output_file}'")
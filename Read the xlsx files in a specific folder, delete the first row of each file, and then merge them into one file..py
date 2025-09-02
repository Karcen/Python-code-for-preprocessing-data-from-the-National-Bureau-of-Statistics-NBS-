# 读取特定文件夹下的xlsx文件，删除每个文件的第一行，然后合并到一个文件
# Read the xlsx files in a specific folder, delete the first row of each file, and then merge them into one file.

import os
import pandas as pd

def merge_xlsx_files(input_folder, output_file):
    """
    读取指定文件夹内的所有 .xlsx 文件，删除每个文件的第一行，然后合并到一个文件中
    每个工作表的名称使用原 Excel 文件的名称
    """
    # 创建一个 ExcelWriter 对象，用于写入最终的合并文件
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
         #历文件夹中的所有文件
        for filename in os.listdir(input_folder):
            file_path = os.path.join(input_folder, filename)
            
            # 检查文件是否是 .xlsx 文件
            if os.path.isfile(file_path) and filename.endswith('.xlsx'):
                # 读取 Excel 文件，跳过第一行
                try:
                    data = pd.read_excel(file_path, skiprows=1)
                    # 将数据写入到新的 Excel 文件中，工作表名称为原文件名（去掉扩展名）
                    sheet_name = os.path.splitext(filename)[0]
                    data.to_excel(writer, sheet_name=sheet_name, index=False)
                    print(f"处理完成: {filename}")
                except Exception as e:
                    print(f"处理失败: {filename}, 错误信息: {e}")

if __name__ == "__main__":
    input_folder = r'.\panel'
    output_file = r'.\panel_merged.xlsx'
    merge_xlsx_files(input_folder, output_file)
    print(f"所有文件已合并到: {output_file}")
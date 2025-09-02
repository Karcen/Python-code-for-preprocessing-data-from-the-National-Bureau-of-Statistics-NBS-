# 将指定文件夹内的所有 .xls 文件转换为 .xlsx 格式
# Convert all .xls files in the specified folder to .xlsx format.

import os
import pandas as pd

def convert_xls_to_xlsx(input_folder):
    """
    将指定文件夹内的所有 .xls 文件转换为 .xlsx 格式
    """
    # 遍历文件夹中的所有文件
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        
        # 检查文件是否是 .xls 文件
        if os.path.isfile(file_path) and filename.endswith('.xls'):
            # 构建输出文件路径，将 .xls 替换为 .xlsx
            output_filename = filename.replace('.xls', '.xlsx')
            output_path = os.path.join(input_folder, output_filename)
            
            # 读取 .xls 文件
            try:
                data = pd.read_excel(file_path)
                # 写入 .xlsx 文件
                data.to_excel(output_path, index=False)
                print(f"转换成功: {filename} -> {output_filename}")
            except Exception as e:
                print(f"转换失败: {filename}, 错误信息: {e}")

if __name__ == "__main__":
    input_folder = r'.\Data_revision'
    convert_xls_to_xlsx(input_folder)
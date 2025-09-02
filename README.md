# README

## 中文说明

### 项目简介

本项目旨在对 **国家统计局 (National Bureau of Statistics, NBS)** 网站下载的数据进行格式转换与预处理，以便后续进行面板数据 (panel data) 分析。主要功能包括：

1. 将指定文件夹内的所有 `.xls` 文件批量转换为 `.xlsx` 格式。
2. 读取特定文件夹下的 `.xlsx` 文件，删除每个文件的第一行，并将所有文件合并到一个总文件中。
3. 将合并后的数据转换为长格式 (long format)，形成标准的面板数据结构。

### 文件结构与功能

* **convert\_xls\_to\_xlsx.py**
  将文件夹中的 `.xls` 文件批量转换为 `.xlsx` 格式。

* **merge\_xlsx\_files.py**
  遍历文件夹内的 `.xlsx` 文件，删除第一行后，分别写入合并文件中的不同工作表。

* **transform\_to\_panel.py**
  将合并后的 `.xlsx` 文件中的各个工作表转化为长格式数据，并分别保存为新的面板数据文件。

### 使用方法

1. 修改脚本中的 `input_folder` 和 `output_file` 路径为本地路径。
2. 先运行 `convert_xls_to_xlsx.py`，将 `.xls` 文件转换为 `.xlsx` 文件。
3. 再运行 `merge_xlsx_files.py`，合并 `.xlsx` 文件。
4. 最后运行 `transform_to_panel.py`，生成面板数据文件。

### 注意事项

* 考虑到 **国家统计局英文版网站访问速度较慢**，推荐使用 **中文版网站** 下载数据。
* 中文版数据中的省份名称可以手动替换为英文。参考如下映射表：

| 中文名称 | English Name   |
| ---- | -------------- |
| 北京   | Beijing        |
| 天津   | Tianjin        |
| 河北   | Hebei          |
| 山西   | Shanxi         |
| 内蒙古  | Inner Mongolia |
| 辽宁   | Liaoning       |
| 吉林   | Jilin          |
| 黑龙江  | Heilongjiang   |
| 上海   | Shanghai       |
| 江苏   | Jiangsu        |
| 浙江   | Zhejiang       |
| 安徽   | Anhui          |
| 福建   | Fujian         |
| 江西   | Jiangxi        |
| 山东   | Shandong       |
| 河南   | Henan          |
| 湖北   | Hubei          |
| 湖南   | Hunan          |
| 广东   | Guangdong      |
| 广西   | Guangxi        |
| 海南   | Hainan         |
| 重庆   | Chongqing      |
| 四川   | Sichuan        |
| 贵州   | Guizhou        |
| 云南   | Yunnan         |
| 西藏   | Tibet          |
| 陕西   | Shaanxi        |
| 甘肃   | Gansu          |
| 青海   | Qinghai        |
| 宁夏   | Ningxia        |
| 新疆   | Xinjiang       |

---

## English Instructions

### Project Overview

This project is designed to preprocess data downloaded from the **National Bureau of Statistics (NBS)** for further panel data analysis. The pipeline includes:

1. Converting all `.xls` files in a specified folder into `.xlsx` format.
2. Reading `.xlsx` files in a specified folder, deleting the first row of each file, and merging them into one output file (each sheet corresponds to one source file).
3. Transforming merged data into **long format (panel data)** suitable for econometric or statistical analysis.

### File Structure and Functions

* **convert\_xls\_to\_xlsx.py**
  Batch convert `.xls` files into `.xlsx` format.

* **merge\_xlsx\_files.py**
  Read `.xlsx` files, remove the first row, and save them into different sheets of one merged file.

* **transform\_to\_panel.py**
  Transform each sheet of the merged file into long-format panel data, and save each as a new `.xlsx` file.

### Usage

1. Update `input_folder` and `output_file` paths in each script to match your local environment.
2. Run `convert_xls_to_xlsx.py` first to convert `.xls` to `.xlsx`.
3. Run `merge_xlsx_files.py` to merge processed `.xlsx` files.
4. Run `transform_to_panel.py` to generate panel data files.

### Notes

* Since the **English version of the NBS website is slow**, it is recommended to use the **Chinese version** instead.
* Province names in Chinese data can be manually replaced with English equivalents. A mapping table is provided above.

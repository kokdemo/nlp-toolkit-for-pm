# nlp-toolkit-for-pm
 产品经理的自然语言处理工具箱

## 准备

你需要安装以下的库：

    pip3 install jieba
    pip3 install pandas

## 人名检测

将导入的数据按照 origin.csv的格式整理好（utf-8格式），切换到这个文件夹内，输入：

    python3 detect-name.py

就会将origin中的文本切词，把里面人名挑出来。最后输出到 detect-name.csv 中。
# nlp-toolkit-for-pm
 产品经理的自然语言处理工具箱

## 准备

首先你需要python3的开发环境，如果你没有，请按照这个链接进行配置：http://www.runoob.com/python/python-install.html

然后安装pip（python的包管理器）：https://www.jianshu.com/p/eb46d00fc7ba

你需要安装以下的库：

    pip3 install jieba
    pip3 install pandas

## 人名检测

将导入的数据按照 origin.csv的格式整理好（utf-8格式），切换到这个文件夹内，输入：

    python3 detect-name.py

就会将origin中的文本切词，把里面人名挑出来。最后输出到 detect-name.csv 中。

## 分词与词性过滤

将导入的数据按照 slice-word.xlsx 的格式整理好（utf-8格式），切换到test-data文件夹内，输入：

    python3 slice-word.py

就会将 slice-word.xlsx 中的文本切词，把里面人名挑出来。最后打印出来。

如果要加上词性过滤，需要修改代码，在word_filter变量添加要过滤掉的词性。
# <p align="center">📒PureWriterBackup: 为纯纯写作设计的导出工具</p>

<p align="center">
    <a href="https://github.com/WangTingZheng/PureWriterBackup/releases/tag/v1.0.0">
        <img src="https://img.shields.io/badge/release-v1.0.0-brightgreen.svg">
    </a>
    <a href="">
        <img src="https://img.shields.io/badge/状态-随缘更新-brightgreen.svg">
    </a>
    <a href="https://github.com/python/cpython">
        <img src="https://img.shields.io/badge/Python-3.7.4-blue.svg">
    </a>
    <a href="https://github.com/WangTingZheng/PureWriterBackup">
      <img src="https://img.shields.io/github/stars/WangTingZheng/PureWriterBackup.svg?style=social">
    </a>
    
</p>

## 环境依赖：
- python3
- pip

本项目是针对纯纯写作的备份文件`.pwb`的解析api，`.pwb`是纯纯写作作者自己封装的后缀名，它实际上是一个`zip`的压缩包，通过解压缩，我们可以看到，它包含三个文件：
- MD5：校验文件完整性；
- info.db：一个带有备份信息的数据库文件，采用的是sqlite数据库，包含大部分备份信息
- Setting.xml：带有少量设置信息的文件，webdev的账号密码就保存于此

使用时，把备份文件后缀名改为`.zip`，解压后得到一个后缀名为`.zip`的数据库文件，`放入`项目的./res`里，取名`test.db`。
在`CMD` 或者 ``git`下cd到项目地址后执行：
```
python -r install requirements.txt
python main.py
```
在`./res`文件夹下就会生成一个叫`test.epub`的电子书文件
<details>
<summary><mark><font color=darkred>函数</font></mark></summary>

## 函数
### 电子书
>create_book( ):
- 功能：创建一个`.epub`电子书变量
- 形参：无
- 返回值：返回创建好的电子书变量

> add_metadata(book, metadata)
- 功能：为电子书添加元数据
- 形参：book，metadata
  - book：要添加的目标电子书
  - metadata：要添加的元数据，格式为
```python
metadata={'identifier':'123','title':'test','language':'zh-cn','author':'wtz'}
```
- 返回值：无
> add_css(book)
- 功能：为电子书添加css信息
- 形参：book
  - book：要添加的目标电子书
- 返回值：无
>add_page_to_toc(c)
- 功能：把页面添加到页面元组
- 形参：c
  - c：由`epub.EpubHtml`创建的页面
- 返回值：无

>add_page(book, text title, number)
- 功能：定义一个页面，添加到电子书和目录、spine
- 形参：book，text
  - book：要添加的目标电子书
  - text：要添加的html页面信息
  - title：文章标题
  - number：文章标号
- 返回值：无
</details>

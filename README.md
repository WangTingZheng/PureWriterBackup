# PureWriterBackup
本项目是针对纯纯写作的备份文件`.pwb`的解析api，`.pwb`是纯纯写作作者自己封装的后缀名，它实际上是一个`zip`的压缩包，通过解压缩，我们可以看到，它包含三个文件：
- MD5：未知，猜测应该与密码加密有关；
- info.db：一个带有备份信息的数据库文件，采用的是sqlite数据库，包含大部分备份信息
- Setting.xml：带有少量设置信息的文件，webdev的账号密码就保存于此

使用时，把备份文件放入`./res`里，取名`test.db`，执行：
```
python main.py
```

# 函数
## 电子书
>create_book():
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

>add_page(book, text)
- 功能：定义一个页面，添加到电子书和目录、spine
- 形参：book，text
  - book：要添加的目标电子书
  - text：要添加的页面信息，它是一个元组：
```python
txt1={'head':'this is a head','main':'this is main'}
```
- 返回值：无
> main(metadata, text, number)
- 功能：创建一个电子书
- 形参：metadata，text，number
  - metadata：元数据
  - text：一个由number个页面信息字典组成的列表
  - number：text列表里的字典/页面的个数
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

## 使用
### 提取数据库文件
> 旧版本

旧版本的纯纯写作的备份文件是一个后缀名为`.db`的文件，只是一个`sqlite`数据库文件，你可以直接准备好这个文件，不需要进行进一步的处理；

> 新版本

#### 介绍
新版本的纯纯写作封装了自己的备份文件格式，叫`.pwb`，`pwb`是`pure writer backup`的缩写，它实际上是一个压缩包
#### 提取数据库文件
- 把`.pwb`文件改成后缀名为`.zip`的文件
- 把这个压缩包解压缩
- 拿到里面一个后缀名为`.db`的文件
### 转化
- 把数据库文件放在与`main.exe`同一文件夹
- 执行`main.exe`
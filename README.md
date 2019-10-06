# cn2an: Chinese Numerals To Arabic Numerals

[![Build Status](https://travis-ci.org/HaveTwoBrush/cn2an.svg?branch=master)](https://travis-ci.org/HaveTwoBrush/cn2an)
[![Pypi](https://img.shields.io/pypi/v/cn2an.svg)](https://pypi.org/project/cn2an/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/HaveTwoBrush/cn2an/blob/master/LICENSE)
[![stars](https://img.shields.io/github/stars/HaveTwoBrush/cn2an.svg)](https://github.com/HaveTwoBrush/cn2an/stargazers)
[![API](https://img.shields.io/badge/API-reference-pink.svg)](https://github.com/HaveTwoBrush/cn2an/wiki/API)

📦 **`cn2an`** 是一个将 `中文数字` 和 `阿拉伯数字` 快速转化的工具包！

[![](https://award.dovolopor.com?lt=Ailln's&rt=idea&lbc=lightgray&rbc=red&ltc=red)](https://github.com/HaveTwoBrush/award)

[![](./src/cn2an-site.png)](https://www.dovolopor.com/cn2an)
🔗[点我访问 DEMO](https://www.dovolopor.com/cn2an)

## 1 功能

### 1.1 `中文数字` => `阿拉伯数字`

1. 支持 `中文数字` => `阿拉伯数字`；
2. 支持 `大写中文数字` => `阿拉伯数字`；
3. 支持 `中文数字和阿拉伯数字` => `阿拉伯数字`；(开发中，暂不能使用)

### 1.2 `阿拉伯数字` => `中文数字`

4. 支持 `阿拉伯数字` => `中文数字`；
5. 支持 `阿拉伯数字` => `大写中文数字`；
6. 支持 `阿拉伯数字` => `大写人民币`； 
7. 支持 `中文数字和阿拉伯数字` => `中文数字`。(开发中，暂不能使用)

## 2 安装

> ⚠️注意：仅支持 `Python 3.6+` 版本。

### 2.1 使用 pip 安装

```shell
$ pip install cn2an
```

### 2.2 从代码库安装

```shell
$ git clone https://github.com/HaveTwoBrush/cn2an.git
$ cd cn2an
$ python setup.py install
```

## 3 使用

```python
# 在文件首部引入包
import cn2an

# 查看版本
cn2an.__version__
# output: 0.3.7
```

### 3.1 `中文数字` => `阿拉伯数字`

```python
import cn2an

# 在 strict 模式下，只有严格符合的才可以进行转化
output = cn2an.cn2an("一百二十三", "strict")
# or output = cn2an.cn2an("一二三")
print(output)
# 123

# 在 normal 模式下，还可以将 一二三 进行转化
output = cn2an.cn2an("一二三", "normal")
print(output)
# 123

# 在 smart 模式下，还可以将混合描述的 1百23 进行转化 (开发中，暂不能使用)
output = cn2an.cn2an("1百23", "smart")
print(output)
# 123
```

### 3.2 `阿拉伯数字` => `中文数字`

```python
import cn2an

# 在 low 模式下，数字转化为小写的中文数字
output = cn2an.an2cn("123", "low")
# or output = cn2an.an2cn("123")
print(output)
# 一百二十三

# 在 up 模式下，数字转化为大写的中文数字
output = cn2an.an2cn("123", "up")
print(output)
# 壹佰贰拾叁

# 在 rmb 模式下，数字转化为人民币专用的描述
output = cn2an.an2cn("123", "rmb")
print(output)
# 壹佰贰拾叁元整

# 在 smart 模式下，可以将混合描述数字转化为小写的中文数字 (开发中，暂不能使用)
output = cn2an.an2cn("1百23", "smart")
print(output)
# 一百二十三
```

详细用法见 [API](https://github.com/HaveTwoBrush/cn2an/wiki/API).

## 4 版本支持

- 理论上支持 `Windows`、`MacOS`、`Ubuntu` 下的所有 `Python 3.6+` 的版本。
- 实际上仅在 `Windows 10`、`MacOS 10.14`、`Ubuntu 16.04` 的 `Python 3.6.3` 上做过完整测试。
- 欢迎提交其他版本使用情况到 [Issues](https://github.com/HaveTwoBrush/cn2an/issues) 中，期待你的反馈。
- 如果你有 `Python 2` 的使用需求，可 Fork 代码自行修改。当然也欢迎提 PR，贡献自己代码给其他人。

## 5 问题反馈

1. 先搜索 [Issues](https://github.com/HaveTwoBrush/cn2an/issues) 中有没有人已经问过类似的问题；
2. 如果没有找到解答，请新开一个 issue；
3. 在「issue 标题」中填写你遇到的问题的简介；
4. 在「issue 详情」中填写你遇到的问题的详情；
5. 最后，不要忘记注明你使用的操作系统（比如 Windows 10）和 Python 版本（比如 Python 3.6.3）。

## 6 计划事项

本项目是用看板管理开发进度，请点击 [v0.3](https://github.com/HaveTwoBrush/cn2an/projects/1) 查看开发进度和计划事项。

## 7 许可证

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)

## 8 交流

欢迎添加微信号：`kinggreenhall`，备注「cn2an」，我邀请你进入交流群。

## 9 致谢

- [Thunder Bouble](https://github.com/sfyc23): 提出很多有效的反馈，包括一些 bug 和新功能。

## 10 参考

- [如何发布自己的包到 pypi ？](https://www.v2ai.cn/python/2018/07/30/PY-1.html)
- [python 中的小陷阱](https://www.v2ai.cn/python/2019/01/01/PY-6.html)

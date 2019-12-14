# cn2an: Chinese Numerals To Arabic Numerals

[![Pypi](https://img.shields.io/pypi/v/cn2an.svg)](https://pypi.org/project/cn2an/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/Ailln/cn2an/blob/master/LICENSE)
[![stars](https://img.shields.io/github/stars/Ailln/cn2an.svg)](https://github.com/Ailln/cn2an/stargazers)
[![API](https://img.shields.io/badge/API-reference-pink.svg)](https://github.com/Ailln/cn2an/wiki/API)

📦 **`cn2an`** 是一个快速转化 `中文数字` 和 `阿拉伯数字` 的工具包！

[![](https://award.dovolopor.com?lt=Ailln's&rt=idea&lbc=lightgray&rbc=red&ltc=red)](https://github.com/Ailln/award)

[![](./src/cn2an-site.png)](https://www.dovolopor.com/cn2an)
🔗[点我访问 DEMO](https://www.dovolopor.com/cn2an)

## 1 功能

### 1.1 `中文数字` => `阿拉伯数字`

- 支持 `中文数字` => `阿拉伯数字`；
- 支持 `大写中文数字` => `阿拉伯数字`；
- 支持 `中文数字和阿拉伯数字` => `阿拉伯数字`；(开发中，暂不能使用)

### 1.2 `阿拉伯数字` => `中文数字`

- 支持 `阿拉伯数字` => `中文数字`；
- 支持 `阿拉伯数字` => `大写中文数字`；
- 支持 `阿拉伯数字` => `大写人民币`； 
- 支持 `中文数字和阿拉伯数字` => `中文数字`；(开发中，暂不能使用)

### 1.3 支持负数

- 所有转化支持 `负数`。

## 2 安装

> ⚠️注意：仅支持 `Python 3.6+` 版本。

### 2.1 使用 pip 安装

```shell
pip install cn2an
```

### 2.2 从代码库安装

```shell
git clone https://github.com/Ailln/cn2an.git
cd cn2an
python setup.py install
```

## 3 使用

```python
# 在文件首部引入包
import cn2an

# 查看版本
print(cn2an.__version__)
# 0.3.10
```

### 3.1 `中文数字` => `阿拉伯数字`

> 最大支持到`万亿兆`，即`10**32`。

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

# 全模式支持负数
output = cn2an.cn2an("负一百二十三")
print(output)
# -123
```

### 3.2 `阿拉伯数字` => `中文数字`

> 最大支持到`10**32`，即`万亿兆`。

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

# 全模式支持负数
output = cn2an.cn2an("-123")
print(output)
# 负一百二十三
```

详细用法见 [API](https://github.com/Ailln/cn2an/wiki/API).

## 4 版本支持

- 理论上支持 `Windows`、`MacOS`、`Ubuntu` 下的所有 `Python 3.6+` 的版本。
- 实际上仅在 `Windows 10`、`MacOS 10.14`、`Ubuntu 16.04` 的 `Python 3.6.9` 和 `Python3.7.4` 上做过完整测试。
- 欢迎提交其他版本使用情况到 [Issues](https://github.com/Ailln/cn2an/issues) 中，期待你的反馈。
- 如果你有 `Python 2` 的使用需求，可 Fork 代码自行修改。当然也欢迎提 PR，贡献自己代码给其他人。

## 5 问题反馈

1. 先搜索 [Issues](https://github.com/Ailln/cn2an/issues) 中有没有人已经问过类似的问题；
2. 如果没有找到解答，请新开一个 issue：
    1. 首先，在「issue 标题」中填写你遇到的问题的简介；
    2. 然后，在「issue 详情」中填写你遇到的问题的详情；
    3. 最后，不要忘记注明你使用的操作系统（比如 Windows 10）和 Python 版本（比如 Python 3.6.3）。
3. 还可以参考 [issue 模版](https://github.com/Ailln/cn2an/tree/master/.github/ISSUE_TEMPLATE)。

## 6 开发相关

### 6.1 开发进度

本项目是用看板管理开发进度，请点击 [v0.3](https://github.com/Ailln/cn2an/projects/1) 查看开发进度和计划事项。

### 6.2 代码测试

本地测试使用 [Anaconda](https://www.anaconda.com/) 的虚拟环境，测试方法如下。

```bash
# 安装 conda 环境
conda create -n py369 python=3.6.9
conda create -n py374 python=3.7.4

# 执行测试
bash local_test.sh
```

线上测试使用 [GitHub Actions](https://github.com/Ailln/cn2an/actions)。

### 6.3 性能测试

- 测试设备：`2.3 GHz 双核Intel Core i5 MacBook Pro`
- 测试代码：[performance_test.py](https://github.com/Ailln/cn2an/tree/master/cn2an/performance_test.py)
- 测试方法：

    ```bash
    pip install -r requirements_test.txt

    python -m cn2an.performance_test
    ```

- 测试结果：
    | 序号 | 功能 | 执行次数 | 执行时间(平均) | 性能(次/秒)
    | :-: | :-: | :-: | :-: | :-: |
    |  1  | an2cn | 10000 | 0.23 | **43k** |
    |  2  | cn2an | 10000 | 0.56 | **18k** |

 在测试时，我使用的测试数据是最大数据，因此大多数情况下性能要比这个要好。

## 7 许可证

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)

## 8 交流

欢迎添加微信号：`kinggreenhall`，备注「cn2an」，我邀请你进入交流群。

## 9 致谢

- [Thunder Bouble](https://github.com/sfyc23): 提出很多有效的反馈，包括一些 bug 和新功能。

## 10 参考

- [如何发布自己的包到 pypi](https://www.v2ai.cn/python/2018/07/30/PY-1.html)
- [Python 中的小陷阱](https://www.v2ai.cn/python/2019/01/01/PY-6.html)
- [汉字数字转阿拉伯数字](https://www.zouyesheng.com/han-number-convert.html)

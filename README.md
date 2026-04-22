# cn2an: Chinese Numerals To Arabic Numerals

[![Pypi](https://img.shields.io/pypi/v/cn2an.svg)](https://pypi.org/project/cn2an/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/Ailln/cn2an/blob/master/LICENSE)
[![stars](https://img.shields.io/github/stars/Ailln/cn2an.svg)](https://github.com/Ailln/cn2an/stargazers)
[![build](https://img.shields.io/github/actions/workflow/status/Ailln/cn2an/build.yml)](https://github.com/Ailln/cn2an/actions/workflows/build.yml)
[![API](https://img.shields.io/badge/API-reference-pink.svg)](https://github.com/Ailln/cn2an/wiki/API)
[![download month](https://img.shields.io/pypi/dm/cn2an)](https://pypistats.org/packages/cn2an)

📦 **`cn2an`** 是一个快速转化 `中文数字` 和 `阿拉伯数字` 的工具包！

> 🎈 `v0.5.24 update`: fix numeral parsing and transform edge cases
> 
> 🎈 [`en2an`](https://github.com/Ailln/en2an): 「英文数字」和「阿拉伯数字」互转正在收集需求中！ [详情](https://github.com/Ailln/en2an)
>
> 🎈 [`Cn2An.jl`](https://github.com/Ailln/Cn2An.jl): Julia 语言版本已经上线，正在丰富基础功能。[详情](https://github.com/Ailln/Cn2An.jl)

## 1 功能

### 1.1 `中文数字` => `阿拉伯数字`

- 支持 `中文数字` => `阿拉伯数字`；
- 支持 `大写中文数字` => `阿拉伯数字`；
- 支持 `中文数字和阿拉伯数字` => `阿拉伯数字`；
- 支持 `中文数字` => `阿拉伯数字字符串` 的原样直译；

### 1.2 `阿拉伯数字` => `中文数字`

- 支持 `阿拉伯数字` => `中文数字`；
- 支持 `阿拉伯数字` => `大写中文数字`；
- 支持 `阿拉伯数字` => `大写人民币`；
- 支持 `阿拉伯数字字符串` => `中文数字` 的原样直译；

### 1.3 句子转化

- 支持 `中文数字` => `阿拉伯数字`；
  - 支持 `日期`；
  - 支持 `分数`；
  - 支持 `百分比`；
  - 支持 `摄氏度`；

- 支持 `阿拉伯数字` => `中文数字`；
  - 支持 `日期`；
  - 支持 `分数`；
  - 支持 `百分比`；
  - 支持 `摄氏度`；

### 1.4 其他

- 支持 `小数`；
- 支持 `负数`；
- 支持 `HTTP API`。

## 2 安装

> ⚠️ 注意：
> 
> 1. 本地安装仅支持 Python 的 3.7 以上版本；
> 2. 尽可能使用 `cn2an` 的最新版本。

### 2.1 使用 pip 安装

```shell
pip install cn2an -U
```

### 2.2 从代码库安装

```shell
git clone https://github.com/Ailln/cn2an.git
cd cn2an && python setup.py install
```

## 3 使用

```python
# 在文件首部引入包
import cn2an

# 查看当前版本号
print(cn2an.__version__)
# 0.5.24
```

### 3.1 `中文数字` => `阿拉伯数字`

> 最大支持到 `10**16`，即 `千万亿`，最小支持到 `10**-16`。

```python
import cn2an

# 在 strict 模式（默认）下，只有严格符合数字拼写的才可以进行转化
output = cn2an.cn2an("一百二十三")
# 或者
output = cn2an.cn2an("一百二十三", "strict")
# output:
# 123

# 在 normal 模式下，可以将 一二三 进行转化
output = cn2an.cn2an("一二三", "normal")
# output:
# 123

# 在 smart 模式下，可以将混合拼写的 1百23 进行转化
output = cn2an.cn2an("1百23", "smart")
# output:
# 123

# 以上三种模式均支持负数
output = cn2an.cn2an("负一百二十三", "strict")
# output:
# -123

# 以上三种模式均支持小数
output = cn2an.cn2an("一点二三", "strict")
# output:
# 1.23

# 在 direct 模式下，只做逐位原样转化，并返回字符串
output = cn2an.cn2an("零零三", "direct")
# output:
# 003

output = cn2an.cn2an("一二点三零", "direct")
# output:
# 12.30
```

### 3.2 `阿拉伯数字` => `中文数字`

> 最大支持到`10**16`，即`千万亿`，最小支持到 `10**-16`。

```python
import cn2an

# 在 low 模式（默认）下，数字转化为小写的中文数字
output = cn2an.an2cn("123")
# 或者
output = cn2an.an2cn("123", "low")
# output:
# 一百二十三

# 在 up 模式下，数字转化为大写的中文数字
output = cn2an.an2cn("123", "up")
# output:
# 壹佰贰拾叁

# 在 rmb 模式下，数字转化为人民币专用的描述
output = cn2an.an2cn("123", "rmb")
# output:
# 壹佰贰拾叁元整

# 以上三种模式均支持负数
output = cn2an.an2cn("-123", "low")
# output:
# 负一百二十三

# 以上三种模式均支持小数
output = cn2an.an2cn("1.23", "low")
# output:
# 一点二三

# 在 direct 模式下，只做逐位原样转化
output = cn2an.an2cn("012", "direct")
# output:
# 零一二

output = cn2an.an2cn("12.30", "direct")
# output:
# 一二点三零
```

### 3.3 句子转化

> ⚠️：试验性功能，可能会造成不符合期望的转化。

```python
import cn2an

# 在 cn2an 方法（默认）下，可以将句子中的中文数字转成阿拉伯数字
output = cn2an.transform("小王捡了一百块钱")
# 或者
output = cn2an.transform("小王捡了一百块钱", "cn2an")
# output:
# 小王捡了100块钱

# 在 an2cn 方法下，可以将句子中的中文数字转成阿拉伯数字
output = cn2an.transform("小王捡了100块钱", "an2cn")
# output:
# 小王捡了一百块钱

# direct=True 时，句子中的数字只做逐位原样转化，不做日期、范围等额外处理
output = cn2an.transform("电话零零三，二〇〇二年", "cn2an", direct=True)
# output:
# 电话003，2002年

output = cn2an.transform("电话012，1-2个月", "an2cn", direct=True)
# output:
# 电话零一二，一-二个月


## 支持日期
output = cn2an.transform("小王的生日是二零零一年三月四日", "cn2an")
# output:
# 小王的生日是2001年3月4日

output = cn2an.transform("小王的生日是2001年3月4日", "an2cn")
# output:
# 小王的生日是二零零一年三月四日


## 支持分数
output = cn2an.transform("抛出去的硬币为正面的概率是二分之一", "cn2an")
# output:
# 抛出去的硬币为正面的概率是1/2

output = cn2an.transform("抛出去的硬币为正面的概率是1/2", "an2cn")
# output:
# 抛出去的硬币为正面的概率是二分之一

## 支持百分比
## 支持摄氏度
```

### 3.4 HTTP API

主要为其他语言（Java、Javascript、Go等）用户提供方便，当然 Python 用户也可以使用，点击查看[详细用法](https://github.com/Ailln/cn2an/wiki/API#http-api)。

## 4 版本支持

- 理论上支持 `Windows`、`MacOS`、`Ubuntu` 下的所有 `Python 3.7+` 的版本。
- 实际上仅在 `ubuntu-latest`、`windows-latest`、`macOS-latest` 的 `Python 3.7, 3.9, 3.11` 上做过完整测试。
- 欢迎提交其他版本使用情况到 [Issues](https://github.com/Ailln/cn2an/issues) 中，期待你的反馈。
- 如果你有 `Python 2` 的使用需求，可 Fork 代码自行修改。当然也欢迎提 PR，贡献自己代码给其他人。

## 5 问题反馈

1. 先搜索 [Issues](https://github.com/Ailln/cn2an/issues) 中有没有人已经问过类似的问题；
2. 如果没有找到解答，请新开一个 issue：
    1. 首先，在「issue 标题」中填写你遇到的问题的简介；
    2. 然后，在「issue 详情」中填写你遇到的问题的详情；
    3. 最后，不要忘记注明你使用的操作系统（比如 Windows 10）和 Python 版本（比如 Python 3.7.9）。
3. 还可以参考 [Issue Template](https://github.com/Ailln/cn2an/tree/master/.github/ISSUE_TEMPLATE) 。

## 6 开发相关

### 6.1 开发进度

本项目是用看板管理开发进度，请点击 [v0.5](https://github.com/Ailln/cn2an/projects/4) 查看开发进度和计划事项。

### 6.2 代码测试

本地测试使用 [Anaconda](https://www.anaconda.com/) 的虚拟环境，测试方法如下：

```bash
# 执行测试
bash scripts/local_test.sh
```

线上测试使用 [GitHub Actions](https://github.com/Ailln/cn2an/actions) 。

### 6.3 性能测试

- 测试版本：`v0.5.1`
- 测试设备：`2.3 GHz 双核Intel Core i5 MacBook Pro`
- 测试代码：[performance.py](https://github.com/Ailln/cn2an/tree/master/cn2an/performance.py)
- 测试方法：

    ```bash
    pip install -r requirements_test.txt

    python -m cn2an.performance
    ```

- 测试结果：

    | 序号 |  功能   | 执行次数  | 执行时间(万次平均) | 性能(次/秒) |
    |:--:|:-----:|:-----:|:----------:|:-------:|
    | 1  | an2cn | 10000 |    0.15    | **67k** |
    | 2  | cn2an | 10000 |    0.35    | **29k** |

测试时，我使用的是最大长度的测试数据！因此，大多数情况下该库的性能会更好～

## 7 许可证

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)
[![](https://award.dovolopor.com?lt=Ailln's&rt=idea&lbc=lightgray&rbc=red&ltc=red)](https://github.com/Ailln/award)

## 8 致谢

- [Thunder Bouble](https://github.com/sfyc23): 提出很多有效的反馈，包括一些 bug 和新功能；
- [Damon Yu](https://github.com/20071313): 增加对全角数字和全角符号的支持；
- [Beants](https://github.com/Beants): 修复了口语格式的 bug；
- Ray: 提出修改输出 warn 的方法，以及其他一些建议。

## 9 参考

- [🎈 cn2an 核心代码解析](https://www.v2ai.cn/2020/06/30/python/8-cn2an/)
- [如何发布自己的包到 pypi](https://www.v2ai.cn/2018/07/30/python/1-pypi/)
- [Python 中的小陷阱](https://www.v2ai.cn/2019/01/01/python/4-python-trap/)
- [汉字数字转阿拉伯数字](https://www.zouyesheng.com/han-number-convert.html)
- [Chinese Text Normalization for Speech Processing](https://github.com/speechio/chinese_text_normalization)
- [The Best Tool of Chinese Number to Digits](https://github.com/Wall-ee/chinese2digits)
- [Microsoft Recognizers Text Overview](https://github.com/microsoft/Recognizers-Text)
- [process: 数据预处理管道](https://github.com/Ailln/proces)
- [wikipedia: 中文数字](https://zh.wikipedia.org/zh-sg/%E4%B8%AD%E6%96%87%E6%95%B0%E5%AD%97)

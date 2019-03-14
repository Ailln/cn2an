# 📦 cn2an: Chinese Numerals To Arabic Numerals.

`cn2an` 是一个将「中文数字」和「阿拉伯数字」互相转化的工具包。

> **🚨更新日志：**
>
>   1. 添加「问题反馈」指南；
>   2. 下个版本引入 win 下的测试。

## 1. 功能

1. 「中文数字」转「阿拉伯数字」；
2. 「阿拉伯数字」转「中文数字」；
3. 「阿拉伯数字」转「大写中文数字」；
4. 支持命令行调用。

## 2. 版本支持

- 理论上支持 `python 2.7` 和 `python 3.6` 的所有版本。
- 实际上仅在 `python 2.7.10` 和 `python 3.6.3` 上做过完整测试。
- 欢迎提交其他版本使用情况到 [Issues](https://github.com/HaveTwoBrush/cn2an/issues)。

## 3. 安装

### 3.1 使用 pip 安装

```shell
pip install cn2an
```

### 3.2 从代码库安装

```shell
git clone https://github.com/HaveTwoBrush/cn2an.git
cd cn2an
python setup.py install
```

## 4. 使用

### 4.1 在代码中调用

```python
# 在文件首部引入包
import cn2an

# 查看版本
cn2an.__version__
# output: 0.1.0
```

#### 1 中文数字转阿拉伯数字

```python
cn2an.cn2an("一百万零五十四")
# output: 1000054

# 支持大写中文数字
cn2an.cn2an("壹佰万零伍十肆")
# output: 1000054
```

#### 2 阿拉伯数字转中文数字

```python
# 支持数字和字符串两种不同类型的输入
cn2an.an2cn("21024124")
cn2an.an2cn(21024124)
# output: 二千一百零二万四千一百二十四

# 支持小数
cn2an.an2cn("0.414")
cn2an.an2cn(0.414)
# output: 零点四一四

# 支持大写，需要增加额外的参数 True
cn2an.an2cn("21024124", True)
cn2an.an2cn(21024124, True)
# output: 贰仟壹佰零贰万肆仟壹佰贰拾肆

cn2an.an2cn("0.414", True)
cn2an.an2cn(0.414, True)
# output: 零点肆壹肆
```

### 4.2 在命令行中使用

#### 1 中文数字转阿拉伯数字

```bash
cn2an 一百万零五十四
# output: 1000054

# 支持小数
cn2an 零点四一四
# output: 0.414

# 支持大写
cn2an 壹佰万零伍拾肆
# output: 1000054
```

#### 2 阿拉伯数字转中文数字

```bash
an2cn 21024124
# output: 二千一百零二万四千一百二十四

# 支持小数
an2cn 0.414
# output: 零点四一四

# 支持大写，这里需要增加额外的参数 cap
cn2an 1000054 cap
# output: 壹佰万零伍十肆
an2cn 0.414 cap
# output: 零点肆壹肆
```

## 5 TODO

- [x] 阿拉伯数字转大写中文数字；
- [x] 关于零的bug；
- [x] 支持 幺 == 1 的转化；
- [ ] 自动化单元测试。

## 6 Version

- `v0.0.7` 修复 一千五百万零三百零一 等类似格式无法正确转化的问题。
- `v0.1.0` 重构代码，兼容 python 2.7。

## 7 问题反馈

1. 先搜索 [Issues](https://github.com/HaveTwoBrush/cn2an/issues) 中有没有人已经问过类似的问题；
2. 如果没有找到解答，请新开一个 issue；
3. 在「issue 标题」中填写你遇到的问题的简介；
4. 在「issue 详情」中填写你遇到的问题的详情；
5. 最后，不要忘记注明你使用的操作系统（比如 win10）和 python 版本（比如 python 3.6.3）。

## 8 License

[MIT License](https://github.com/HaveTwoBrush/cn2an/blob/master/LICENSE)
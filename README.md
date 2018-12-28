# cn2an

cn2an = Chinese Numerals To Arabic Numerals.

本模块的作用是「中文数字」和「阿拉伯数字」互相转化。

## 安装

1 使用 pip 安装：

```shell
pip install cn2an
```

2 从代码库安装：

```shell
git clone https://github.com/kinggreenhall/cn2an.git
cd cn2an
python setup.py install
```

## 使用

1 在代码中直接调用：

```python
import cn2an

# 1 中文数字转阿拉伯数字

cn2an.cn2an("一百万零五十四")
# output: 1000054

# 支持大写
cn2an.cn2an("壹佰万零伍十肆")
# output: 1000054

# 2 阿拉伯数字转中文数字

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

2 通过命令行使用：

```bash
# 1 中文数字转阿拉伯数字

cn2an 一百万零五十四
# output: 1000054

# 支持小数
cn2an 零点四一四
# output: 0.414

# 支持大写
cn2an 壹佰万零伍十肆
# output: 1000054

# 2 阿拉伯数字转中文数字

an2cn 21024124
# output: 二千一百零二万四千一百二十四

# 支持小数
an2cn 0.414
# output: 零点四一四

# 支持大写，这里需要增加额外的参数 cap
cn2an cap 1000054
# output: 壹佰万零伍十肆
an2cn cap 0.414
# output: 零点肆壹肆
```

## TODO

- [x] 阿拉伯数字转大写中文数字。
- [x] 关于零的bug。
- [x] 支持 幺 == 1 的转化。
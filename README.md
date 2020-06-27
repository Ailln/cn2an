# cn2an: Chinese Numerals To Arabic Numerals

[![Pypi](https://img.shields.io/pypi/v/cn2an.svg)](https://pypi.org/project/cn2an/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/Ailln/cn2an/blob/master/LICENSE)
[![stars](https://img.shields.io/github/stars/Ailln/cn2an.svg)](https://github.com/Ailln/cn2an/stargazers)
[![build](https://img.shields.io/github/workflow/status/Ailln/cn2an/build)](https://github.com/Ailln/cn2an/actions?query=workflow%3Abuild)
[![API](https://img.shields.io/badge/API-reference-pink.svg)](https://github.com/Ailln/cn2an/wiki/API)

📦 **`cn2an`** 是一个快速转化 `中文数字` 和 `阿拉伯数字` 的工具包！

[![](https://ailln.oss-cn-hangzhou.aliyuncs.com/github/cn2an/cn2an-site-v0.4.2.png)](https://www.dovolopor.com/cn2an)

🔗[点我访问 DEMO](https://www.dovolopor.com/cn2an)

> 🎈 [`en2an`](https://github.com/Ailln/en2an): 「英文数字」和「阿拉伯数字」互转正在收集需求中！ [详情](https://github.com/Ailln/en2an)

## 1 功能

### 1.1 `中文数字` => `阿拉伯数字`

- 支持 `中文数字` => `阿拉伯数字`；
- 支持 `大写中文数字` => `阿拉伯数字`；
- 支持 `中文数字和阿拉伯数字` => `阿拉伯数字`；

### 1.2 `阿拉伯数字` => `中文数字`

- 支持 `阿拉伯数字` => `中文数字`；
- 支持 `阿拉伯数字` => `大写中文数字`；
- 支持 `阿拉伯数字` => `大写人民币`；

### 1.3 句子转化（试验性功能）

- 支持 `中文数字` => `阿拉伯数字`；
- 支持 `阿拉伯数字` => `中文数字`；

### 1.4 其他

- 支持`小数`；
- 支持`负数`；
- 支持`http api`。

## 2 安装

> ⚠️注意：
> 1. 本地安装仅支持 Python 的 3.6 以上版本；
> 2. 其他语言用户可以考虑使用 [http api](https://www.dovolopor.com/api/cn2an) ；
> 3. 请尽可能使用 cn2an 的最新版本。

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

# 查看版本
print(cn2an.__version__)
# 0.4.3
```

### 3.1 `中文数字` => `阿拉伯数字`

> 最大支持到`10**16`，即`千万亿`，最小支持到 `10**-16`。

```python
import cn2an

# 在 strict 模式（默认）下，只有严格符合数字拼写的才可以进行转化
output = cn2an.cn2an("一百二十三")
# 或者
output = cn2an.cn2an("一百二十三", "strict")
# output:
# 123

# 在 normal 模式下，还可以将 一二三 进行转化
output = cn2an.cn2an("一二三", "normal")
# output:
# 123

# 在 smart 模式下，还可以将混合拼写的 1百23 进行转化
output = cn2an.cn2an("1百23", "smart")
# output:
# 123

# 以上三种模式均支持负数
output = cn2an.cn2an("负一百二十三")
# output:
# -123

# strict 和 normal 模式支持小数，smart 模式暂不支持
output = cn2an.cn2an("一点二三")
# output:
# 1.23
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
output = cn2an.an2cn("-123")
# output:
# 负一百二十三

# 以上三种模式均支持小数
output = cn2an.an2cn("1.23")
# output:
# 一点二三
```

### 3.3 句子转化（试验性功能）

```python
import cn2an

output = cn2an.transform("我捡了一百块钱")
# 或者
output = cn2an.transform("我捡了一百块钱", "cn2an")
# output:
# 我捡了100块钱

output = cn2an.transform("我捡了100块钱", "an2cn")
# output:
# 我捡了一百块钱
```

详细用法见 [API](https://github.com/Ailln/cn2an/wiki/API).

### 3.4 HTTP API

主要为其他语言用户提供方便，当然 Python 用户也可以使用。

#### Python

```python
import requests

response = requests.get("https://api.dovolopor.com/v1/cn2an",
  params={
    "text": "1234567890",
    "function": "an2cn",
    "method": "low"
  }
)
print(response.json())
# { output: "一百二十三", msg: "转化成功" }
```

#### Javascript

```javascript
const axios = require("axios")

axios.get("https://api.dovolopor.com/v1/cn2an", {
  params: {
    text: "123",
    function: "an2cn",
    method: "low"
  }
}).then(
  function (res) {
    console.log(res.data);
  }
)
// { output: "一百二十三", msg: "转化成功" }
```

#### Go

```go
package main

import (
    "fmt"
    "io/ioutil"
    "net/http"
    "net/url"
)

func main(){
    params := url.Values{}
    Url, err := url.Parse("https://api.dovolopor.com/v1/cn2an")
    if err != nil {
        return
    }
    params.Set("text", "123")
    params.Set("function", "an2cn")
    params.Set("method", "low")

    Url.RawQuery = params.Encode()
    urlPath := Url.String()
    resp,err := http.Get(urlPath)
    defer resp.Body.Close()
    body, _ := ioutil.ReadAll(resp.Body)
    fmt.Println(string(body))
}
// { output: "一百二十三", msg: "转化成功" }
```

## 4 版本支持

- 理论上支持 `Windows`、`MacOS`、`Ubuntu` 下的所有 `Python 3.6+` 的版本。
- 实际上仅在 `ubuntu-latest`、`windows-latest`、`macOS-latest` 的 `Python 3.6, 3.7, 3.8` 上做过完整测试。
- 欢迎提交其他版本使用情况到 [Issues](https://github.com/Ailln/cn2an/issues) 中，期待你的反馈。
- 如果你有 `Python 2` 的使用需求，可 Fork 代码自行修改。当然也欢迎提 PR，贡献自己代码给其他人。

## 5 问题反馈

1. 先搜索 [Issues](https://github.com/Ailln/cn2an/issues) 中有没有人已经问过类似的问题；
2. 如果没有找到解答，请新开一个 issue：
    1. 首先，在「issue 标题」中填写你遇到的问题的简介；
    2. 然后，在「issue 详情」中填写你遇到的问题的详情；
    3. 最后，不要忘记注明你使用的操作系统（比如 Windows 10）和 Python 版本（比如 Python 3.6.3）。
3. 还可以参考 [Issue Template](https://github.com/Ailln/cn2an/tree/master/.github/ISSUE_TEMPLATE) 。

## 6 开发相关

### 6.1 开发进度

本项目是用看板管理开发进度，请点击 [v0.4](https://github.com/Ailln/cn2an/projects/2) 查看开发进度和计划事项。

### 6.2 代码测试

本地测试使用 [Anaconda](https://www.anaconda.com/) 的虚拟环境，测试方法如下。

```bash
# 执行测试
bash scripts/local_test.sh
```

线上测试使用 [GitHub Actions](https://github.com/Ailln/cn2an/actions) 。

### 6.3 性能测试

- 测试版本：`v0.3.10`
- 测试设备：`2.3 GHz 双核Intel Core i5 MacBook Pro`
- 测试代码：[performance.py](https://github.com/Ailln/cn2an/tree/master/cn2an/performance.py)
- 测试方法：

    ```bash
    pip install -r requirements_test.txt

    python -m cn2an.performance
    ```

- 测试结果：

    | 序号 | 功能 | 执行次数 | 执行时间(平均) | 性能(次/秒)
    | :-: | :-: | :-: | :-: | :-: |
    |  1  | an2cn | 10000 | 0.23 | **43k** |
    |  2  | cn2an | 10000 | 0.56 | **18k** |

测试时，我使用的是最大长度的测试数据！因此，大多数情况下该库的性能会更好～

## 7 许可证

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)
[![](https://award.dovolopor.com?lt=Ailln's&rt=idea&lbc=lightgray&rbc=red&ltc=red)](https://github.com/Ailln/award)

## 8 交流

欢迎添加微信号：`Ailln_`，备注「cn2an」，我邀请你进入交流群。

## 9 致谢

- [Thunder Bouble](https://github.com/sfyc23): 提出很多有效的反馈，包括一些 bug 和新功能；
- [Damon Yu](https://github.com/20071313): 增加对全角数字和全角符号的支持。

## 10 参考

- [如何发布自己的包到 pypi](https://www.v2ai.cn/2018/07/30/python/1-pypi/)
- [Python 中的小陷阱](https://www.v2ai.cn/2019/01/01/python/4-python-trap/)
- [汉字数字转阿拉伯数字](https://www.zouyesheng.com/han-number-convert.html)

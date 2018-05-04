# encoding: utf-8
import sys

D_NUMERAL_UNIT = {
    u"零": 0,
    u"一": 1, u"壹": 1,
    u"二": 2, u"贰": 2, u"两": 2,
    u"三": 3, u"叁": 3,
    u"四": 4, u"肆": 4,
    u"五": 5, u"伍": 5,
    u"六": 6, u"陆": 6,
    u"七": 7, u"柒": 7,
    u"八": 8, u"捌": 8,
    u"九": 9, u"玖": 9,
    u"十": 10, u"拾": 10,
    u"百": 100, u"佰": 100,
    u"千": 1000, u"仟": 1000,
    u"万": 10000,
    u"亿": 100000000,
}

L_NUMERAL = [
    u"零",
    u"一",
    u"二",
    u"三",
    u"四",
    u"五",
    u"六",
    u"七",
    u"八",
    u"九"
]

L_UNIT = [
    u"",
    u"十",
    u"百",
    u"千",
    u"万",
    u"十",
    u"百",
    u"千",
    u"亿",
    u"十",
    u"百",
    u"千",
    u"万",
    u"十",
    u"百",
    u"千"
]


def int_cn2an(data):
    output_an = 0
    unit_value = 1
    len_input_cn = len(data)
    for index in range(len_input_cn - 1, -1, -1):
        unit_key = D_NUMERAL_UNIT.get(data[index])
        if unit_key < 10:
            output_an += unit_value * unit_key
        else:
            if unit_key > unit_value:
                unit_value = unit_key
                if index == 0:
                    output_an += unit_value
            else:
                unit_value *= unit_key
    return output_an


def float_cn2an(data):
    output_an = 0
    len_input_cn = len(data)
    for index in range(len_input_cn - 1, -1, -1):
        unit_key = D_NUMERAL_UNIT.get(data[index])
        output_an += unit_key * 10 ** -(index + 1)
    return output_an


# 将中文数字转化成阿拉伯数字
def cn2an(input_cn=u"零零零"):
    # 支持命令行使用
    len_argv = len(sys.argv)
    if len_argv == 1:
        if input_cn == u"零零零":
            raise Exception(u"请在cn2an()中输入需要转化的中文数字！")
        else:
            pass
    elif len_argv == 2:
        input_cn = sys.argv[1]
    else:
        if sys.argv[0][-5:] == u"cn2an":
            raise Exception(u"参数过多！")
        else:
            pass
    
    # 判断输入数据是否合理
    for input_key in input_cn:
        l_all_keys = list(D_NUMERAL_UNIT.keys())
        l_all_keys.append(u"点")
        if input_key not in l_all_keys:
            raise Exception(u"错误的数据输入: {}".format(input_key))

    split_input_cn = input_cn.split(u"点")
    len_split_input_cn = len(split_input_cn)
    
    if len_split_input_cn == 1:
        int_input_cn = split_input_cn[0]
        output_data = int_cn2an(int_input_cn)
    elif len_split_input_cn == 2:
        int_input_cn = split_input_cn[0]
        output_data_int = int_cn2an(int_input_cn)
        float_input_cn = split_input_cn[1]
        output_data_float = float_cn2an(float_input_cn)
        output_data = output_data_int + output_data_float
    else:
        raise Exception(u"错误，请检查输入数据格式。")
    
    if len_argv == 1:
        if input_cn == u"零零零":
            print(u"请在输入需要转化的中文数字！")
        else:
            return output_data
    elif len_argv == 2:
        print(output_data)
    else:
        if sys.argv[0][-5:] == u"cn2an":
            pass
        else:
            return output_data


def int_an2cn(data):
    output_an = u""
    len_input_cn = len(data)

    for i, d in enumerate(data):
        if int(d):
            output_an += L_NUMERAL[int(d)] + L_UNIT[len_input_cn - i - 1]
        else:
            if i > 0 and not output_an[-1] == u"零":
                if not (len_input_cn - i - 1) % 4:
                    output_an += L_NUMERAL[int(d)] + L_UNIT[len_input_cn - i - 1]
                else:
                    output_an += L_NUMERAL[int(d)]

    output_an = output_an.replace(u"零万", u"万").replace(u"零亿", u"亿").strip(u"零")

    # 解决 一十 问题
    if output_an[:2] == "一十":
        output_an = output_an[1:]
        
    # 0 - 1 之间的小数
    if not output_an:
        output_an = u"零"
        
    return output_an


def float_an2cn(data):
    output_an = u"点"
    for d in data:
        output_an += L_NUMERAL[int(d)]
    return output_an


# 将阿拉伯数字转化成中文数字
def an2cn(input_an=u"000"):
    # 支持命令行使用
    len_argv = len(sys.argv)
    if len_argv == 1:
        if input_an == u"000":
            raise Exception(u"请在an2cn()中输入需要转化的阿拉伯数字！")
        else:
            pass
    elif len_argv == 2:
        input_an = sys.argv[1]
    else:
        # ipython 问题处理
        if sys.argv[0][-5:] == u"an2cn":
            raise Exception(u"参数过多！")
        else:
            pass

    # 判断输入数据是否合理
    for input_key in str(input_an):
        l_all_keys = [u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"."]
        if input_key not in l_all_keys:
            raise Exception(u"错误的数据输入: {}".format(input_key))

    input_an = str(input_an)
    split_input_an = input_an.split(u".")
    len_split_input_an = len(split_input_an)
    
    if len_split_input_an == 1:
        int_input_an = split_input_an[0]
        output_data = int_an2cn(int_input_an)
    elif len_split_input_an == 2:
        int_input_an = split_input_an[0]
        output_data_int = int_an2cn(int_input_an)
        float_input_an = split_input_an[1]
        output_data_float = float_an2cn(float_input_an)
        output_data = output_data_int + output_data_float
    else:
        raise Exception(u"错误，请检查数据格式。")
    
    if len_argv == 1:
        if input_an == u"000":
            print(u"请在输入需要转化的阿拉伯数字！")
        else:
            return output_data
    elif len_argv == 2:
        print(output_data)
    else:
        # ipython 问题处理
        if sys.argv[0][-5:] == u"an2cn":
            pass
        else:
            return output_data

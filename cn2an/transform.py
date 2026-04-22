import re
from warnings import warn

from .cn2an import Cn2An
from .an2cn import An2Cn
from .conf import NUMBER_CN2AN, UNIT_CN2AN


class Transform(object):
    def __init__(self) -> None:
        self.all_num = "".join(list(NUMBER_CN2AN.keys())) + "貳兩參陸柒捌玖壹肆伍"
        self.upper_num = "壹贰貳叁參肆伍陆陸柒捌玖"
        self.all_unit = "".join(list(UNIT_CN2AN.keys())) + "萬億"
        self.cn2an = Cn2An().cn2an
        self.an2cn = An2Cn().an2cn
        self.cn_pattern = f"负?([{self.all_num}两{self.all_unit}]+点)?[{self.all_num}两{self.all_unit}]+"
        self.smart_cn_pattern = f"-?([0-9]+\\.)?[0-9]+[{self.all_unit}]+"
        self.measure_words = (
            "斤|克|千克|公斤|吨|米|厘米|毫米|公里|升|毫升|元|角|分|个|只|条|张|块|瓶|杯|份|本|"
            "辆|台|匹|头|位|亩|小时|分钟|秒|天|半"
        )
        self.half_pattern = re.compile(f"半(?={self.measure_words})")

    def transform(self, inputs: str, method: str = "cn2an") -> str:
        if method == "cn2an":
            inputs = inputs.replace("廿", "二十")
            inputs = self.half_pattern.sub("0.5", inputs)
            # date
            inputs = re.sub(
                fr"((({self.smart_cn_pattern})|({self.cn_pattern}))年)?([{self.all_num}{self.all_unit}]+月)?([{self.all_num}{self.all_unit}]+日)?",
                lambda x: self.__sub_util(x.group(), "cn2an", "date"), inputs)
            # fraction
            inputs = re.sub(fr"{self.cn_pattern}分之{self.cn_pattern}",
                            lambda x: self.__sub_util(x.group(), "cn2an", "fraction"), inputs)
            # percent
            inputs = re.sub(fr"百分之{self.cn_pattern}",
                            lambda x: self.__sub_util(x.group(), "cn2an", "percent"), inputs)
            # celsius
            inputs = re.sub(fr"(零下)?{self.cn_pattern}摄氏度",
                            lambda x: self.__sub_util(x.group(), "cn2an", "celsius"), inputs)
            # number
            output = re.sub(self.cn_pattern,
                            lambda x: self.__sub_cn_number(x), inputs)

        elif method == "an2cn":
            inputs = re.sub(fr"\d+(\.\d+)?-\d+(\.\d+)?(?=({self.measure_words}))",
                            lambda x: self.__sub_util(x.group(), "an2cn", "range"), inputs)
            # date
            inputs = re.sub(r"(\d{2,4}年)?(\d{1,2}月)?(\d{1,2}日)?",
                            lambda x: self.__sub_util(x.group(), "an2cn", "date"), inputs)
            # fraction
            inputs = re.sub(r"\d+/\d+",
                            lambda x: self.__sub_util(x.group(), "an2cn", "fraction"), inputs)
            # percent
            inputs = re.sub(r"-?(\d+\.)?\d+%",
                            lambda x: self.__sub_util(x.group(), "an2cn", "percent"), inputs)
            # celsius
            inputs = re.sub(r"\d+℃",
                            lambda x: self.__sub_util(x.group(), "an2cn", "celsius"), inputs)
            # number
            output = re.sub(r"-?(\d+\.)?\d+",
                            lambda x: self.__sub_util(x.group(), "an2cn", "number"), inputs)
        else:
            raise ValueError(f"error method: {method}, only support 'cn2an' and 'an2cn'!")

        return output

    def __sub_util(self, inputs, method: str = "cn2an", sub_mode: str = "number") -> str:
        try:
            if inputs:
                if method == "cn2an":
                    if sub_mode == "date":
                        return re.sub(fr"(({self.smart_cn_pattern})|({self.cn_pattern}))",
                                      lambda x: str(self.cn2an(x.group(), "smart")), inputs)
                    elif sub_mode == "fraction":
                        if inputs[0] != "百":
                            frac_result = re.sub(self.cn_pattern,
                                                 lambda x: str(self.cn2an(x.group(), "smart")), inputs)
                            numerator, denominator = frac_result.split("分之")
                            return f"{denominator}/{numerator}"
                        else:
                            return inputs
                    elif sub_mode == "percent":
                        return re.sub(f"(?<=百分之){self.cn_pattern}",
                                      lambda x: str(self.cn2an(x.group(), "smart")), inputs).replace("百分之", "") + "%"
                    elif sub_mode == "celsius":
                        negative = inputs.startswith("零下")
                        number_text = inputs[2:-3] if negative else inputs[:-3]
                        sign = "-" if negative else ""
                        return f"{sign}{self.cn2an(number_text, 'smart')}℃"
                    elif sub_mode == "number":
                        return str(self.cn2an(inputs, "smart"))
                    else:
                        raise Exception(f"error sub_mode: {sub_mode} !")
                else:
                    if sub_mode == "date":
                        inputs = re.sub(r"\d+(?=年)",
                                        lambda x: self.an2cn(x.group(), "direct"), inputs)
                        return re.sub(r"\d+",
                                      lambda x: self.an2cn(x.group(), "low"), inputs)
                    elif sub_mode == "fraction":
                        frac_result = re.sub(r"\d+", lambda x: self.an2cn(x.group(), "low"), inputs)
                        numerator, denominator = frac_result.split("/")
                        return f"{denominator}分之{numerator}"
                    elif sub_mode == "celsius":
                        return self.an2cn(inputs[:-1], "low") + "摄氏度"
                    elif sub_mode == "percent":
                        return "百分之" + self.an2cn(inputs[:-1], "low")
                    elif sub_mode == "range":
                        start, end = inputs.split("-")
                        return f"{self.an2cn(start, 'low')}到{self.an2cn(end, 'low')}"
                    elif sub_mode == "number":
                        return self.an2cn(inputs, "low")
                    else:
                        raise Exception(f"error sub_mode: {sub_mode} !")
        except Exception as e:
            warn(str(e))
            return inputs

    def __sub_cn_number(self, match) -> str:
        inputs = match.group()
        if inputs == "两":
            suffix = match.string[match.end():]
            if not re.match(self.measure_words, suffix):
                return inputs
        if len(inputs) == 1 and inputs in self.upper_num:
            suffix = match.string[match.end():]
            if not re.match(self.measure_words, suffix):
                return inputs
        return self.__sub_util(inputs, "cn2an", "number")

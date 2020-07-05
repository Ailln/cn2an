import re

from . import utils
from .cn2an import Cn2An
from .an2cn import An2Cn


class Transform(object):
    def __init__(self) -> None:
        self.conf = utils.get_default_conf()
        self.all_num = "".join(list(self.conf["number_cn2an"].keys()))
        self.all_unit = "".join(list(self.conf["unit_cn2an"].keys()))
        self.cn2an = Cn2An().cn2an
        self.an2cn = An2Cn().an2cn
        self.cn_pattern = f"负?[{self.all_num}{self.all_unit}]+"

    def transform(self, inputs: str, method: str = "cn2an") -> str:
        if method == "cn2an":
            # date
            inputs = re.sub(fr"([{self.all_num}]+年)?([{self.all_num}]+月)?([{self.all_num}]+日)?",
                            lambda x: self.__sub_util(x.group(), "cn2an", "date"), inputs)

            # percent
            inputs = re.sub(fr"百分之{self.cn_pattern}",
                            lambda x: self.__sub_util(x.group(), "cn2an", "percent"), inputs)

            # number
            output = re.sub(self.cn_pattern,
                            lambda x: self.__sub_util(x.group(), "cn2an", "number"), inputs)
        elif method == "an2cn":
            # date
            inputs = re.sub(r"([0-9]{2,4}年)?([0-9]{1,2}月)?([0-9]{1,2}日)?",
                            lambda x: self.__sub_util(x.group(), "an2cn", "date"), inputs)

            # percent
            inputs = re.sub(r"[0-9]+%",
                            lambda x: self.__sub_util(x.group(), "an2cn", "percent"), inputs)

            # number
            output = re.sub(r"\d+",
                            lambda x: self.__sub_util(x.group(), "an2cn", "number"), inputs)
        else:
            raise ValueError(f"error method: {method}, only support 'cn2an' and 'an2cn'!")

        return output

    def __sub_util(self, inputs, method: str = "cn2an", sub_mode: str = "number") -> str:
        if inputs:
            if method == "cn2an":
                if sub_mode == "date":
                    return re.sub(self.cn_pattern,
                                  lambda x: str(self.cn2an(x.group(), "smart")), inputs)
                elif sub_mode == "percent":
                    return re.sub(f"(?<=百分之){self.cn_pattern}",
                                  lambda x: str(self.cn2an(x.group(), "smart")) + "%", inputs)[3:]
                elif sub_mode == "number":
                    return str(self.cn2an(inputs, "smart"))
                else:
                    raise Exception(f"error sub_mode: {sub_mode} !")
            else:
                if sub_mode == "date":
                    return re.sub(r"\d+",
                                  lambda x: self.an2cn(x.group(), "direct"), inputs)
                elif sub_mode == "percent":
                    return "百分之" + self.an2cn(inputs[:-1], "low")
                elif sub_mode == "number":
                    return self.an2cn(inputs, "low")
                else:
                    raise Exception(f"error sub_mode: {sub_mode} !")

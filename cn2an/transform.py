import re

from . import utils
from .cn2an import Cn2An
from .an2cn import An2Cn


class Transform(object):
    def __init__(self):
        self.conf = utils.get_default_conf()
        self.cn2an = Cn2An().cn2an
        self.an2cn = An2Cn().an2cn

    def transform(self, inputs, mode="cn2an"):
        if mode == "cn2an":
            pattern = r"[负" + "".join(self.conf["number_low"] + list(set(self.conf["unit_low"]))) + "]+"
            output = re.sub(pattern, lambda x: str(self.cn2an(x.group())), inputs)
        elif mode == "an2cn":
            pattern = r"\d+"
            output = re.sub(pattern, lambda x: self.an2cn(x.group()), inputs)
        else:
            raise ValueError(f"error mode: {mode}, only support 'cn2an' and 'an2cn'!")

        return output

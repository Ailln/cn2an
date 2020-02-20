import re

from . import utils
from .cn2an import Cn2An
from .an2cn import An2Cn


class Transform(object):
    def __init__(self):
        self.conf = utils.get_default_conf()
        self.cn2an = Cn2An().cn2an
        self.an2cn = An2Cn().an2cn

    def transform(self, sentence, method="cn2an"):
        if method == "cn2an":
            re_item = self.conf["number_low"] + list(set(self.conf["unit_low"]))
            pattern = r"[负" + "".join(re_item) + "]+"
            output = re.sub(pattern, lambda x: str(self.cn2an(x.group())), sentence)
        elif method == "an2cn":
            pattern = r"[0-9]+"
            output = re.sub(pattern, lambda x: self.an2cn(x.group()), sentence)
        else:
            raise ValueError(f"error method: {method}, only support 'cn2an' and 'an2cn'!")

        return output

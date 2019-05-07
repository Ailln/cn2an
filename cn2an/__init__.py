from . import version
from . import cn2an as c2a
from . import an2cn as a2c
from . import utils


__version__ = version.VERSION

cn2an = c2a.Cn2An().cn2an
an2cn = a2c.An2Cn().an2cn
cn2an_shell = c2a.Cn2An().cn2an_shell
an2cn_shell = a2c.An2Cn().an2cn_shell

from .version import VERSION
from .cn2an import Cn2An
from .an2cn import An2Cn
from .transform import Transform

__version__ = VERSION

cn2an = Cn2An().cn2an
an2cn = An2Cn().an2cn
transform = Transform().transform

__all__ = [
    "__version__",
    "cn2an",
    "an2cn",
    "transform"
]

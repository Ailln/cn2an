"""Simple preprocessing utilities for cn2an.

This module provides a lightweight implementation of the preprocessing
pipelines referenced in `cn2an.py` and `an2cn.py`:
1. traditional_to_simplified: convert common traditional Chinese number/unit characters to simplified.
2. full_angle_to_half_angle: convert full-width (全角) ASCII and digit characters to half-width (半角).

If a character is not in the mapping it is left unchanged.
"""

from typing import Iterable, List

_TRADITIONAL_MAP = {
    # digits (保留〇原样以便在 strict 模式下触发非法字符校验)
    "零": "零", "壹": "一", "貳": "二", "贰": "二", "叁": "三", "肆": "四", "伍": "五",
    "陸": "六", "陆": "六", "柒": "七", "捌": "八", "玖": "九", "拾": "十",
    # units
    "佰": "百", "仟": "千", "萬": "万", "億": "亿", "圓": "圆", "圆": "圆", "兩": "两",
    # currency variants
    "元": "元", "角": "角", "分": "分",
}


def _traditional_to_simplified(text: str) -> str:
    return "".join(_TRADITIONAL_MAP.get(ch, ch) for ch in text)


def _full_angle_to_half_angle(text: str) -> str:
    """Convert full-width ASCII/digits to half-width.

    Full-width characters range: 0xFF01-0xFF5E. The conversion rule
    is: code_point - 0xFEE0. Space (0x3000) becomes normal space.
    Unmapped characters are returned unchanged.
    """
    result_chars: List[str] = []
    for ch in text:
        code = ord(ch)
        if code == 0x3000:  # full-width space
            result_chars.append(" ")
        elif 0xFF01 <= code <= 0xFF5E:
            result_chars.append(chr(code - 0xFEE0))
        else:
            result_chars.append(ch)
    return "".join(result_chars)


_PIPELINE_FUNC = {
    "traditional_to_simplified": _traditional_to_simplified,
    "full_angle_to_half_angle": _full_angle_to_half_angle,
}


def preprocess(text: str, pipelines: Iterable[str]) -> str:
    """Apply preprocessing pipelines sequentially to the input text.

    :param text: original text
    :param pipelines: iterable of pipeline names in execution order
    :return: processed text
    """
    for name in pipelines:
        func = _PIPELINE_FUNC.get(name)
        if func is not None:
            text = func(text)
    return text

__all__ = ["preprocess"]

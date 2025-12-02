from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any, Dict

# Ensure local package is importable without installation.
BASE_DIR = Path(__file__).resolve().parent
LOCAL_LIB = BASE_DIR / "build" / "lib"
if LOCAL_LIB.exists():
    sys.path.insert(0, str(LOCAL_LIB))

from flask import Flask, jsonify, request, send_from_directory

from cn2an import an2cn as an2cn_func
from cn2an import cn2an as cn2an_func
from cn2an import transform as transform_func

app = Flask(__name__, static_folder="frontend", static_url_path="")

HYPHEN_RANGE_PATTERN = re.compile(r"\d\s*-\s*\d")
CH_NUMERAL = "零〇一二三四五六七八九十百千万亿兆点兩两壹贰叁肆伍陆柒捌玖拾佰仟萬億兆0123456789"
RANGE_NEG_PATTERN = re.compile(rf"(?<=([{CH_NUMERAL}]))负(?=([{CH_NUMERAL}]))")
RANGE_HYPHEN_RESULT_PATTERN = re.compile(r"(?<=\d)\s*-\s*(?=\d)")


def _bad_request(message: str):
    return jsonify({"error": message}), 400


def _get_json_payload() -> Dict[str, Any]:
    payload = request.get_json(silent=True) or {}
    if not isinstance(payload, dict):
        raise ValueError("请求体必须是 JSON 对象")
    return payload


@app.get("/")
def index():
    """Serve the frontend single page."""
    return send_from_directory(app.static_folder, "index.html")


@app.post("/api/cn2an")
def api_cn2an():
    try:
        payload = _get_json_payload()
    except ValueError as exc:
        return _bad_request(str(exc))

    text = str(payload.get("text", "")).strip()
    mode = str(payload.get("mode", "strict")).strip() or "strict"

    if not text:
        return _bad_request("text 不能为空")

    try:
        result = cn2an_func(text, mode)
    except Exception as exc:  # noqa: BLE001
        return _bad_request(str(exc))

    return jsonify({"result": result})


@app.post("/api/an2cn")
def api_an2cn():
    try:
        payload = _get_json_payload()
    except ValueError as exc:
        return _bad_request(str(exc))

    text = str(payload.get("text", "")).strip()
    mode = str(payload.get("mode", "low")).strip() or "low"

    if not text:
        return _bad_request("text 不能为空")

    try:
        result = an2cn_func(text, mode)
    except Exception as exc:  # noqa: BLE001
        return _bad_request(str(exc))

    return jsonify({"result": result})


@app.post("/api/transform")
def api_transform():
    try:
        payload = _get_json_payload()
    except ValueError as exc:
        return _bad_request(str(exc))

    text = str(payload.get("text", "")).strip()
    direction = str(payload.get("direction", "cn2an")).strip() or "cn2an"

    if direction not in {"cn2an", "an2cn"}:
        return _bad_request("direction 仅支持 cn2an 或 an2cn")

    if not text:
        return _bad_request("text 不能为空")

    should_fix_range_an2cn = (
        direction == "an2cn" and text.count("-") == 1 and HYPHEN_RANGE_PATTERN.search(text)
    )
    should_fix_range_cn2an = (
        direction == "cn2an" and text.count("-") == 1 and HYPHEN_RANGE_PATTERN.search(text)
    )
    text_for_transform = text
    try:
        result = transform_func(text_for_transform, direction)
    except Exception as exc:  # noqa: BLE001
        return _bad_request(str(exc))

    if should_fix_range_an2cn:
        result = RANGE_NEG_PATTERN.sub("到", result)
    elif should_fix_range_cn2an:
        result = RANGE_HYPHEN_RESULT_PATTERN.sub("到", result)

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


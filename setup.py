import sys
from setuptools import setup
from setuptools import find_packages

NAME = "cn2an"
VERSION = "0.5.12"
AUTHOR = "Ailln"
EMAIL = "kinggreenhall@gmail.com"
URL = "https://github.com/Ailln/cn2an"
LICENSE = "MIT License"
DESCRIPTION = "Convert Chinese numerals and Arabic numerals."

if sys.version_info[:2] < (3, 6):
    raise RuntimeError("Python version >= 3.6 required.")

if __name__ == "__main__":
    setup(
        name=NAME,
        version=VERSION,
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        license=LICENSE,
        description=DESCRIPTION,
        packages=find_packages(),
        include_package_data=True,
        install_requires=open("./requirements.txt", "r", encoding="utf-8").read().splitlines(),
        long_description=open("./README.md", "r", encoding="utf-8").read(),
        long_description_content_type='text/markdown',
        zip_safe=True,
        classifiers=[
            "Programming Language :: Python :: 3",
            f"License :: OSI Approved :: {LICENSE}",
            "Operating System :: OS Independent",
        ],
        python_requires=">=3.6"
    )

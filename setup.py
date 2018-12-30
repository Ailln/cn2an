# encoding: utf-8

from __future__ import absolute_import

from setuptools import setup
from setuptools import find_packages

from cn2an import version


setup(
    name="cn2an",
    version=version.VERSION,
    author="HaveTwoBrush",
    author_email="kinggreenhall@gmail.com",
    url="https://github.com/kinggreenhall/cn2an",
    packages=find_packages(),
    include_package_data=True,
    install_requires=open("./requirements.txt", "r").read().splitlines(),
    description="Convert Chinese numerals and Arabic numerals.",
    long_description=open("./README.md", "r").read(),
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "cn2an=cn2an:cn2an",
            "an2cn=cn2an:an2cn"
        ]
    },
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)

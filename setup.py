from setuptools import setup

setup(
    name='cn2an',
    version='0.0.2',
    author='HaveTwoBrush',
    author_email='kinggreenhall@gmail.com',
    url='https://v2ai.cn',
    packages=['cn2an'],
    install_requires=[],
    description='Convert Chinese numerals and Arabic numerals.',
    setup_requires=['setuptools-markdown'],
    long_description_markdown_filename='README.md',
    entry_points={
        'console_scripts': [
            'cn2an=cn2an:cn2an',
            'an2cn=cn2an:an2cn'
        ]
    }
)

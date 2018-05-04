from setuptools import setup

setup(
    name='cn2an',
    version='0.0.1',
    author='HaveTwoBrush',
    author_email='kinggreenhall@gmail.com',
    url='https://v2ai.cn',
    description='Convert Chinese numerals and Arabic numerals.',
    packages=['cn2an'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'cn2an=cn2an:cn2an',
            'an2cn=cn2an:an2cn'
        ]
    }
)

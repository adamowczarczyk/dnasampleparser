from setuptools import setup

setup(
    name='gparser',
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        gparser=main:cli
    ''',
)

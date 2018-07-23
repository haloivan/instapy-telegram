from setuptools import setup

__version__ = '1.0'
__author__ = 'Halo Ivan'

requirements = [
    'python-telegram-bot==10.1.0'
]

description = 'InstaPy Telegram Bot'

setup(
    name='instapy_telegram',
    version=__version__,
    author=__author__,
    author_email='halo.ivan@devanesia.com',
    url='https://github.com/haloivan/instapy-telegram',
    py_modules='instatelemod',
    description=description,
    install_requires=requirements,
    packages=['instatelemod'],
    include_package_data=True,
)

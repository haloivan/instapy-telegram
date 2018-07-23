# instapy-telegram
This project is my learning project with telegram bot using python language.

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)

## How to run instapy-telegram in ubuntu 16.04 LTS or Higher version

### You must install InstaPy project on your ubuntu server/pc
<a href='https://github.com/timgrossmann/InstaPy/blob/master/docs/How_To_DO_Ubuntu_on_Digital_Ocean.md'>Click Here for The Tutorial</a>

### Please Follow This Step!!! for installing instapy-telegram project
```sh
$ pip install --upgrade pip
$ pip install python-telegram-bot
$ usersys=$(whoami)
$ cd /$usersys/InstaPy
$ git clone https://github.com/haloivan/instapy-telegram.git
$ cp /$usersys/InstaPy/instapy-telegram/instapytelegram.py /$usersys/InstaPy/instapytelegram.py
```

#### Setting
- open file config.ini in folder instapy-telegram --> teledata
- insert your telegram token, instagram username (without @) and password
- open and edit file instapytelegram.py (in InstaPy Folder)
- find this code and change all "x" with your favorite hashtag (without #)
```sh
tag_1 = ['x', 'x', 'x', 'x', 'x']
tag_2 = ['x', 'x', 'x', 'x', 'x']
tag_3 = ['x', 'x', 'x', 'x', 'x']
tag_4 = ['x', 'x', 'x', 'x', 'x']
```
- save

#### Run
```sh
$ cd /root/InstaPy && /usr/bin/python /root/InstaPy/instapytelegram.py
```

### Noted
Every you updating this repo please do the last step in installing this project tutorial, for work properly.

Have issue with this project? come write <a href='https://github.com/haloivan/instapy-telegram/issues'>here</a>. I will help you as much as possible.

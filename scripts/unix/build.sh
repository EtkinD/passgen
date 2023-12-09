#!/bin/bash

source venv/bin/activate

pyinstaller -D -F -c -i assets/icon.ico -n PasswordGenerator main.py

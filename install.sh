#!usr/bin/bash

pkg install python
python -m pip install --upgrade pip
pip install uvicorn
pip install fastapi
pip install python-multipart

pkg install gh
gh auth login
gh repo clone sasha0000kr/TempMonitor

cd TempMonitor
python kernel.py
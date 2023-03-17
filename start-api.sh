#!/bin/bash

# ./start-api.sh

dpkg --list | grep "venv" > /dev/null 

if [ $? -ne 0 ]; then
   echo -e "❌  package python3-venv is not installed!\n"
   exit 1
fi

if [ -d venv ]; then	
   
   echo -e "🐍  Activating Python virtual environment... "
   source venv/bin/activate
   pip3 freeze | grep -E "flask-restx" > /dev/null
   if [ ! $? -ne 0 ]; then
      echo "📦  Installing API dependencies... "
      pip3 install flask flask-restx python-dotenv requests > /dev/null
   fi
else
   echo "🕒 Craeting Python virtual environment... "
   python3 -m venv venv
   echo -e "🐍  Activating Python virtual environment... "
   source venv/bin/activate
   
   echo "📦  Installing API dependencies... "
   pip3 install flask flask-restx python-dotenv requests > /dev/null 
fi

echo -e "🔛  Start API in port 8181\n"
python3 api/api.py

#!/bin/bash
# ./app-compose.sh <option>[--start|--destroy]

OPTION=$1

echo "IP_HOST_API=$(hostname -I | cut -d" " -f1)" > ./.env
ENVFILE=$PWD/.env
if [ ! -s "$ENVFILE" ]; then
        echo "File .env does not exist or is empty!"; exit
fi

case $OPTION in
        "--start")
                echo -e '🐳  Building containers ...'
                docker-compose build > /dev/null
                echo -e '🐳  Starting containers ...'
                docker-compose up -d > /dev/null
                echo -e '🚀  container started successfully!'
                echo "🕒 Initilize API Provision ... "
                bash start-api.sh
                ;;
        "--destroy")
                echo -e '🔴  Destroying containers and images ...'
                docker-compose down --rmi all
                echo -e '🤝  Finished environment ...'
                ;;
        *)
                echo "Not a valid argument!"
                echo "excution example: ./app-compose.sh <option>[--start|--destroy]"
esac
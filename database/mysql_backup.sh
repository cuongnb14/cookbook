#!/bin/bash
# ls -1tr | head -n -10 | xargs -d '\n' rm -f --
# Requirements :mysqldump (sudo apt-get install mysql-client)
# Upzip file: gzip -d ${DIR_BACKUP}/${FILE_BACKUP}.sql.gz
# -----------------------------------------------------------

MYSQL_HOST='127.0.0.1'
MYSQL_PORT='3309'

MYSQL_USER='root'
MYSQL_PASSWORD=dev@123
MYSQL_DATABASE=plusfun

DIR_BACKUP='/home/cuongnb/tmp'
DATE_BACKUP=`date +%Y-%m-%d"_"%H-%M-%S`
FILE_BACKUP=${MYSQL_DATABASE}_${DATE_BACKUP}

KEEP_NEWEST=3

echo "Start backup..."
mysqldump -h ${MYSQL_HOST} -P ${MYSQL_PORT} -u${MYSQL_USER} -p${MYSQL_PASSWORD} ${MYSQL_DATABASE} | gzip > ${DIR_BACKUP}/${FILE_BACKUP}.sql.gz

echo "Remove old file"
cd ${DIR_BACKUP} && ls -1tr | head -n -${KEEP_NEWEST} | xargs -d '\n' rm -f --

echo "Done!"
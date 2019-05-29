# sudo apt install mysql-client-5.7   

MYSQL_HOST='127.0.0.1'
MYSQL_PORT='3306'

MYSQL_USER='root'
MYSQL_PASSWORD=123456

DIR_BACKUP='/tmp'

DATE_BACKUP=`date +%Y-%m-%d"_"%H-%M-%S`

for MYSQL_DATABASE in $(mysql -h ${MYSQL_HOST} -P ${MYSQL_PORT} -u${MYSQL_USER} -p${MYSQL_PASSWORD} -e 'show databases' -s --skip-column-names); do
    echo "Exporting database ${MYSQL_DATABASE} ..."
    mysqldump -h ${MYSQL_HOST} -P ${MYSQL_PORT} -u${MYSQL_USER} -p${MYSQL_PASSWORD} ${MYSQL_DATABASE} | gzip > ${DIR_BACKUP}/${MYSQL_DATABASE}_${DATE_BACKUP}.sql.gz;
done

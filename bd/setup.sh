set -e
service mysql start

use cripto

mysql < /mysql/cripto.sql

service mysql stop
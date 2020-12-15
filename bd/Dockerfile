FROM mysql:5.7.32
COPY setup.sh /mysql/setup.sh
COPY critop.sql /mysql/critop.sql

RUN /mysql/critop.sql

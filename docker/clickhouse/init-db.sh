#!/bin/bash
set -e

echo "Creating database mydb and user myuser..."

clickhouse-client <<-EOSQL
CREATE DATABASE IF NOT EXISTS mydb;

CREATE USER IF NOT EXISTS myuser
  IDENTIFIED WITH plaintext_password BY 'mypass'
  DEFAULT DATABASE mydb;

GRANT ALL ON mydb.* TO myuser WITH GRANT OPTION;
EOSQL

echo "Database 'mydb' and user 'myuser' created successfully."
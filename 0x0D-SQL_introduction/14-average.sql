#!/bin/bash
# This script calculates the average score from the table second_table in the hbtn_0c_0 database.

if [ -z "$1" ]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi

DATABASE=$1

SQL="SELECT AVG(score) AS average FROM second_table;"
mysql -u username -p --database="$DATABASE" -e "$SQL"

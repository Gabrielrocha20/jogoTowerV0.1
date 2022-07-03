import mysql.connector

con = mysql.connector.connect(host='localhost', user='root', password='', database='test')
if con.is_connected():
    db_info = con.get_server_info()
    print('\033[1;41m\033[1;97m                  TOWER                        \033[0;0m')
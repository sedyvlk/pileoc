# Hi
import psycopg2

user1c = psycopg2.connect("dbname='testdb1' user='testuser1' host='beast' password='user1'")
user2c = psycopg2.connect("dbname='testdb1' user='testuser1' host='beast' password='user1'")
user3c = psycopg2.connect("dbname='testdb1' user='testuser1' host='beast' password='user1'")
admin1c = psycopg2.connect("dbname='testdb1' user='testadmin1' host='beast' password='admin1'")
admin2c = psycopg2.connect("dbname='testdb1' user='testadmin1' host='beast' password='admin1'")


#
while 1:
    command = input("What now? ")
    if command == 'help':
        print('conns --> Show me connections')

    elif command == 'quit':
        print('Bye')
        break
    elif command == 'conns':
        pass

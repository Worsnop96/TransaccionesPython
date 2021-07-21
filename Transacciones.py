import psycopg2

conexion = psycopg2.connect(user='postgres', password='****', host='localhost', port='5432', database='test_db')

try:
    conexion.autocommit =False
    cursor= conexion.cursor()
    sentencia = "insert into persona(nombre, apellido) values(%s, %s)"
    valor=('maria', 'gomez')
    cursor.execute(sentencia, valor)
    #update
    sentencia = "update persona set nombre = %s where id = %s"
    valor=('carmen', 12)
    cursor.execute(sentencia, valor)
    print(f'fin de transaccion')
    sentencia = "delete from persona"
    cursor.execute(sentencia)
    conexion.commit()
except Exception as e:
    conexion.rollback()
    print(f'ha ocurrido un error de tipo {e}, y se ha generado un rollback')
finally:
    conexion.close()
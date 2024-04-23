## импортировать необходимые модули
import pyodbc
import pandas as pd
import sqlalchemy as sa

##Подключаемся к базе данных
# Specifying the ODBC driver, server name, database, etc. directly
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost,14333;DATABASE=computer;UID=sa;PWD=SQLPaw!2;CHARSET=UTF8')
# Create a cursor from the connection
cursor = cnxn.cursor()

##Формат выполнения запросов. - Теперь готовы. Копим запросы :-)
query = '''
SELECT *
FROM Pass_in_trip
JOIN Passenger ON Pass_in_trip.ID_psg = Passenger.ID_psg
WHERE Pass_in_trip.trip_no = 1123;
'''

sql_query = pd.read_sql_query(query, cnxn)

df = pd.DataFrame(sql_query)
df

##для проверки на NULL стандарт предлагает более короткую форму — оператор COALESCE
query = '''
SELECT DISTINCT Product.model,
 COALESCE(CAST(price AS CHAR(20)),'Нет в наличии') price
FROM Product LEFT JOIN
 PC ON Product.model = PC.model
WHERE Product.type = 'pc';'''


##Использование CASE с агрегатной функцией - NULLIF
query = '''
SELECT COUNT(*) total_qty, 
COUNT(NULLIF(town_to, 'Moscow')) non_moscow
FROM Trip
WHERE town_from='Rostov';
'''
## Импортировать необходимые модули
import pyodbc
import pandas as pd
import sqlalchemy as sa

## Подключаемся к базе данных используя pyodbc - устаревший вариант - больше не используется
# Specifying the ODBC driver, server name, database, etc. directly
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost,14333;DATABASE=computer;UID=sa;PWD=SQLPaw!2;CHARSET=UTF8')
# Create a cursor from the connection
cursor = cnxn.cursor()

## Подключаемся к базе данных, используя рекомендуемый SQLalchemy
# В подключении используется ODBC драйвер freetds (https://www.freetds.org/docs.html), абсолютная ссылка на файл которого используется в строке подключения
import pandas as pd
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

dburl = 'mssql://sa:SQLPaw!2@localhost,14333/inc_out?driver=/opt/homebrew/Cellar/freetds/1.4.12/lib/libtdsodbc.so'
engine = create_engine(dburl)
connection = engine.connect()

## формат выполнения запросов через SQLalchemy
query = "SELECT * FROM table"

with Session(engine) as session:
    res = connection.execute(sa.text(query))
    df = pd.DataFrame(res)
# выводим результат запроса
df

## Копим запросы :-)
# Join
query = '''
SELECT *
FROM Pass_in_trip
JOIN Passenger ON Pass_in_trip.ID_psg = Passenger.ID_psg
WHERE Pass_in_trip.trip_no = 1123;
'''

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
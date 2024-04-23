## 1. читаем из файла
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

## 2. читаем все файлы в папке по маске и собираем один датафрейм
import glob
l = [pd.read_excel(filename) for filename in glob.glob("../folder/filename*.xlxs")]
df_load = pd.concat(l, axis = 0)

## 3. Выборка в датафрейме по списку значений
keys = ['value1', 'value2']
df_f = df_load
df_f1 = df_f.loc[df_f['column'].isin(keys)]
table = pd.pivot_table(df_f1, values='count_all', index=['to_date'], columns = ['Key'], aggfunc=np.sum)
table = table.transponse()

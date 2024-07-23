import random
import pandas as pd

# Генерация данных
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
# Преобразование в one hot
# создаём новый пустой объект DataFrame и кладём в переменную one_hot
one_hot = pd.DataFrame()
# Создаём цикл, который проходит по каждой категории из списка уникальных значений столбца whoAmI data['whoAmI'].unique()
for category in data['whoAmI'].unique():
    one_hot[category] = (data['whoAmI'] == category).astype(int) # добавляем столбец, в котором имя стобца соответсвует категории, значением будет булевый массив, преобразованный в численный

# Печать результата 
print(one_hot.head())



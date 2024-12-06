# ЗАДАНИЕ ПО ТЕМЕ "Обзор сторонних библиотек Python"

import pandas as pd
from matplotlib import pyplot as plt
from PIL import Image

"""
С помощью библиотеки PANDAS считываем данные из csv-файла.
В файле содержатся данные о среднемесячных температурах за 2023 по трем городам России.
Рассчитываем максимальное, минимальное и среднегодовое значение для каждого города,
добавляем рассчитанные данные в таблицу и выгружаем новую таблицу в xlsx-файл
"""
# Считываем данные из файла scv и представляем в виде массива DataFrame
table_read = pd.read_csv('AvMonTemp_2023.csv', delimiter=';', encoding='UTF-8')
# Устанавливаем значения столбца "город" в качестве индекса строк
table_read.set_index('город', inplace=True)
# Добавим в DataFrame столбцы с максимальной, минимальной и средней температурой для каждого города
table_read['Макс.температура'] = table_read.max(axis=1)
table_read['Мин.температура'] = table_read.min(axis=1)
table_read['Среднегодовая температура'] = table_read.mean(axis=1).round(1)
# Выведем на консоль значения последних трех столбцов полученной таблицы
print(table_read.iloc[:, -3:])
# Сохраним данные полученного массива в xlsx-файл
table_read.to_excel('AvMonTemp_new.xlsx')

"""
С помощью библиотеки MATPLOTLIB строим линейные графики и
сохраняем полученный график в jpg-файл
"""
# Для построения графика в качестве аргумента X возьмем заголовки столбцов с месяцами
x = list(table_read.columns[0:11])
# Для построения графиков в качестве аргументов Y возьмем значения строк с температурой за 12 месяцев
y1 = table_read.iloc[0, 0:11]
y2 = table_read.iloc[1, 0:11]
y3 = table_read.iloc[2, 0:11]
# Наименования для легенды - индексы строк
leg1 = table_read.index[0]
leg2 = table_read.index[1]
leg3 = table_read.index[2]
# Задать размер окна для графика
plt.figure(figsize=(10, 6))
# Строим три линейных графика
plt.plot(x, y1, color='g', lw=3, marker='o', markersize=5, label=leg1)
plt.plot(x, y2, color='r', lw=3, marker='o', markersize=5, label=leg2)
plt.plot(x, y3, color='b', lw=3, marker='o', markersize=5, label=leg3)
# Проведем на графике горизонтальную линию у = 0
plt.axhline(y=0, color='m', ls='--', lw=2)
# Задаем название графика и параметры других элементов графика
plt.title('Среднемесячная температура за 2023 год\n', fontweight='bold', fontsize=18)
plt.xlabel('Месяц', fontweight='bold', fontsize=12)  # Подпись для оси х
plt.ylabel('Температура (°C)', fontweight='bold', fontsize=12)  # Подпись для оси y
plt.grid(linestyle='--')  # Отображение сетки на графике
plt.legend(loc=2, fontsize=12)  # Легенда графика, расположение - левый верхний угол (upper left)
# Сохраним график в jpg-файл
plt.savefig('AvMonTemp_2023.jpg')
# Вывод полученного графика на экран
# plt.show()

"""
С помощью библиотеки PILLOW оформляем изображение с графиком, сделав фоном другую картинку
и выгружаем полученное изображение в pdf-файл
"""
# Открываем изображения графика и картинки для фона
image1 = Image.open('AvMonTemp_2023.jpg')
image2 = Image.open('seasons_01.jpg')
w1, h1 = image1.size  # Размеры первого изображения
# Делаем размеры второго изображения такими же, как и у первого
image2 = image2.resize((w1, h1))
# Накладываем одно изображение на другое
image3 = Image.blend(image1, image2, 0.3)
# Вывод полученного изображения на экран
image3.show()
# Сохраняем полученное изображение в pdf-файл
image3.save('AvMonTemp_new.pdf')

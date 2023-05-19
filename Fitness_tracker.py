weight = 75 # Вес
height = 175 # Рост
steps = 8462 # Количество пройденных за день шагов
hours = 2 # Время движения в часах
len_step_m = 0.65 # Длина одного шага в метрах
transfer_coeff = 1000 # Коэффициент перевода значения растояния из метров в километры

dist = steps*len_step_m / transfer_coeff

mean_speed = dist / hours
minutes = hours * 60

if dist >= 6.5:
    achievement = 'Отличный результат! Цель достигнута.'
elif dist >= 3.9:
    achievement = 'Неплохо! День был продуктивным.'
elif dist >= 2:
    achievement = 'Маловато, но завтра наверстаем!'
else:
    achievement = 'Лежать тоже полезно. Главное — участие, а не победа!'

spent_calories = (0.035*weight + (mean_speed**2 / height) * 0.029*weight) * minutes

output = f'''Сегодня вы прошли {steps} шагов.
Пройденная дистанция {dist:.2f} км.
Вы сожгли {spent_calories:.2f} ккал.
{achievement}'''         
print(output)


Сегодня вы прошли 8462 шагов.
Пройденная дистанция 5.50 км.
Вы сожгли 326.28 ккал.
Неплохо! День был продуктивным.
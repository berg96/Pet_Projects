weight = 75 # Вес
height = 175 # Рост
steps = 8462 # Количество пройденных за день шагов
hours = 2 # Время движения в часах
len_step_m = 0.65 # Длина одного шага в метрах
transfer_coeff = 1000 # Коэффициент перевода значения расстояния из метров в километры

dist = steps * len_step_m / transfer_coeff # Напишите формулу расчёта

mean_speed = dist / hours
minutes = hours * 60

spent_calories = (0.035*weight + (mean_speed**2 / height) * 0.029*weight) * minutes

output = f'Сегодня вы прошли {dist:.2f} км и затратили {spent_calories:.2f} килокалорий. '  # Здесь подготовьте строку для вывода
print(output)
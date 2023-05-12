print('Привет, я Анфиса!')
print('Я маленькая, но уже программа!')

name = 'Анфиса'                # Имя
job = 'персональный помощник'  # Профессия

print('Привет, я ' + name + ', твой ' + job + '!')

count = 8
message = 'У вас ' + str(count) + ' новых сообщений'
print(message)

temperature = -25
weather = 'солнечно'

print('Сегодня ' + weather)
print(f'Температура воздуха {temperature} градусов')


friends = ['Сергей', 'Соня', 'Дима', 'Алина', 'Егор']

print(friends)

index = -2

print('Привет, ' + friends[index] + ', я Анфиса!')

index = 2

print(f'{friends[index]} живёт в Красноярске')

count = len(friends)

print(f'У тебя {count} друзей')


for messages_count in range(0, 21):
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        print('У вас 1 новое сообщение')
    elif messages_count < 5:
        print('У вас', messages_count, 'новых сообщения')
    else:
        print(f'У вас {messages_count} новых сообщений')


for current_hour in range(0, 24):
    print("На часах " + str(current_hour) + ":00.")
    if current_hour < 6:
        print('Доброй ночи!') 
    elif current_hour < 12:
        print('Доброе утро!')
    elif current_hour < 18:
        print('Добрый день!')
    elif current_hour < 23:
        print('Добрый вечер!')
    else:
        print('Доброй ночи!')
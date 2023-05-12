def say_about():
    print('Привет, я Анфиса!')
    print('Я персональный помощник.')
    print('Я ещё маленькая,')
    print('но постоянно расту и умнею:')
    print('ведь мой код каждый день дописывают!')

say_about()

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
    elif messages_count >=2 and messages_count <= 4:
        print(f'У вас {messages_count} новых сообщения')
    else:
        print(f'У вас {messages_count} новых сообщений')


def say_hello(current_hour):
    if current_hour <= 5 or current_hour >= 23:
        print('Доброй ночи!')
    elif current_hour >= 6 and current_hour <= 11:
        print('Доброе утро!')
    elif current_hour >= 12 and current_hour <= 17:
        print('Добрый день!')
    elif current_hour >= 18 and current_hour <= 22:
        print('Добрый вечер!')

say_hello(4)
say_hello(10)
say_hello(15)
say_hello(20)
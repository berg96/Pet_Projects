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


for messages_count in range(6):
    if messages_count > 0:
        print(f'Новых сообщений: {messages_count}')
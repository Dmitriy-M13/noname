print('Прветствую Вас!', 'Начинаем тест по математике')

points = 0
print('Чему равна сумма всех углов треугольника?')
answer = input('Ваш ответ: ')

if answer.lower() == '180':
    print('Верно!')
    points +=10
else:
    print('Неверно! ')
    points -= 10

print('Как называются два треугольника с равными углами и пропорциональными сторонами? ')
answer = input('Ваш ответ: ')

if answer.lower() == 'подобные':
    print('Верно!')
    points +=10
else:
    print('Неверно! ')
    points -= 5

print('С каких чисел начинаются числа Фибоначчи?')
answer = input('Ваш ответ: ')

if answer.lower() == '0и1':
    print('Верно!')
    points +=10
else:
    print('Неверно! ')
    points -= 10

print('Чтобы найти длину гипотенузы прямоугольного треуголника, нужно применить теорему....?')
answer = input('Ваш ответ: ')

if answer.lower() == 'пифагора':
    print('Верно!')
    points +=10
else:
    print('Неверно! ')
    points -= 10

if 40 <= points <= 50:
    print('Ваша оценка 5')

elif 30 <= points <= 40:
    print('Ваша оценка 4')

elif 20 <= points <= 30:
    print('Ваша оценка 3')

else:
    print('Ваша оценка 2')



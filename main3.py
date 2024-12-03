print('Вам нужно найти сундук и что бы его открыть, найдите ключ')


has_map = False
has_key = False
has_klad = False

energy = 100

choice = input('куда пойдешь? [север, юг, запад, восток] ')
# север-ключ, юг-карта, восток-сундук, запад-ничего

if choice == 'север':
    print('Вы нашли ключ от сундука!')
    energy -= 30
    print(f'текущий запас енергии: {energy}')
    print('Теперь найдите сундук!')
    has_key = True
    has_map = False
    has_klad = False
elif choice == 'юг':
    print('Вы нашли карту, она вам подсказывает, что ключ от сундука находится на севере. ')
    energy -= 30
    print(f'текущий запас енергии: {energy}')
    has_map = True
    has_key = False
    has_klad = False
elif choice == 'восток':
    print('вы нашли сундук, но вам теперь нужно найти ключ')
    energy -= 30
    print(f'текущий запас енергии: {energy}')
    print('Теперь найдите ключ! куда отправитесь дальше?')
    has_map = False
    has_key = False
    has_klad = False
elif choice == 'запад':
    print('вы ничего не нашли, попробуйте пойти в другую сторону')
    energy -= 30
    print(f'текущий запас енергии: {energy}')
    print('куда отправитесь дальше?')
    has_map = False
    has_key = False
    has_klad = False


hour = int(input('Ведите часы: '))
minute = int(input('Ведите минуты: '))
differents = int(input('Ведите разницу: '))

new_hour = hour + differents

if new_hour > 24:
    new_hour -=24

if new_hour < 0:
    new_hour += 24

print(f'{new_hour}:{minute}')

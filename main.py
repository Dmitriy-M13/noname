file_size = int(input('введите размер файла'))
speed = int(input('введите скорость загрузки (бит/с)'))

file_size_bit = file_size * 1024 * 1024 * 1024 * 8

download_time = file_size_bit / speed

choice = input('введите единицу измерения [с / м / ч]: ')
if choice == 'с':
    print(f'вермя скачивания файла: {download_time}с')
elif choice == 'м':
    print(f'вермя скачивания файла: {download_time// 60}м')
elif choice == 'ч':
    print(f'вермя скачивания файла: {download_time// 3600}ч')
else:
    print('некорректный выбор')
            
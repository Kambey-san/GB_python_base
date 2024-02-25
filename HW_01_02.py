"""2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды
 и выведите в формате чч:мм:сс. Используйте форматирование строк."""

time_input = int(input('Введите время в секундах: '))
time_out_h = time_input // 3600
time_h = str(time_out_h).zfill(2)   # https://pythonz.net/references/named/string.zfill/


time_out_min = (time_input - (time_out_h * 3600)) // 60
time_min = str(time_out_min).zfill(2)


time_out_sec = (time_input - (time_out_h * 3600)) - (time_out_min * 60)
time_sec = str(time_out_sec).zfill(2)

print(str(f'{time_h}:{time_min}:{time_sec}'))
'''3. Напишите код, который запрашивает число и сообщает является ли оно 
простым или составным. Используйте правило для проверки: “Число является 
простым, если делится нацело только на единицу и на себя”. Сделайте ограничение 
на ввод отрицательных чисел и чисел больше 100 тысяч.'''

MIN_NUM = 0
MAX_NUM = 100000
START = 1
MIN_PRIME_NUM = 2

input_num = -1

while not (MIN_NUM <= input_num <= MAX_NUM):
    input_num = int(input(f'Введите целое число между {MIN_NUM} и {MAX_NUM}  = '))

if input_num >= MIN_PRIME_NUM:
    sum = 0
    for i in range(START, input_num + 1):
        if input_num % i == 0:
            sum += 1
    if sum <= 2:
        print(f'Число {input_num} простое.')
    else:
        print(f'Число {input_num} составное.')
else:
    print('Числа 0 и 1 не являются ни простыми, ни составными см. определение!')
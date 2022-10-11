price_all = 0
while True:
    try:
        ticket_number = input('Сколько билетов Вам надо? ')
        ticket_number = int(ticket_number)
        if type(ticket_number) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(ticket_number):
    i += 1
    while True:
        try:
            age_for_ticket = input(f'Сколько лет тому, кому Вы берете билет №{i}? ')
            age_for_ticket = int(age_for_ticket)
            if age_for_ticket < 18:
                print('Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно')
            elif 25 > age_for_ticket >= 18:
                price_all += 990
                print('Стоимость билета со скидкой составит: 990 руб.')
            else:
                price_all += 1390
                print('Полная стоимость билета: 1390 руб.')
            if type(age_for_ticket) == int:
                break
        except ValueError:
            print('Введите целое число')
if ticket_number > 3:
    price_all = price_all - ((price_all / 100) * 10)
    print(f'ИТОГО {price_all} руб. с учетом 10%-ой скидки на полную стоимость заказа за регистрацию больше 3-х человек')
else:
    print(f'ИТОГО {price_all} руб.')
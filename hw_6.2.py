'hw_6.2'
seconds_input = input('Введіть кількість секунд: ')

if int(seconds_input) < 0 or int(seconds_input) > 8640000:
    print('Число має бути більше або дорівнювати 0 і менше ніж 8640000')
else:
    seconds_in_minute = 60
    seconds_in_hour = 60 * seconds_in_minute
    seconds_in_day = 24 * seconds_in_hour

    days = int(seconds_input) // int(seconds_in_day)
    hours = (int(seconds_input) % int(seconds_in_day)) // int(seconds_in_hour)
    minutes = (int(seconds_input) % int(seconds_in_hour)) // int(seconds_in_minute)
    seconds = int(seconds_input) % int(seconds_in_minute)

    if days % 10 == 1 and days != 11:
        days_str = f'{days} день'
    elif days == 11:
        days_str = f'{days} днів'
    elif days % 10 in {2, 3, 4} and days % 100 not in {12, 13, 14}:
        days_str = f'{days} дні'
    else:
        days_str = f'{days} днів'

    hours_str = str(hours).zfill(2)
    minutes_str = str(minutes).zfill(2)
    seconds_str = str(seconds).zfill(2)

    print(f'{seconds_input} -> {days_str}, {hours_str}:{minutes_str}:{seconds_str}')
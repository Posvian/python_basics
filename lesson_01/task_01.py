# Реализовать вывод информации о промежутке
# времени в зависимости от его продолжительности
# duration в секундах: до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = 86401
minute_duration = 60
hour_duration = minute_duration * 60
day_duration = hour_duration * 24

day_amount = duration // day_duration
hour_amount = duration % day_duration // hour_duration
minute_amount = duration % day_duration % hour_duration // minute_duration
second_amount = duration % day_duration % hour_duration % minute_duration

if duration < minute_duration:
    print(second_amount, 'сек')
elif minute_duration <= duration < hour_duration:
    print(minute_amount, 'мин', second_amount, 'сек')
elif hour_duration <= duration < day_duration:
    print(hour_amount, 'час', minute_amount, 'мин', second_amount, 'сек')
else:
    print(day_amount, 'дн', hour_amount, 'час', minute_amount, 'мин', second_amount, 'сек')


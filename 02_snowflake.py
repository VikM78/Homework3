# -*- coding: utf-8 -*-

import simple_draw as sd
max_x = 1200
max_y = 600
sd.resolution = (max_x, max_y)
# познакомится с параметрами библиотечной функции рисования снежинки sd.snowflake()

# sd.snowflake(center=point_0, length=200, factor_a=0.5)

# реализовать падение одной снежинки
y = 500
x = 100
length = 50

y2 = 450
x2 = 150
length2 = 50

y_mul = -1
x_mul = 1

y2_mul = 1
x2_mul = -1

while True:
    sd.clear_screen()
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=length)
    y += 10 * y_mul
    if y < length or y > max_y - length:
        #break
        y_mul *= -1
    x += 10 * x_mul
    if x < length or x > max_x - length:
        x_mul *= -1

    point2 = sd.get_point(x2, y2)
    sd.snowflake(center=point2, length=length2, factor_c=30)
    y2 += 10 * y2_mul
    if y2 < length2 or y2 > max_y - length:
        y2_mul = y2_mul * -1
        #break
    x2 += 20 * x2_mul
    if x2 < length2 or x2 > max_x - length2:
        x2_mul *= -1

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# реализовать падение одной снежинки из произвольного места экрана

# реализовать падение одной снежинки с ветром - смещение в сторону


sd.pause()

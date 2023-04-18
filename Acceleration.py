initial_speed = float(input("Введите начальную скорость в м/с: "))
final_speed = float(input("Введите конечную скорость в м/с: "))
time = float(input("Введите время изменения скорости в секундах: "))
acceleration = (final_speed - initial_speed) / time
print("Ускорение: {:.2f} м/с^2".format(acceleration))

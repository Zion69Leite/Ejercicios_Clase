num = (float(input("\nPor favor, ingrese su nota:\n")))

if num < 0:
    print("Su nota es Incorrecta")

if num >= 0 and num < 5:
    print("Su nota es Insuficiente")

if num >= 5 and num < 6:
    print("Su nota es Suficiente")

if num >= 6 and num < 7:
    print("Su nota esta Bien")

if num >= 7 and num < 9:
    print("Su nota es Notable")

if num >= 9 and num <= 10:
    print("Su nota es Sobresaliente")

if num > 10:
    print("Su nota es Incorrecta")

print ("\n¡¡¡Graciassss!!!")
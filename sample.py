def introducir_puntos():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()

        if not point.isdecimal() or not 0 < int(point) <= 5:
            print('Por favor, introduzca un valor entre 1 y 5')
            continue

        print('Introduzca sus comentarios.')
        comment = input()
        post = f'punto: {point} comentario: {comment}'

        with open("data.txt", 'a') as file_pc:
            file_pc.write(f'{post}\n')

        break


def comprobar_resultados():
    print('Resultados hasta la fecha.')
    with open("data.txt", "r") as read_file:
        print(read_file.read())


while True:
    print('Seleccione el proceso que desea aplicar')
    print('1:Introducir puntos de evaluación y comentarios')
    print('2:Comprueba los resultados hasta ahora.')
    print('3:Terminar.')

    num = input()

    if not num.isdecimal() or not 1 <= int(num) <= 3:
        print('Por favor, introduzca del 1 a 3')
        continue

    num = int(num)

    if num == 1:
        introducir_puntos()

    elif num == 2:
        comprobar_resultados()

    elif num == 3:
        print('Terminación.')
        break

# Григорьев Максим Денисович
# Составить программу, которая печатает True, если точка с координатами (х, у) принадлежит заданным закрашенным (заштрихованным) областям, показанным на рисунках в табл. 1, и false — в противном случае.

while True:
    try:
        x_coord = float(input("Введите координату x: "))
        y_coord = float(input("Введите координату y: "))
        
        if 0 <= x_coord <= 4 and 0 <= y_coord <= 4:
            print("Точка внутри области: True")
        else:
            print("Точка внутри области: False")
        break
    except ValueError:
        print("Ошибка! Введите правильные числовые значения для координат.")
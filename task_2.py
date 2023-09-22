'''2.Треугольник существует только тогда, когда сумма любых двух 
его сторон больше третьей. Дано a, b, c - стороны предполагаемого 
треугольника. Требуется сравнить длину каждого отрезка-стороны с 
суммой двух других. Если хотя бы в одном случае отрезок окажется 
больше суммы двух других, то треугольника с такими сторонами не 
существует. Отдельно сообщить является ли треугольник 
разносторонним, равнобедренным или равносторонним.'''

side_triangle_a = float(input("Введите длину сторону треугольника a: ")) 
side_triangle_b = float(input("Введите длину сторону треугольника b: ")) 
side_triangle_c = float(input("Введите длину сторону треугольника c: ")) 
 
if side_triangle_a >= side_triangle_b + side_triangle_c or side_triangle_b >= side_triangle_a + side_triangle_c or side_triangle_c >= side_triangle_a + side_triangle_b: 
    print("\nТреугольника с указанными Вами длинами сторон:\nДлина стороны треугольника a =", side_triangle_a,"\nДлина стороны треугольника b =", side_triangle_b,"\nДлина стороны треугольника c =", side_triangle_c,"\nНе существует!")

else: 
    print("\nТреугольник с указанными Вами длинами сторон:\nДлина стороны треугольника a =", side_triangle_a,"\nДлина стороны треугольника b =", side_triangle_b,"\nДлина стороны треугольника c =", side_triangle_c,"\nСуществует!")

    if side_triangle_a == side_triangle_b == side_triangle_c:
        print("И является равносторонним!")

    elif side_triangle_a == side_triangle_b and side_triangle_a != side_triangle_c or side_triangle_b == side_triangle_c and side_triangle_b != side_triangle_a or side_triangle_c == side_triangle_a and side_triangle_c:
        print("И является равнобедрянным!")

    else:
        print("И является разносторонним!")
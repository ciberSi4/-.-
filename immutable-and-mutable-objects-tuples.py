# Неизменяемые и изменяемые объекты. Кортежи

immutable_var = ( 1, 2, 3, "a", "b", "c" )
print ( "Вывод кортежа immutable_var на экран: ", immutable_var, type (immutable_var) )
# immutable_var [0] = 11 (TypeError: 'tuple' object does not support item assignment)
# immutable_var [3] = "s" (TypeError: 'tuple' object does not support item assignment)
# Кортеж относится к неизменяемым типам данных, тем не менее внутри он может содержать изменяемые типы
# При попытках изменить значение переменных в кортеже immutable_var - программа выдаёт ошибку

mutable_list = [ 4, 5, 6, "d", "e", "f" ]
print ( "Переменная mutable_list: ", mutable_list, type (mutable_list) )
print ( "Изменяем значения списка mutable_list" )
mutable_list [0] = 7
mutable_list [1] = 8
mutable_list [2] = 9
mutable_list [3] = "z"
mutable_list [4] = "x"
mutable_list [5] = "v"
print (mutable_list)
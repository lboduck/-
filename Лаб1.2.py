# TODO Найдите количество книг, которое можно разместить на дискете

v_d = 1.44
pages = 100
lines = 50
symbols = 25
v_symbols = 4

v_b = (v_symbols*symbols*lines*pages)/1024 ** 2
count_of_books = int(v_d/v_b)
print("Количество книг, помещающихся на дискету:",count_of_books)

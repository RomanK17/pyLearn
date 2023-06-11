a = '55'
print(id(a))  # 2780091929264, строки - immutable
a = 'aboba'
print(id(a))  # 2780091929392 - создается новый объект
a = a.upper()
print(id(a))  # 1395174756912 - новый, переменная выступает как ярлык, который ссылается на объект

result = 'hello {}'
s = result.format(a)
print(s)
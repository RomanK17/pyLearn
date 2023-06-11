a = '55'
print(id(a))  # 2780091929264, строки - immutable
a = 'aboba'
print(id(a))  # 2780091929392 - создается новый объект
a = a.upper()
print(id(a))  # 1395174756912 - новый, переменная выступает как ярлык, который ссылается на объект

result = 'hello {}'  # можно через {}
s = result.format(a)
print(s)

# another way
name = 'Perception'
views = 100
onWebsite = '{filmName} + {viewsNumber}'
result = onWebsite.format(filmName = name,viewsNumber = views)
print(result)

# another way
result2 = f'{name} + {views}'
print(result2)
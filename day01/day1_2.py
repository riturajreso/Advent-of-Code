from collections import Counter

lines = open('input.txt').readlines()
pairs = map(str.split, lines)
columns = zip(*pairs)

cast_column = lambda l: map(int, l)
column1, column2 = map(cast_column, columns)

column_2_counts = Counter(column2)

calculate_product = lambda num: num * column_2_counts[num]
products = map(calculate_product, column1)

total = sum(products)
print(total)
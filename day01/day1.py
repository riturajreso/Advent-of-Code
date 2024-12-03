lines = open('input.txt').readlines()

pairs = map(str.split, lines)

columns = zip(*pairs)

sort_ints = lambda l: sorted(map(int, l))
sorted_int_columns = map(sort_ints, columns)

find_distance = lambda a, b: abs(a-b)
distances = map(find_distance, *sorted_int_columns)

total_distance = sum(distances)
print(total_distance)
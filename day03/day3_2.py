import re

with open('input.txt') as f:
  data = ''.join(f.readlines())

exps = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data)
do = True
total = 0
for x1, x2, d1, d2 in exps:
  if x1:
    if do:
      total += int(x1) * int(x2)
  elif d1:
    do = True
  elif d2:
    do = False

print(total)
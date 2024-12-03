def safe(lst):
    return sorted(lst) in [lst, lst[::-1]] \
       and all(1 <= abs(a-b) <= 3 for a, b in zip(lst, lst[1:]))

part1_safe, other_safe = 0, 0
for line in open('input.txt'):
    L = [int(x) for x in line.split()]
    if safe(L):
        part1_safe += 1
    elif any(safe(L[:i] + L[i+1:]) for i in range(len(L))):
        other_safe += 1

print('Part 1 safe:', part1_safe)
print('Part 2 safe:', part1_safe + other_safe)
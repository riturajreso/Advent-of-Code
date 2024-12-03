def safe(lst):
    
    is_ascending = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    is_descending = all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
    if not (is_ascending or is_descending):
        return False

    for i in range(len(lst)-1):
        if not (1 <= abs(lst[i] - lst[i+1]) <= 3):
            return False
    return True

safe_before_removal, safe_after_removal = 0, 0
for line in open('input.txt'):
    L = [int(x) for x in line.split()]
    if safe(L):
        safe_before_removal += 1
    else:
        for i in range(len(lst)):
            modified_lst = lst[:i] + lst[i+1:]
            if is_safe_arrangement(modified_lst):
                safe_after_removal += 1
                break

print('Part 1 safe:', safe_before_removal)
print('Part 2 safe:', safe_before_removal + safe_after_removal)

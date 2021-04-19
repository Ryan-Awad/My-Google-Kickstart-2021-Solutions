# Solution by: Ryan Awad
# Round B
# (5pts, 7pts)

for i in range(int(input())):
    l = int(input())
    s = input().upper()

    substr_len = 1
    substr_list = []

    unicode_values = [ord(x) - 65 for x in s]
    for j in range(len(unicode_values)):
        substr_list.append(substr_len)

        if j != len(unicode_values) - 1:
            condition = unicode_values[j] < unicode_values[j+1]
        else:
            condition = unicode_values[j] > unicode_values[j-1]
            
        if condition:
            substr_len += 1
        else:
            substr_len = 1

    print(f'Case #{i+1}: {" ".join([str(y) for y in substr_list])}')
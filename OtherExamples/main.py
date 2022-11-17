
string = str(input())
result = []
i=0
while i < len(string)-1:
    s = 1
    if string[i] == string[i+1]:
        while i < len(string)-1 and string[i] == string[i+1]:
            i += 1
            s += 1
    result.append((string[i], s))
    if s == 1:
        i += 1
    if s == 1 and i == len(string)-1:
        result.append((string[i], s))
print(result)






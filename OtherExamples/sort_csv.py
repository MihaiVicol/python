import csv

result = {}
with open("test.csv", mode='r') as csv_file:
    csv_dict = csv.DictReader(csv_file, delimiter=',')

    for i in csv_dict:
        for j in i.items():
            if len(result) < len(i)*2-2 and j[0] != 'Year' and j[0] != 'Month':
                result[j[0]] = j[1]
                if (j[0] + 'Year' in result) is False:
                    result[j[0] + 'Year'] = i['Year']
                if (j[0] + 'Month' in result) is False:
                    result[j[0] + 'Month'] = i['Month']
            elif j[0] != 'Year' and j[0] != 'Month':
                if j[1] > result[j[0]]:
                    result[j[0]] = j[1]
                    result[j[0] + 'Year'] = i['Year']
                    result[j[0] + 'Month'] = i['Month']

print(result)



import json

# data = {'today': 9, 'is': 7, 'nice': 8, 'day': 6}
# output = json.dumps(data)
# # output = json.load(data)
# print(output)
# print(type(output))

with open('abc.json', 'r', encoding='utf-8') as f:
    output = json.load(f)
print(output)
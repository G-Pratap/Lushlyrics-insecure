import re

line = "i love cats pet:cat"
var = re.match(r"pet:\w\w\w", line)
# print(var)
# var.group(0)

var = re.search(r"pet:\w\w\w", line)
# print(var)
# print(var.group(0))

line = "pet : cat i love cats pet : cow i love cows"
var = re.findall(r"pet : \w\w\w", line)
print(var)
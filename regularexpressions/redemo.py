import re

# On 'None' method, you cannot invoke group method
str = "Take up one idea. one idea at a time."
str1 = "Take 1 up one 23 idea. one idea 45 at a time."

result1 = re.search(r'o\w\w', str)
print(result1.group())

result2 = re.findall(r'o\w\w', str)
print(result2)

# 'match' only looks at the beginning
result3 = re.match(r'o\w\w', str)
print(result3)

result3 = re.match(r'T\w\w', str)
print(result3.group())

result4 = re.split(r'\d', str1)
print(result4)

result5 = re.sub(r'one', 'two', str)
print(result5)

result6 = re.findall(r'o\w{1, 2}', str)
print(result2)

str2 = "Today's date is 29-12-2019 and tomorrow's date is 30-12-2019."
result7 = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', str2)
print(result7)

result8 = re.search(r'^T\w*', str)
print(result8.group())

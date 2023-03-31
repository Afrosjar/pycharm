def get_data(num):
    return num * 2


data = [1, 2, 3, 4]
f_data = [y for x in data if (y := get_data(x)) != 4]
print(f_data)

lines = ['#11', '22', '33']
if any((comment := line).startswith('#') for line in lines):
    print(comment)

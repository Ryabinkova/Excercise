ids = ['S001', 'S002', 'S003', 'S004']
names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle']
grades = [86, 98, 89, 92]
result= []
s1 = {}
for i, j in zip(names, grades):
    s1.setdefault(i, j)


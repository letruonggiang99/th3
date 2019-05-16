## My script using the math module ##
import mymath # note no .py
values=[2,4,6,8,10]
print('squares:')
for v in values:
    print(mymath.square(v))
print('Cubes:')
for v in values:
    print(mymath.cube(v))
    print('Average: ' + str(mymath.average(values)))

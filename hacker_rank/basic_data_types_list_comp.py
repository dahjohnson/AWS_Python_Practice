x = int(input('Enter x coordinate: '))
y = int(input('Enter y coordinate: '))
z = int(input('Enter z coordinate: '))
n = int(input('Enter n interger: '))

coord = [[i, j, k] (for i in range(x+1)) for j in range(y+1) for k in range(z+1) if (i + j + k != n)]

print(coord)

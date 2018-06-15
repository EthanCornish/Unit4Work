
file = open('results', 'w')

A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
number = '{0}{1}{2}{3}{4}{5}'.format(A,B,C,D,E,F)

while A <= 9:
    number = ('{0}{1}{2}{3}{4}{5}'.format(A, B, C, D, E, F))
    result = ('C@{0}d'.format(number))
    file.write(result)
    file.write('\n')
    while B <= 9:
        number = ('{0}{1}{2}{3}{4}{5}'.format(A, B, C, D, E, F))
        result = ('C@{0}d'.format(number))
        file.write(result)
        file.write('\n')
        while C <= 9:
            number = ('{0}{1}{2}{3}{4}{5}'.format(A, B, C, D, E, F))
            result = ('C@{0}d'.format(number))
            file.write(result)
            file.write('\n')
            while D <= 9:
                number = ('{0}{1}{2}{3}{4}{5}'.format(A, B, C, D, E, F))
                result = ('C@{0}d'.format(number))
                file.write(result)
                file.write('\n')
                while E <= 9:
                    number = ('{0}{1}{2}{3}{4}{5}'.format(A, B, C, D, E, F))
                    result = ('C@{0}d'.format(number))
                    file.write(result)
                    file.write('\n')
                    while F <= 9:
                        number = ('{0}{1}{2}{3}{4}{5}'.format(A, B, C, D, E, F))
                        result = ('C@{0}d'.format(number))
                        file.write(result)
                        file.write('\n')
                        F += 1
                    E += 1
                D +=1
            C += 1
        B += 1
    A+=1

file.close()
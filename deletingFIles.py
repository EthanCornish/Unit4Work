import os

f = open('deletingFiles.txt', 'w')
f.write('I am writing to a file\n')
f.write('Still Going\n')
f.write('Ok that is enough\n')
f.close()
print('Written')

os.remove('deletingFiles.txt.')

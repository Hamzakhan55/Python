f = open('file.txt', 'w')
lines = ['This is line 1\n', 'This is line 2\n', 'This is line 3\n']
f.writelines(lines)
f.close()
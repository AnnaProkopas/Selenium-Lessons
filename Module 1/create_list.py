fin = open('list.txt', 'r')
text = fin.read().split('\n')
print("\\begin{itemize}")
for string in text:
    print('\item \url{' + string + '}')
print("\\end{itemize}")
fin.close()

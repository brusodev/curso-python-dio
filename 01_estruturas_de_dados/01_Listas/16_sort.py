linguagens = ['csharp', 'js', 'python', 'java', 'c']
linguagens.sort()
print(linguagens) # ['c', 'csharp', 'java', 'js', 'python']

linguagens = ['c', 'csharp', 'java', 'js', 'python']
linguagens.sort(reverse=True)
print(linguagens) # ['python', 'js', 'java', 'csharp', 'c']

linguagens = ['csharp', 'js', 'python', 'java', 'c']
linguagens.sort(key=lambda x: len(x))
print(linguagens) # ['c', 'js', 'java', 'csharp', 'python']

linguagens = ['csharp', 'js', 'python', 'java', 'c']
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens) # ['csharp', 'python', 'java', 'js', 'c']


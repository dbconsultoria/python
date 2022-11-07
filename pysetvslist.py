#Listas são tipos de dados padrão do Python que armazenam valores em uma sequência. 
#Sets são outro tipo de dados padrão do Python que também armazena valores. 
#A principal diferença é que sets não podem ter várias ocorrências do mesmo elemento.


# atribuição python set e list

pylist = ['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS','Python','R']
pyset = set(pylist)

print('Lista: ',pylist)
print('Set: ', pyset)

pyset1 = set(['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS','Python','R'])
pyset2 = set(['C', 'Java', 'SQL', 'Bitbucket', 'PowerBI', 'SAS','Python','R'])

#UNION
print('UNION ',pyset1 | pyset2)

#INTERSECTION
print('INTERSECTION ',pyset1 & pyset2)

#DIFFERENCE
print('DIFFERENCE ',pyset1 - pyset2)

with open('template.txt') as file:
    f = file.readlines()
stro = ''.join(f[1:])
stro = stro.replace('\n', '@')
stro = stro[:-1]
stro = stro[7:]
spis = ['Monday(',')@Tuesday(',')@Wednesday(',')@Thursday(',')@Friday(',')@Saturday(',')@Sunday(']
for i in spis:
    stro = stro.replace(i, '#')

print(stro)
spis_rasp = stro.split('#')
print(spis_rasp)
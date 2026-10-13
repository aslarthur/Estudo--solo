lista = {'Nome': 'Arthur', 'Idade': 11, 'Estudando': 'Programação'}
for n, (c, v) in enumerate(lista.items(), start=1):
    print (f"{n}. {c}: {v}")
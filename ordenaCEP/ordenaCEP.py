import struct

lista = []
registroCEP = struct.Struct('72s72s72s72s2s8s2s')

with open('./BuscaCep/cep.dat', 'rb') as f:
    tam_reg = registroCEP.size
    f.seek(0, 2)
    tam_arq = f.tell()
    qtd_reg = tam_arq/tam_reg
    qtd_reg_por_arq = qtd_reg/8
    f.seek(0, 0)

    for i in range(8):
        line = f.read(tam_reg)
        j = 0
        while len(line) > 0 and j <= qtd_reg_por_arq:
            e = registroCEP.unpack(line)
            lista.append(e)
            line = f.read(tam_reg)
            j += 1

        lista.sort(key=lambda e: e[5])

        with open('cep{}.dat' .format(str(i)), 'wb') as fn:
            for e in lista:
                fn.write(registroCEP.pack(*e))
        lista.clear()


primeiro = 0
segundo = 1
final = 8

while final <= 14:
    arq1 = open('cep{}.dat' .format(str(primeiro)), 'rb')
    arq1.seek(0, 2)
    tam_arq1 = arq1.tell()
    qtd_reg_arq1 = tam_arq1/tam_reg
    arq1.seek(0, 0)
    arq2 = open('cep{}.dat' .format(str(segundo)), 'rb')
    arq2.seek(0, 2)
    tam_arq2 = arq2.tell()
    qtd_reg_arq2 = tam_arq2/tam_reg
    arq2.seek(0, 0)
    novo_arq = open('cep{}.dat' .format(str(final)), 'wb')

    l1 = arq1.read(tam_reg)
    l2 = arq2.read(tam_reg)
    x = 0
    y = 0

    while x < qtd_reg_arq1 and y < qtd_reg_arq2:
        if l1 < l2:
            novo_arq.write(l1)
            l1 = arq1.read(tam_reg)
            x += 1
        else:
            novo_arq.write(l2)
            l2 = arq2.read(tam_reg)
            y += 1

    while x <= qtd_reg_arq1:
        novo_arq.write(l1)
        l1 = arq1.read(tam_reg)
        x += 1

    while y <= qtd_reg_arq2:
        novo_arq.write(l2)
        l2 = arq2.read(tam_reg)
        y += 1

    primeiro += 2
    segundo += 2
    final += 1

    arq1.close()
    arq2.close()
    novo_arq.close()

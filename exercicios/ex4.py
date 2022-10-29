def ex4_a():
    seqAtual = 1;
    maiorSeq = 1;
    numeroAnterior = int(input("N: "))
    for i in range(0, 149):
        numeroAtual = int(input("N: "))

        if(numeroAnterior + 1 == numeroAtual):
            seqAtual += 1;
        else:
            seqAtual = 1;

        if(seqAtual > maiorSeq ):
            maiorSeq = seqAtual

        numeroAnterior = numeroAtual

    print("Maior sequência de números crescentes de tamanho = " + str(maiorSeq))

def ex4_b():
    seqAtual = 1;
    maiorSeq = 1;
    numeroAnterior = int(input("N: "))
    for i in range(0, 149):
        numeroAtual = int(input("N: "))

        if(numeroAnterior == numeroAtual):
            seqAtual += 1;
        else:
            seqAtual = 1;

        if(seqAtual > maiorSeq ):
            maiorSeq = seqAtual

        numeroAnterior = numeroAtual

    print("Maior sequencia de números constantes de tamanho = " + str(maiorSeq))

ex4_a()
ex4_b()
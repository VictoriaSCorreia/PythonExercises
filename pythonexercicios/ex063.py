# SEQUÊNCIA DE FIBONACCI (ALGORITMO QUE ME FEZ SOFRER, MAS CONSEGUI SOZINHA)
num = int(input('Digite um número: '))
cont = 3  # printa duas vezes antes do loop e o contador é iniciado primeiro = 3
seq1 = 0  # atribui um valor
seq2 = 1  # atribui um valor
print(seq1, end=' ')
print(seq2, end=' ')
while cont <= num:
    cont = cont + 1
    seq = seq1 + seq2  # inicializa a seq
    seq1 = seq2
    seq2 = seq
    print(seq, end=' ')



n = int(input())

nails = [int(x) for x in input().split()]


"""def count_crossed_lines(i, j, crossed=0):
    # base case
    if i == n-1:
        return crossed
    # recursive loop
    if nails[i] > nails[j]:
        crossed += 1
    j += 1
    if j == n:
        i += 1
        j = i + 1
    return count_crossed_lines(i, j, crossed)
"""


def count_crossed_lines(y, crossed=0):
    print("y=", y, end=" ")
    # base case
    if y == n:
        return crossed
    # recursive loop
    if nails[y-1] > nails[y]:
        crossed += 1
    y += 1
    return count_crossed_lines(y, crossed)


i = total_count = 0
j = 1
while i < n-1:
    i += 1
    total_count += count_crossed_lines(i)
    print()

"""
i = cnt = 0
j = 1
while i < n-1:
    if nails[i] > nails[j]:
        cnt += 1
    j += 1
    if j == n:
        i += 1
        j = i+1
"""
print(total_count)

cnt = 0
for i in range(n):
    cnt += i - nails[i]

print("cnt=", cnt)

ix = 0
for nail in nails:
    print(nail, ix)
    ix += 1


def merge_sort(init, end):
    if init == end
        return 0

    ms = merge_sort(init, (init + end)//2) + merge_sort((init+end)//2 + 1, end)
    sz = 0
    j = (init + end) / 2 + 1

    for i in range(init, (init+end)//2):
        while (j <= end) and (vetor[j] < vetor[i]):
aux[tam]=vetor[j];
tam++;
j++; // passo para o próximo elemento
invers += (ini+fim) / 2-i+1; // e adicino o número de inversões em metades diferentes com o elemento j
}

// adiciono
o
elemento
i
aux[tam] = vetor[i];
tam + +;
}

// adiciono
o
resto
dos
elementosda
segunda
metade
while (j <= fim){

aux[tam]=vetor[j];
tam++;
j++;
}

for (int i=ini; i <= fim; i++) vetor[i]=aux[i-ini]; // e troco os valores do vetor original pelos ordenados

return invers; // retorno
o
número
de
inversões
calculado
}

int
main()
{

scanf("%d", & n); // leio
o
valor
de
n

for (int i=1; i <= n; i++) scanf("%d", & vetor[i]); // leio os valores do vetor

printf("%lld\n", merge_sort(1, n)); // imprimo
a
quantidade
de
inversões
do
vetor

return 0;
}







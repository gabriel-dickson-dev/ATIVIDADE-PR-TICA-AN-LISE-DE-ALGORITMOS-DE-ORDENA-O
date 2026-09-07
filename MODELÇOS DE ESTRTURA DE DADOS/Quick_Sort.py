def quick_sort(vetor):
    comparacoes = 0
    movimentacoes = 0

    def particionar(inicio, fim):
        nonlocal comparacoes, movimentacoes

        pivo = vetor[fim]
        i = inicio - 1

        for j in range(inicio, fim):
            comparacoes += 1

            if vetor[j] <= pivo:
                i += 1

                if i != j:
                    vetor[i], vetor[j] = vetor[j], vetor[i]
                    movimentacoes += 1

        if i + 1 != fim:
            vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]
            movimentacoes += 1

        return i + 1

    def ordenar(inicio, fim):
        if inicio < fim:
            posicao_pivo = particionar(inicio, fim)

            ordenar(inicio, posicao_pivo - 1)
            ordenar(posicao_pivo + 1, fim)

    ordenar(0, len(vetor) - 1)

    return comparacoes, movimentacoes

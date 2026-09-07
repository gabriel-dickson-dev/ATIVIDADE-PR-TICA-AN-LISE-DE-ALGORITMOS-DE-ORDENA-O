import random
from time import perf_counter

# ALGORITMOS DE ORDENAÇÃO

def bubble_sort(vetor):
    comparacoes, trocas = 0, 0
    n = len(vetor)
    
    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            comparacoes += 1
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
                trocas += 1
                trocou = True
        if not trocou:
            break
            
    return comparacoes, trocas


def insertion_sort(vetor):
    comparacoes, movimentacoes = 0, 0
    
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1
        
        while j >= 0:
            comparacoes += 1
            if vetor[j] > chave:
                vetor[j + 1] = vetor[j]
                movimentacoes += 1
                j -= 1
            else:
                break
                
        vetor[j + 1] = chave
        movimentacoes += 1 
      # Inserção final da chave
        
    return comparacoes, movimentacoes


def selection_sort(vetor):
    comparacoes, trocas = 0, 0
    n = len(vetor)
    
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            comparacoes += 1
            if vetor[j] < vetor[menor]:
                menor = j
                
        if menor != i:
            vetor[i], vetor[menor] = vetor[menor], vetor[i]
            trocas += 1
            
    return comparacoes, trocas


def quick_sort(vetor):
    comparacoes, movimentacoes = 0, 0

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


# EXPERIMENTO E RELATÓRIO

def executar_experimento():
    random.seed(42)
    tamanhos = [10, 100, 1000]

    for tamanho in tamanhos:
        original = [random.randint(0, 9999) for _ in range(tamanho)]
        
        # Testando cada algoritmo e medindo tempo (opcional, mas útil)
        algoritmos = {
            "Bubble Sort": bubble_sort,
            "Insertion Sort": insertion_sort,
            "Selection Sort": selection_sort,
            "Quick Sort": quick_sort
        }

        print(f"\n{'='*45}")
        print(f"RELATÓRIO DE DESEMPENHO - TAMANHO N = {tamanho}")
        print(f"{'='*45}")
        print(f"{'Algoritmo':<18} | {'Comparações':<12} | {'Trocas/Movimentações':<20}")
        print("-" * 55)

        for nome, funcao in algoritmos.items():
            copia_vetor = original.copy()
            
            inicio_tempo = perf_counter()
            comp, mov_trocas = funcao(copia_vetor)
            fim_tempo = perf_counter()
            
            print(f"{nome:<18} | {comp:<12} | {mov_trocas:<20}")

if __name__ == "__main__":
    executar_experimento()

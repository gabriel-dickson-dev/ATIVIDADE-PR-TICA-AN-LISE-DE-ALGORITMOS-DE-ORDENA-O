import random

def gerar_vetor(tamanho):
    return [random.randint(0, 9999) for _ in range(tamanho)]

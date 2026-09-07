# Geração de Dados

Nesta etapa são gerados vetores de números aleatórios para os experimentos de ordenação.

São utilizados três tamanhos:

* 10 elementos
* 20 elementos
* 1.000 elementos

Para cada tamanho, é criado um único vetor original e depois são feitas cópias idênticas para cada algoritmo, garantindo que todos recebam os mesmos dados.

```python
original = [random.randint(0, 9999) for _ in range(tamanho)]

vetor_bubble = original.copy()
vetor_insertion = original.copy()
vetor_selection = original.copy()
vetor_quick = original.copy()
```

A biblioteca ***random*** é utilizada para gerar os valores aleatórios.

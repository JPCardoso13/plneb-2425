## Exercício 1 - *reverse_string(s)*
A string é invertida usando **slicing** ([::-1]) e o valor resultante é devolvido.

## Exercício 2 - *count_as(s)*
É criado um **dicionário** para contar os caracteres 'a' e 'A'. A string é percorrida, e os contadores são incrementados
sempre que um desses caracteres é encontrado. O dicionário criado é devolvido pela função após o loop.

## Exercício 3 - *count_vowels(s)*
Define-se uma string com as vogais a procurar (maiúsculas e minúsculas, sem acentos). A string de entrada é percorrida
e um **contador** é incrementado sempre que um caractere coincide com uma vogal. O valor do contador é devolvido após a
conclusão do loop.

## Exercício 4 - *to_lowercase(s)*
Recorre-se ao método **.lower()** de uma string para devolver uma versão em **minúsculas** da string.

## Exercício 5 - *to_uppercase(s)*
Recorre-se ao método **.upper()** de uma string para devolver uma versão em **maiúsculas** da string.

## Exercício 6 - *is_palindrome(s)*
A string é percorrida até à **metade**, sendo comparado cada caractere com o seu correspondente a **contar do fim**. Se
houver uma diferença, é retornado **False**; caso contrário, o loop continua e, se forem concluídas todas as iterações,
é devolvido um valor **True**.

## Exercício 7 - *are_balanced(s1, s2)*
Percorre-se **s1**, sendo verificando se cada um dos seus caracteres está presente em **s2**. Se algum não estiver, é 
retornado **False**. Devolve-se **True** se o loop completar todas as iterações (i.e. se nunca for devolvido False
durante nenhuma das iterações).\
**NOTA**: A versão alternativa com **set(s1).issubset(set(s2)) é mais eficiente no tempo**, pois a verificação em
conjuntos (hash set) tem **tempo de acesso constante**.

## Exercício 8 - *check_occurrences(s1, s2)*
Utiliza o método **.count()** de uma string para verificar as ocorrências de s1 em s2. Se s1 for uma string vazia é
devolvido **0** dado que o método usado devolve o comprimento de s2 se a string submetida for vazia, comportamento
indesejado para este caso.

## Exercício 9 - *is_anagram(s1, s2)*
Começa por invalidar strings de tamanho diferente. Em casos válidos, **mapeia os caracteres de s1 para um contador**,
iterando uma vez sobre s1. Em seguida, percorre-se s2, **verificando se os seus caracteres estão presentes no dicionário
ou se o contador associado a cada um deles é superior a 0**, sendo devolvido **False** caso esta condição se cumpra.
Se esse return não acontecer, o contador associado a esse caractere no mapa é **decrementado**. Se o segundo loop
concluir todas as iterações, a função retorna **True**.\
**NOTA**: Esta abordagem é mais rápida do que a versão alternativa comentada no código, sobretudo para strings
compridas.

## Exercício 10 - *group_anagrams(string_list)*
Cada string da lista recebida é **ordenada alfabeticamente e usada como chave num dicionário**. Se a chave ainda não
existir, cria-se uma entrada com uma lista contendo essa string. Caso contrário, a string é adicionada à lista
correspondente. Deste modo, a função **agrupa as strings de acordo com a sua relação enquanto anagramas**.

## Execução de testes:
O módulo inclui ainda uma função **teste(num_exercise, func, *args)**, que foi usada para imprimir os resultados dos
testes das funções criadas de forma formatada na consola.

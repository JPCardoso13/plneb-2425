# TPC2

## Descrição das funções implementadas:

### Exercício 1.1 - **`starts_with_hello(line)`**:
Determina se uma string começa com a palavra **"hello"** utilizando a função **`match`** do módulo **`re`**. 
Permite correspondências parciais, pois procura **"hello"** sem restringir a palavra completa (**`\bhello\b`**).\
**Exemplo**:
```python
starts_with_hello("hello world")  # Output: True
starts_with_hello("hellow world")  # Output: True
```

### Exercício 1.2 - **`has_hello(line)`**:
Verifica se **"hello"** aparece na string com recurso à função **`search`** do módulo **`re`**. 
Permite correspondências parciais.\
**Exemplo**:
```python
has_hello("hi, hello there")  # Output: True
has_hello("hehelloworld")  # Output: True
```

### Exercício 1.3 - **`find_hellos(line)`**:
Procura todas as ocorrências de **"hello"** na string utilizando **`findall`** do módulo **`re`**. 
Ignora maiúsculas e minúsculas e permite correspondências parciais.\
**Exemplo**:
```python
find_hellos("Hello! hheLLoh, it's me... Heyyy, hello? HELLO!")  # Output: ['Hello', 'heLLo', 'hello', 'HELLO']
```

### Exercício 1.4 - **`replace_hellos(line)`**:
Substitui todas as ocorrências de **"hello"** por **"\*YEP\*"** na string, utilizando **`sub`** do módulo **`re`**. 
Ignora maiúsculas e minúsculas e permite correspondências parciais.\
**Exemplo**:
```python
replace_hellos("HELLO! hhellOw")  # Output: "*YEP*! h*YEP*w"
```

### Exercício 1.5 - **`separate_by_comma(line)`**:
Separa o conteúdo da string por vírgulas recorrendo à função **`split`** do módulo **`re`**. 
Devolve uma lista de substrings resultantes da divisão.\
**Exemplo**:
```python
separate_by_comma("bananas, laranjas, maçãs")  # Output: ['bananas', 'laranjas', 'maçãs']
```

### Exercício 2 - **`palavra_magica(frase)`**:
Determina se uma frase termina exatamente em **"por favor"** seguido de um sinal de pontuação válido: 
regex **(\\?|\.{1,3}|!\\?)$**. Utiliza a função **`search`** do módulo **`re`**.\
**Exemplo**:
```python
palavra_magica("Podes dar-me isso, por favor!?")  # Output: True
palavra_magica("porpor favor!")  # Output: False
```

### Exercício 3 - **`narcissismo(linha)`**:
Conta quantas vezes a palavra **"eu"** aparece na string (ocorrências exatas, com ou sem maiúsculas). 
Utiliza **`findall`** do módulo **`re`** e devolve o comprimento da lista resultante.\
**Exemplo**:
```python
narcissismo("Eu sou EU, mEU deus!")  # Output: 2
```

### Exercício 4 - **`troca_de_curso(linha, novo_curso)`**:
Substitui todas as ocorrências exatas de **"LEI"** na string pelo termo submetido à função. 
Utiliza a função **`sub`** do módulo **`re`**.\
**Exemplo**:
```python
troca_de_curso("É lei ser de LEI!", "biomédica")  # Output: "É lei ser de biomédica!"
```

### Exercício 5 - **`soma_string(linha)`**:
Recebe uma string com números separados por vírgulas e devolve a sua soma, utilizando o **`split`** do módulo **`re`** 
para separar a string.\
**Exemplo**:
```python
soma_string("1,-3,2")  # Output: 0
```

### Exercício 6 - **`pronomes(frase)`**:
Encontra todos os pronomes na frase (ocorrências exatas, com ou sem maiúsculas) através da função **`findall`** do 
módulo **`re`**.\
**Exemplo**:
```python
pronomes("nós somos elEs, mEU")  # Output: ['nós', 'elEs']
```

### Exercício 7 - **`variavel_valida(palavra)`**:
Verifica se uma string começa por uma letra e contém apenas caracteres alfanuméricos e underscores. 
Combina a função **``findall``** do módulo **``re``** com o método **``join``** da classe padrão para strings.\
**Exemplo**:
```python
variavel_valida("var_1")  # Output: True
variavel_valida("variável 1")  # Output: False
```
Em alternativa, a função poderia ser definida como:
```python
def variavel_valida(palavra):
    return True if re.fullmatch(r"[a-zA-Z]\w*", palavra) else False
```

### Exercício 8 - **`inteiros(string)`**:
Devolve os números inteiros, positivos ou negativos, encontrados numa string. Utiliza a função **``findall``** do 
módulo **``re``** e admite que os caracteres na string não têm significado semântico, pelo que dígitos separados por 
vírgulas, pontos ou outros sinais de pontuação são interpretados como números inteiros independentes.\
**Exemplo**:
```python
inteiros("-13 graus é menos que14graus")  # Output: ['-13', '14']
inteiros("3,1 não é inteiro")  # Output: ['3', '1']
```

### Exercício 9 - **`underscores(string)`**:
Substitui todos os espaços numa string por underscores, convertendo vários espaços seguidos num só underscore. 
Recorre ao **`sub`** do módulo **`re`**.\
**Exemplo**:
```python
underscores("  esta string tem  espaços")  # Output: "_esta_string_tem_espaços"
```

### Exercício 10 - **`codigos_postais(lista_codigos)`**:
Itera sobre a lista de códigos postais e utiliza a função **``split``** do módulo **``re``** para separar o conteúdo de 
cada elemento na lista por hífens. Devolve uma lista de tuplos, cada um representando um par separado por hífen.
Exemplo:
```python
codigos_postais(["4750-860", "222-222"])  # Output: [('4750', '860'), ('222', '222')]
```

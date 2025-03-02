# TPC3
## Extração de dados textuais para criação de template HTML
### Objetivo
Este exercício tem como objetivo processar um ficheiro de texto contendo conceitos médicos e as suas respetivas
definições, gerando um ficheiro HTML para visualização formatada dos conteúdos. O exercício está englobado na componente
prática da terceira aula de PLNEB-2025.

### Descrição do Problema
O ficheiro de entrada está estruturado com conceitos médicos seguidos das suas definições e separados destas por
quebras de linha. Cada par conceito-definição é delimitado por uma quebra de linha dupla.
No entanto, o ficheiro contém casos em que os conceitos e definições são separados por quebras de página, o que introduz
quebras de linha adicionais. Como consequência, a abordagem original do exercício (desenvolvida na aula), que marcava
conceitos com o caractere **@** sempre que eram precedidos por duas quebras de linha, falhava em alguns casos,
identificando incorretamente partes das definições como conceitos.

### Solução Proposta
Para resolver este problema, a solução proposta modifica a abordagem inicial de marcação de conceitos. Em vez de
simplesmente adicionar o caractere **@** após cada dupla quebra de linha, **é utilizada uma expressão regular mais
robusta**.

O código original da aula utilizava:
```python
texto = re.sub(r"\n\n", "\n\n@", texto)
```
Sendo substituído pela linha:
```python
texto = re.sub(r"(\n\n)(.*)\n{1,}", r"\1@\2\n", texto)
```
Esta nova abordagem garante que apenas as linhas que representam conceitos são corretamente identificadas, evitando
marcações erradas dentro das definições. A estrutura gerada para o template HTML confirma o sucesso desta resolução.

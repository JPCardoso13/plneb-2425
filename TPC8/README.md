# TPC8
## Web Scraping - Extração de Conteúdos de um Website
### Objetivo
Extrair conteúdos do website "Atlas da Saúde" utilizando a biblioteca Beautiful Soup, estruturando os dados de forma
lógica e organizada no formato JSON.

### Implementação
O processo de web scraping parte do código desenvolvido durante a aula prática, com a adição de novas funções que
permitem uma formatação mais clara e estruturada dos dados extraídos.

A lógica do programa foi dividida em várias partes modulares para facilitar a organização, o controlo do processo de
extração e a construção do output. De forma geral, o processo envolve as seguintes funções:
- ``get_html_content(url)``: Extrai o conteúdo HTML de uma página a partir do URL fornecido, devolvendo-o como uma
string.
- ``get_info_doencas(letra)``: Devolve um dicionário com a informação relativa a todas as doenças cuja inicial
corresponde à letra fornecida.
- ``get_conteudo_doenca(url_doenca)``: Obtém e estrutura os conteúdos de uma doença específica, a partir do seu URL.
- ``format_contents_as_dict(html_content)``: Converte o conteúdo HTML de uma página de doença num dicionário, com base
nos títulos e conteúdos das tags HTML. É usada pela função anterior.
- ``get_last_elems(html_content)``: Função auxiliar que extrai conteúdos fora da estrutura principal da página, como
elementos finais não aninhados.

### Output
O output gerado segue a estrutura semântica do site, organizando os subtemas de cada doença de forma clara. Secções de
texto compostas por elementos como `<p>` ou `<ul>` são representadas como listas, enquanto outras, como os artigos
relacionados, são organizadas em subdicionários.

Exemplo de estrutura do JSON:
````json
{
    "Exemplo de Doença": {
        "URL": "/url-da-doenca",
        "Resumo": "Resumo da doença.",
        "Conteúdo": {
            "Data": "01/01/2015 - 10:10",
            "Descrição": [
                "Primeiro parágrafo. Seguido de bullet points:",
                [
                  "elemento1",
                  "elemento2"
                ],
                "Último parágrafo."
            ],
            "Causas": [
                "Formatação igual ao elemento anterior."
            ],
            "Sintomas": [
                "Formatação igual ao elemento anterior."
            ],
            "Tratamento": [
                "Formatação igual ao elemento anterior."
            ],
            "Artigos relacionados": {
                "Nome do primeiro URL": "https://www.primeiro-url.pt",
                "Nome do segundo URL": "https://www.segundo-url.pt"
            },
            "Site": "Site referenciado.",
            "Fonte": "Fonte referenciada.",
            "Nota": "Conteúdo da nota."
        }
    },
    "Outra Doença": {
        ...
    }
}
````
**Nota**: Nem todas as doenças possuem todos os campos exemplificados acima.

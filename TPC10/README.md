# TPC10  
## Web Scraping — Extração de Conteúdos de um Website

### Objetivo
Extrair conteúdos do website da Revista Portuguesa de Medicina Interna, utilizando a biblioteca **Beautiful Soup**, e
estruturar os dados de forma lógica e organizada no formato **JSON**.

### Implementação
O processo de *web scraping* está dividido em várias etapas, cada uma com uma função dedicada. De forma geral, o
funcionamento pode ser descrito da seguinte maneira:
- `get_html_content(url)`: Obtém o conteúdo HTML da página indicada pelo URL e devolve-o como uma *string*.


- `scrape_data(num_archives)`: Função principal que orquestra o processo de scraping. Devolve um dicionário onde cada
chave corresponde a uma edição da revista e o respetivo valor é um subdicionário com os metadados da revista e os seus
artigos.


- `fetch_archive_data(soup)`: Extrai os dados de um arquivo de edições da revista, devolvendo um dicionário com a mesma
estrutura da função anterior. É usada como auxiliar em `scrape_data`.


- `fetch_newsletter_data(url)`: Extrai os dados de uma edição específica da revista, incluindo todos os seus artigos, e
devolve-os como um dicionário.


- `fetch_article_data(url)`: Recolhe e organiza todos os elementos essenciais de um artigo, como título (e título
traduzido, se existir), data de publicação, URL, DOI, autores, palavras-chave e resumo (*abstract*).

No seu conjunto, o projeto percorre os vários arquivos da revista, extrai os dados de cada edição e, dentro de cada uma,
recolhe os dados de todos os artigos. O resultado final é uma estrutura unificada e coerente, contendo a informação
relevante de todos os artigos disponíveis no site.

### Output
O resultado do programa é um ficheiro JSON com uma estrutura que respeita a organização lógica e semântica do site. O
conteúdo está dividido por volumes da revista, e dentro de cada um, por artigos, com os respetivos metadados.

#### Exemplo de estrutura do JSON:
```json
{
    "Primeiro volume da revista": {
        "URL": "https://url-do-volume",
        "data_publicacao": "2025-01-01",
        "artigos": [
            {
                "URL": "https://url-do-primeiro-artigo",
                "titulo": "Título do artigo",
                "titulo_pt": "Título traduzido (se existir)",
                "data_publicacao": "2025-01-01",
                "autores": [
                    {
                        "nome": "Nome do autor",
                        "afiliacao": "Afiliação do autor",
                        "orcid": "https://orcid.org/xxxx-xxxx"
                    }
                ],
                "DOI": "https://doi.org/xxxxxx",
                "keywords": [
                    "Palavra-chave 1",
                    "Palavra-chave 2"
                ],
                "abstract": [
                    "Parágrafo 1 do resumo",
                    "Parágrafo 2 do resumo"
                ]
            },
            ...
        ]
    },
    "Outro volume da revista": {
        ...
    }
}
```
**Nota**: Apenas os campos existentes são incluídos. Por exemplo, se um artigo não tiver resumo, o campo `abstract` não
aparece no JSON.

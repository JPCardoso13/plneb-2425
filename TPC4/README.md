# TPC4
## Criação de uma Página HTML de tema livre
### Objetivo
O exercício tem como objetivo o desenvolvimento de uma página web em HTML para compreender a forma como estes ficheiros estão estruturados e como os seus conteúdos são apresentados e se relacionam.

### Tema Selecionado e Motivação da Escolha
O tema selecionado foi a apresentação dos cinco melhores golos de Cristiano Ronaldo. A escolha deveu-se ao facto de o tema **permitir explorar elementos HTML diversos, como elementos de multimédia**, através da incorporação de vídeos e áudio com tags como `<iframe>` e `<audio>`.

### Estrutura da Página
Para tornar a página mais dinâmica e atrativa, foram adicionados um ficheiro `style.css` para estilização e um ficheiro `script.js` para interatividade.

A estrutura base da página divide-se em duas partes principais:

1. **Cabeçalho (`<header>`)**

    Este elemento inclui um título principal (`<h1>`), um contador dinâmico (envolvido numa tag `<span>`), um botão de interação e alguns elementos multimédia. O JavaScript incorporado permite reproduzir um ficheiro de áudio e incrementar o contador sempre que um utilizador interage com a página. O contador pode ser reiniciado através do botão incluído no cabeçalho.

2. **Conteúdo Principal (`<main>`)**

    O conteúdo principal da página está organizado em secções (`<section>`), cada uma representando um dos cinco golos de Cristiano Ronaldo. Cada secção inclui:
    - Um título (`<h2>`) com o nome do golo
    - Um `<iframe>` com o vídeo correspondente
    - Uma lista não ordenada (`<ul>`) com informações sobre o golo, como a data e o minuto a que foi marcado
    - Uma descrição detalhada do acontecimento

É seguido o modelo:
```html
<section>
    <h2>NOME</h2>
    <div class="conteudo-golo">
        <iframe src="url-do-golo"></iframe>
        <ul>
            <li><strong>Data:</strong> DATA</li>
            <li><strong>Adversário:</strong> ADV</li>
            <li><strong>Minuto:</strong> MIN</li>
        </ul>
    </div>
    <p class="descricao">DESC</p>
</section>
```

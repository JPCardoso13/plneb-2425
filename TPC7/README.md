# TPC7
## Integração de tabela com o plug-in DataTables do jQuery
### Objetivo
Integrar uma tabela com o plug-in DataTables do jQuery, permitindo **pesquisa com expressões regulares**. Além disso,
adicionar um elemento na navbar para facilitar a navegação até esta tabela.

### Implementação
Foram realizadas alterações no ficheiro ``conceitos.js`` para habilitar a pesquisa por expressões regulares e definir a
linguagem da tabela para português. Ao carregar a página HTML, o seguinte código é executado com jQuery DataTables:
```javascript
$(document).ready(() => {
    $('#tabela_conceitos').DataTable({
        search: {
            regex: true
        },
        language: {
            "url": "https://cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Portuguese.json"
        }
    });
});
```
No template ``tabela.html``, os elementos da tabela foram atualizados para permitir a navegação direta para as páginas
específicas de cada conceito, através de links dinâmicos:
```html
<tr>
    <td><a href="/conceitos/{{ designacao }}" class="list-group-item list-group-item-action">{{ designacao }}</a></td>
    <td><a href="/conceitos/{{ designacao }}" class="list-group-item list-group-item-action">{{ descricao }}</a></td>
</tr>
```

# TPC5
## Criação de Rota para Template HTML em Flask
### Objetivo
Criar uma rota em Flask que permita que elementos de ancoragem (``<a>``) num template HTML, associados a designações de
conceitos num dicionário médico, redirecionem para páginas geradas dinamicamente com a descrição correspondente.

### Descrição da Implementação
A base da implementação é a criação da rota ``conceito/<designacao>`` e do novo template ``conceito.html``, construído
a partir do template ``layout.html``, desenvolvido durante a aula, utilizando Jinja2. No template ``conceitos.html``,
que foi igualmente criado na aula, a linha `{{ designacao }}` é substituída pelo seguinte HTML:
```html
<a href="{{ url_for('conceito', designacao=designacao) }}">{{ designacao }}</a>
```
Isto permite a navegação dinâmica entre os templates, com ``url_for`` a gerar as rotas corretamente a partir da rota
criada para o efeito.

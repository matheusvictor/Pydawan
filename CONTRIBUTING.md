# Contribuindo:

Ao contribuir com este repositório, primeiro discuta a alteração que deseja fazer via issue, e-mail ou qualquer outro método com os proprietários deste repositório antes de fazer uma alteração.

Observe que temos um código de conduta; siga-o em todas as suas interações com o projeto.

## Processo de Pull Request:

- Verifique as [issues](https://github.com/matheusvictor/Pydawan/issues) existentes no repositório;

- Faça um [fork](https://help.github.com/en/articles/fork-a-repo) deste repositório. Ao fazer um fork, é como se fosse criada uma cópia do código-fonte na sua conta, a qual você poderá modificar sem afetar o repositório original;

- [Clone](https://git-scm.com/book/pt-br/v1/Git-Essencial-Obtendo-um-Reposit%C3%B3rio-Git#Clonando-um-Reposit%C3%B3rio-Existente) a cópia do repositório para seu ambiente local. Abra a pasta que contém o arquivo que deseja resolver. Exemplo: a primeira questão da lista01 estará no seguinte caminho: `Pydawan/lista01/l1q01.py`. **Não exclua as linhas de comentário com a questão**, pois outras pessoas podem querer saber o que você resolveu;

- Uma vez solucionada a questão, compile para testá-la antes de solicitar uma [pull-request](https://help.github.com/articles/creating-a-pull-request). Feito isso, [sincronize]() seu repositório com o original e só depois [realize um commit](https://githowto.com/pt-BR/commiting_changes) para seu repositório;

- Posteriomente, solicite uma PR para o repositório [https://github.com/matheusvictor/Pydawan/](https://github.com/matheusvictor/Pydawan/) com o título `resolve #numeroDaIssue`. Exemplo: `resolve #1`;

## Adicionando novas questões a serem resolvidas:

Se vocẽ deseja adicionar novas questões para que outras pessoas possam resolver, siga os seguintes passos:

- Em seu repositório local, escolha uma das pastas de lista e crie o arquivo para a questão;

- O nível da questão deve está de acordo com o nível , de preferência. Assim, questões mais simples devem ficar na [lista01](https://github.com/matheusvictor/Pydawan/tree/master/lista01) e assim sucessivamente. A complexidade da questão pode ser levada em conta a partir de alguns fatores como: número de variáveis utilizadas, quantidade de processamentos a serem feitos até chegar ao resultado final, etc.
    - Se considerar a complexidade para além dos diretórios atuais, crie um diretório especial para abrigar esta questão. Ou seja, se a questão for para além da [lista04](https://github.com/matheusvictor/Pydawan/tree/master/lista04), considere a criação de uma pasta `lista05`, a qual abrigará a questão sugerida, com numeração consecutiva à última. Ou seja, se a última questão for algo como `l5q10.py`, você deverá criar `l5q11.py`.

- Nomeie o arquivo seguindo o seguinte o padrão adotado em arquivos-questões já existentes. Exemplo: `l1q99.py`;

- Feito isso, abra um PR com o commit `cria questão l1q99.py`.

## Corrigindo questões resolvidas:

Caso note algum erro em alguma das questões, ou acredita que pode melhorar o enunciado e/ou a solução existente (se houver), siga os seguintes passos:

- Corrija o enunciado e/ou a resolução da questão e abra uma PR com o commit `corrige questão l1q05.py`, por exemplo;

- Ou, se preferir, abra uma issue com o título `Corrigir questão lNqXX.py`, para identificar qual questão deve ser corrigida. Por exemplo: `Corrigir questão l1q05.py`. Na descrição da issue, descreva detalhe o problema o quanto for possível.

## Materiais auxiliares:

### Editores de texto & IDEs:

Os materiais abaixo podem te ajudar a escrever e/ou compilar seu(s) código(s) Python:

- Editor(es) de texto: [Visual Code](https://code.visualstudio.com/Download), [Atom](https://atom.io/), [Sublime](https://www.sublimetext.com/3);
- Editor(es) online: [Repl.it](https://repl.it/);
- [PyCharm](http://www.jetbrains.com/pycharm/).

### Comandos Git:

Se você também está iniciando com Git, segue abaixo uma pequena lista de materiais que podem te ajudar:

- [Git Book](https://git-scm.com/book/pt-br/v2);
- O [Gitexplorer](https://gitexplorer.com/) também poderá ser útil se tiver procurando pela sintaxe de comandos git.
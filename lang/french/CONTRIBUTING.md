# Contribuer

<p align="center">
  <span>Français</span> |
  <a href="https://github.com/matheusvictor/Pydawan#contribuindo">Portuguese</a>
</p>

Lorsque vous contribuez à ce dépôt, discutez d'abord du changement que vous souhaitez effectuer par issue, e-mail ou toute autre méthode avec les propriétaires de ce dépôt avant de faire un changement.

Notez que nous avons un code de conduite ; suivez-le dans toutes vos interactions avec le projet.

## Processus de Pull Request:

- Vérifiez les [issues](https://github.com/matheusvictor/Pydawan/issues) existentes dans le dépôt ;

- Faite un [fork](https://help.github.com/en/articles/fork-a-repo) du dépôt. Lors du fork, c'est comme si vous créiez une copie du code source dans votre compte, que vous pouvez modifier sans affecter le référentiel d'origine ;

- [Clonez](https://git-scm.com/book/pt-br/v1/Git-Essencial-Obtendo-um-Reposit%C3%B3rio-Git#Clonando-um-Reposit%C3%B3rio-Existente) la copie du dépôt dans votre environnement local. Ouvrez le dossier contenant le fichier que vous voulez corriger. Exemple : la première question de la lista01 sera dans le chemin suivant : `Pydawan/lista01_fr-BR/l1q01.py`. **Ne supprimez pas les lignes de commentaire avec la question**, car d'autres personnes pourraient vouloir savoir ce que vous avez résolu. **Les commentaires sont également importants**, alors essayez de commenter votre code chaque fois que c'est possible afin que les autres puissent en tirer des leçons ;

- Une fois le problème résolu, compilez pour le tester votre solutions avant de demander une [pull-request](https://help.github.com/articles/creating-a-pull-request). Après cela,[synchronisez](https://git-scm.com/book/pt-br/v1/Git-Essencial-Trabalhando-com-Remotos#Fazendo-o-Fetch-e-Pull-de-Seus-Remotos) votre référentiel vers l'original et seulement ensuite [faire un commit](https://githowto.com/pt-BR/commiting_changes) vers votre dépôt ;

- Posteriomente, solicite uma PR para o repositório [https://github.com/matheusvictor/Pydawan/](https://github.com/matheusvictor/Pydawan/) com o título `resolve #numeroDaIssue`. Exemplo: `resolve #1`;

- Enfin, demandez une PR pour le dépôt [https://github.com/matheusvictor/Pydawan/](https://github.com/matheusvictor/Pydawan/) avec le titre `resolve #numeroDeLIssue`. Exemple : `resolve #1` ;

#### **P.s. : les questions doivent être résolues en utilisant des fonctionnalités compatibles avec Python version 3.7.4 ou inférieure.**

## Ajout de nouvelles questions à résoudre

Si vous voulez ajouter de nouvelles questions à faire résoudre par d'autres personnes, suivez ces étapes :

- Dans votre dépôt local, choisissez un des dossiers de la liste et créez le fichier pour la question ;

- Le niveau de la question doit être conforme au niveau du fichier, de préférence. Ainsi, des questions plus simples devraient se trouver dans la [lista01](https://github.com/matheusvictor/Pydawan/tree/master/lista01) et ainsi de suite. La complexité de la question peut être prise en compte à partir de certains facteurs tels que : le nombre de variables utilisées, la quantité de traitement à effectuer pour atteindre le résultat final, etc.

- Si vous considérez la complexité au-delà des dossiers actuels, créez un dossier spécial pour cette question. C'est-à-dire, si la question va au-delà de la [lista04_fr-BR](https://github.com/matheusvictor/Pydawan/tree/master/lista04), pensez à créer un dossier `05_fr-BR`, qui contiendra la question suggérée, avec la numérotation correspondant de la dernière. C'est-à-dire : si la dernière question est `l5q10.py`, vous devriez créer `l5q11.py`.

- Nommez le fichier en suivant le modèle adopté dans les fichiers précédents. Exemple : `l1q99.py` ;

- Ensuite, ouvrez une PR avec comme messade de commit `cria questão l1q99.py`.

## Corriger les problèmes résolus :

Si vous remarquez une erreur dans l'une ou l'autre des questions, ou si vous croyez que vous pouvez améliorer l'énoncé ou la solution existante (le cas échéant), suivez ces étapes :

- Corrigez l'énoncé et/ou la résolution de la question et ouvrez une PR avec comme message de commit `corrige questão l1q05.py` par exemple ;

- Ou, si vous préférez, [ouvrez une issue](https://help.github.com/en/articles/creating-an-issue) avec le titre `Corrigir questão lNqXX.py`, pour identifier la question à corriger. Par exemple : `Corrigir questão l1q05.py`. Dans la description de la question, décrivez le problème en détail autant que possible.

## Traductions :

Vous pouvez également contribuer à ce dépôt en traduisant les questions dans d'autres langues, de préférence votre langue maternelle ou une autre langue que vous maîtrisez. Si par hasard il n'y a pas eu une liste d'exercices avec la langue que vous recherchez, créez-les en suivant le même modèle que ceux qui existent déjà ou ouvrez une issue !

`Ce sujet est encore en développement !`

## Ouvrir de nouvelles issues

Si vous avez remarqué quelque chose qui ne va pas avec l'une des solutions, l'énonciation ou la traduction, vous pouvez le signaler à partir d'une nouvelle issue. Mais avant de le faire, vérifiez soigneusement si quelqu'un d'autre n'a pas déjà signalé ce problème, afin d'éviter les duplicats.

`Ce sujet est encore en développement !`


## Indication de nouveaux documents d'accompagnement à l'apprentissage :

Vous pouvez également nous aider en nous indiquant du matériel d'accompagnement (de préférence gratuit).

`Ce sujet est encore en développement !`

# Matériels auxiliaires :

## Éditeurs de texte et IDE :

Le matériel ci-dessous peut vous aider à écrire et/ou compiler votre code Python :

- Editeurs de texte : [Visual Code](https://code.visualstudio.com/Download), [Atom](https://atom.io/), [Sublime](https://www.sublimetext.com/3);
- Editeurs en ligne : [Repl.it](https://repl.it/);
- [PyCharm](http://www.jetbrains.com/pycharm/).

## Commandes Git:

Si vous commencez aussi avec Git, voici une courte liste de matériel qui peut vous aider :

- [Git Book](https://git-scm.com/book/pt-br/v2) ;
- [Gitexplorer](https://gitexplorer.com/) peut être utile si vous recherchez la syntaxe de la commande git ;
- [Démystifier Git](https://speakerdeck.com/icarojerry/desmistificando-o-git).

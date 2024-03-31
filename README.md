# Repositorio_Inicial_Git
Repositório criado para estudar git, aulas iniciais da DIO

## Comandos git

1. git init 
    - Inicia um novo repositório git na pasta atual

2. git clone [URL]
    - Clona um repositório git existente para a pasta atual

3. git add . 
    - Adiciona as alterações e prepara para o commit.

4. git commit -m "escreve algo sobre"
    - Realiza um commit com as alterações com a descrição

5. git status
    - exibe o estado atual do repositório, mostra os arquivos modificados.

6. git log
    - mostra o histório de commit

7. git branch
    - lista as branchs locais e destaca a atual

8. git branch [nome da branch]
    - cria uma branch

9. git checkout [nome da branch]
    - altera pra essa branch

10. git merge [branch]
    - combina as alterações de uma branch com a branch atual

11. git pull
    - atualiza as alterações do repositório atual com o remoto

12. git remote -v
    - Lista os repositórios remotos

13. git fetch
    - recupera as últimas alterações do repositório remoto

14. git reset [arquivo]
    - desfaz as alterações no arquivo, remove do índice

15. git rm [arquivo]
    - Remove um arquivo da pasta atual e inclui no próximo commit

16. git diff
    - Mostra as diferenças entre as alterações que ainda não foram adicionadas ao índice

17. git remote add [nome-remoto] [URL]
    - adiciona um repositório remoto 

18. git push origin main
    - Efetua um push com as alterações locais para o repositório online (github)

19. git tag -a [nome_da_tag] -m [escreve_uma_msg]
    - Cria um 'backup' de versão atual, serve pra se eu fizer modificação grande e der ruim eu posso voltar pra uma versao boa

# Conceitos

1. Fork
    - Serve pra tu "clonar" o repositório de alguém, depois tu manda um pull request pra pessoa informando oq alterou, se ela quiser aceitar aceita.
    - Pode ser pra fazer uma melhoria em um código aberto

2. Tag
    - Cria uma versão completa do código, coisa grande.
    - git tag -a [escreve_nome_que_quiser] -m "da o teu papo"

3. Realese
    - cria uma versão do código mais detalhada, ex atualizações.

4. Gist
    - Trecho de código, parece um repositório mas bem menor.

5. Issue  
    - Serve para surgerir alterações, correção de bugs, etc. 
    - Da pra botar imagem pra explicar melhor, definir quem vai resolver isso, botar uma tag pra organizar melhor, etc.
    - Da pra criar o arquivo e dps de commitado tu altera o nome e bota 'fixed [tag]' ex.  'fixed #3'.

6. Wikis
    - Documenta de forma mais organizada e profissional, NÃO é um readme.
    - As wikis funcionam detalhar cada etapa do projeto, testes, atualizações, correção de bugs, etc.

# Prática

## Fazendo coisa local 

### Upar coisa no github
git add. 

git status

git commit -m "escreve o papo"

git push origin [a branch que tu quer]

### Puxar coisa do github
'git pull' pra atualizar oq tu já tem

'git clone [URL]' pra tu pegar um negócio do 0 e criar a pasta

# Markdown

## Cabeçalhos


1. '# Título'
2. '## Subtítulo'
3. '### descrição'
4. '#### descrição 2'
5. '##### descrição 3'
6. '###### descrição 4'


## Formatação de frase/palavra

*italico* ou __italico__

**negrito** ou __negrito__

___italico e negrito___ 

## Formatação de texto

- Lista 1
- Lista 2
    - Sublista

1. Lista 1
2. Lista 2
    1. Sublista

## Links e imagem

1. [Texto da imagem](https://foundations.projectpythia.org/_images/GitHub-logo.png)

2. ![Texto da imagem, vai mostrar a imagem aqui](https://foundations.projectpythia.org/_images/GitHub-logo.png)
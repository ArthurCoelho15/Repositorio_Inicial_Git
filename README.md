# Repositorio_Inicial_Git
Repositório criado para estudar git, aulas iniciais da DIO

// Comandos git

'git init' 
    Inicia um novo repositório git na pasta atual
git clone [URL]
    Clona um repositório git existente para a pasta atual
'git add .' 
    Adiciona as alterações e prepara para o commit.
'git commit -m "escreve algo sobre"'
    Realiza um commit com as alterações com a descrição
'git status'
    exibe o estado atual do repositório, mostra os arquivos modificados.
'git log'
    mostra o histório de commit
'git branch'
    lista as branchs locais e destaca a atual
'git branch [nome da branch]'
    cria uma branch
'git checkout [nome da branch]'
    altera pra essa branch
'git merge [branch]'
    combina as alterações de uma branch com a branch atual
'git pull'
    atualiza as alterações do repositório atual com o remoto
'git remote -v'
    Lista os repositórios remotos
'git fetch'
    recupera as últimas alterações do repositório remoto
'git reset [arquivo]'
    desfaz as alterações no arquivo, remove do índice
'git rm [arquivo]'
    Remove um arquivo da pasta atual e inclui no próximo commit
'git diff'
    Mostra as diferenças entre as alterações que ainda não foram adicionadas ao índice
'git remote add [nome-remoto] [URL]'
    adiciona um repositório remoto 
'git push add origin main'
    Efetua um push com as alterações locais para o repositório online (github)
'git tag -a [nome_da_tag] -m [escreve_uma_msg]
    Cria um 'backup' de versão atual, serve pra se eu fizer modificação grande e der ruim eu posso voltar pra uma versao boa

# Conceitos

Fork = serve pra tu "clonar" o repositório de alguém, depois tu manda um pull request pra pessoa informando oq alterou, se ela quiser aceitar aceita.
Pode ser pra fazer uma melhoria em um código aberto

Tag = cria uma versão completa do código, coisa grande.
git tag -a [escreve_nome_que_quiser] -m "da o teu papo"

Realese = cria uma versão do código mais detalhada, ex atualizações.

Gist = Trecho de código, parece um repositório mas bem menor.

# Prática

// Fazendo coisa local 

git add. 
git status
git commit -m "escreve o papo"
git push origin [a branch que tu quer]


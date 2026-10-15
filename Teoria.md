### ARQUITETURA DE PROJETO 

projeto/
├── db/
│   ├── __init__.py
│   └── models.py
├── services/
│   ├── __init__.py
│   ├── movie.py
│   ├── cinema_hall.py
│   └── movie_session.py
└── manage.py

É uma estrutura de projeto Django simples! 🐍

db/ — app com os models (tabelas do banco)
services/ — pacote com funções de consulta (queries) para cada model
manage.py — comando Django para rodar o projeto

É bem comum em projetos Django separar a lógica de banco (models) da
lógica de negócio (services).
Assim seus arquivos ficam organizados e fáceis de manter!


#### Services
Services são funções reutilizáveis de consulta ao banco
— como uma "API" interna do seu código.
Exemplo: get_movies(), create_movie(), etc.
Você usa elas em vários lugares do seu código.

#### main.py
main.py (ou scripts) são usados para tarefas pontuais
— como popular o banco uma vez, rodar migrações, carregar fixtures, etc.
É algo que você executa e pronto

Neste projeto, o comando python manage.py loaddata cinema_db_data.json que
a tarefa menciona já faz o trabalho de preencher o banco com dados de teste.
Não é necessário criar um main.py pra isso.



### Comandos para usar no Terminal
#### Criar as tabelas no banco
python manage.py makemigrations
python manage.py migrate
#### Carregar dados de teste
python manage.py loaddata cinema_db_data.json
#### Testar no shell
python manage.py shell



### manage.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
Define qual arquivo de configurações o Django deve usar — neste caso, settings.py.

if __name__ == "__main__":
Garante que o código só executa quando você roda o arquivo diretamente (não quando é importado).

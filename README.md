<h1>PROJETO SPACE</h1>

<p>O projeto, adaptado do curso de Django da Alura, apresenta imagens de estrelas, galáxias, nebulosas e planetas capturadas por satélites da NASA.</p>
<p>O usuário pode selecionar as imagens desejadas através de um campo de buscas, clicando em uma categoria ou simplesmente clicando na imagem a partir da listagem.</p>

<br>

<h3>🎯 Objetivos do Projeto</h3>

<p>O projeto foi criado para desenvolver habilidades no uso do framework Django/ Python. Trabalho há anos com Laravel/ PHP e posso afirmar algumas coisas:</p>
<ul>
    <li>Conhecer um novo framework é muito melhor do que conhecer o seu primeiro framework. O uso do Laravel derrubou e muito a curva de aprendizado em Django.</li>
    <li><strong>Django</strong> nativo não implementa tantos recursos quanto o Laravel (e não é tão pesado), mas é uma ferramenta mais simples de utilizar e é sensivelmente mais produtiva.</li>
    <li>Jinja tem recursos similares ao Blade, mas as extensões disponíveis no VSCode deixam um pouco a desejar. Para aumentar a produtividade, é bom desenvolver seus próprios snippets.</li>
    <li>O MVT do Django é um MVC com outros nomes. As models são models, as views são os controllers e as templates são as views em frameworks normais rsss.</li>
    <li>As paths do Django são mais simples e organizadas do que as routes do Laravel.</li>
    <li>No geral, a primeira vista, tenho a impressão de que produtividade tende a ser sensivelmente maior com Django do que com Laravel.</li>
    <li>Ainda não estudei/ implementei um Saas usando Django. Assim que fizer algo nesse sentido volto aqui para compartilhar minhas impressões.</li>
</ul>

<br>

<h3>🦋 Sobre o Design</h3>

<p>No início do treinamento, o projeto pareceu super bem estruturado, mas conforme as coisas foram avançando, percebi que alguns erros impactaram sensívelmente a construção de uma interface <strong>correta</strong>.</p>
<p>O projeto não implementava bootstrap, mas quando alguns formulários passaram a ser implementados, novos cabeçalhos html5 foram implementados junto com as novas páginas.</p>
<p>Ao tentar corrigir o problema refatorando os códigos surgiram vários conflitos... Enfim, implementei alguns ajustes mas não ficou satisfatório, principalmente quando requisita os formulários de cadastro e edição.</p>

<br>

<h3>✨ Get Started</h3>

<p>Siga esses passos para configurar e executar o projeto Django localmente:</p><br>

<strong>PRÉ-REQUISITOS:</strong><br>
Antes de começar, certifique-se de ter o Python 3 instalado em sua máquina.
<br><br>

<strong>1o.</strong> Clonar o repositório e acessar o diretório raiz:

```bash
git clone https://github.com/eanicomaco/space-python-django.git

cd space-python-django
```

<br>

<strong>2o.</strong> Criar e acessar o Ambiente Virtual (venv):

```bash
python -m venv venv

# acessar o ambiente no windows
venv\Scripts\activate

# acessar o ambiente no linux ou mac
source venv/bin/activate
```

<br>

<strong>3o.</strong> Instalar as dependências do projeto:

```bash
pip install -r requirements.txt
```

<br>

<strong>4o.</strong> Configurar o Banco de Dados (SQLight3):

```bash
python manage.py makemigrations
python manage.py migrate
```

<br>

<strong>5o.</strong> Rodar o servidor de desenvolvimento:

```bash
python manage.py runserver
```

<p>Após esses passsos, abrir o navegador e acessar http://127.0.0.1:8000 para ver a aplicação em funcionamento.<p>

<br>

<h3>🛠️ Ferramentas utilizadas</h3>
<ul>
    <li>Python 3.12.3</li>
    <li>Django</li>
    <li>SQLite3</li>
    <li>HTML/ CSS</li>
    <li>Affinity Design</li>
</ul>
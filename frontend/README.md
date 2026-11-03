# EV Monitor — Frontend

Interface web do **EV Monitor**, plataforma para monitorar e comparar a autonomia e a eficiência (km/kWh) de veículos elétricos. Projeto da disciplina UPX III (Facens).

O frontend é um único arquivo, `index.html`, em HTML, CSS e JavaScript puros. Ele conversa com a API REST do backend Django (autenticação JWT) e usa o Chart.js, carregado por CDN, para os gráficos. Não precisa de Node, npm nem build.

## O que o sistema faz

| Tela | Funcionalidade |
|---|---|
| **Login** | Autenticação com usuário e senha (JWT) |
| **Visão geral** | Totais (veículos, lançamentos, km rodados), veículo mais eficiente e gráfico de km/kWh |
| **Veículos** | Cadastro, listagem e exclusão de veículos (marca, modelo, ano, capacidade da bateria em kWh) |
| **Lançamentos** | CRUD de uso: km rodados e nível de bateria (%), com histórico editável e eficiência calculada |
| **Comparador** | Gráfico e tabela comparando a eficiência (km/kWh) entre os modelos |

## Pré-requisitos

- Python 3 e Git
- MySQL 8 instalado, com um banco criado (o projeto usa o banco `mydb`)
- Um navegador moderno (Chrome, Edge, Brave ou Firefox)
- Conexão com a internet (o Chart.js é carregado por CDN)

## Como rodar

### 1. Clonar o repositório

```powershell
git clone https://github.com/victorakimoto/monitoramento-veiculos-eletricos
cd monitoramento-veiculos-eletricos
```

### 2. Subir o backend

```powershell
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Crie o arquivo `.env` dentro de `backend` com as credenciais do seu MySQL (esse arquivo não vai para o GitHub). Os nomes das variáveis são os que o `settings.py` lê com o `python-decouple`.

Depois aplique as migrations, crie um usuário e inicie o servidor:

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

O terminal deve mostrar `Starting development server at http://127.0.0.1:8000/`. **Deixe esse terminal aberto** enquanto usa o sistema. Se fechá-lo, a API para.

> Se aparecer `No module named 'django'`, o ambiente virtual não está ativado. Rode `venv\Scripts\activate` de novo (o prompt deve mostrar `(venv)`).

### 3. Abrir o frontend

Abra o arquivo `frontend/index.html` no navegador (clique duas vezes nele). Entre com o usuário e a senha criados no `createsuperuser`.

O campo **API** no rodapé do login vem como `http://127.0.0.1:8000`. Só altere se o backend estiver em outro endereço ou porta.

## Como usar

1. **Cadastre um veículo** na aba *Veículos*: marca, modelo, ano e capacidade da bateria em kWh.
2. **Registre o uso** na aba *Lançamentos*: escolha o veículo, informe os km rodados e o nível de bateria (%) e clique em **Salvar**. A data é preenchida automaticamente.
3. **Edite ou exclua** um lançamento pelos botões da linha do histórico.
4. **Compare os modelos** na aba *Comparador*. A eficiência (km/kWh) de cada veículo aparece no gráfico e na tabela.
5. Use **Sair** para encerrar a sessão.

A eficiência exibida em cada linha do histórico é calculada no frontend: `km ÷ (capacidade da bateria em kWh × nível da bateria % ÷ 100)`. O valor do Comparador vem direto da API.

## Endpoints usados

| Método | Rota | Uso |
|---|---|---|
| POST | `/api/login/` | Login, retorna os tokens JWT |
| GET, POST | `/api/veiculos/` | Listar e cadastrar veículos |
| DELETE | `/api/veiculos/{id}/` | Excluir veículo |
| GET, POST | `/api/lancamentos/` | Listar e criar lançamentos |
| PUT, DELETE | `/api/lancamentos/{id}/` | Editar e excluir lançamento |
| GET | `/api/comparador/` | Eficiência por veículo |

Todas as rotas, exceto o login, exigem o cabeçalho `Authorization: Bearer <token>`. O frontend cuida disso sozinho.

## Configuração

No início do `<script>` do `index.html` existe um bloco `CONFIG` com os endpoints (`EP`) e os nomes dos campos da API (`F`). Se um campo do backend mudar de nome, é só ajustar ali.

O backend precisa permitir chamadas do navegador (CORS). No `settings.py`:

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # primeiro da lista
    # ...
]
CORS_ALLOW_ALL_ORIGINS = True  # apenas para desenvolvimento
```

## Problemas comuns

| Sintoma | Causa e solução |
|---|---|
| "Não foi possível conectar à API" | O servidor não está rodando ou o CORS não está configurado. Confira o terminal do `runserver` e o `settings.py` |
| `can't open file '...manage.py'` | O terminal está na pasta errada. Entre em `backend` antes |
| `No module named 'django'` | Ative o ambiente virtual com `venv\Scripts\activate` |
| Login recusado | Usuário ou senha incorretos. Crie outro com `python manage.py createsuperuser` |
| Sessão expirada | O token venceu. Entre novamente |
| Tela sem dados | Cadastre pelo menos um veículo e um lançamento |
| Bloqueio no Brave | Desative os Shields para o arquivo (ícone do leão na barra de endereço) |

## Estrutura

```
monitoramento-veiculos-eletricos/
├── backend/     API Django + Django REST Framework + MySQL
└── frontend/
    ├── index.html   Interface completa
    └── README.md    Este arquivo
```

## Equipe

- Kaike Rafael Figueiredo (RA 248984)
- Victor Akimoto Ferreira (RA 264396)
- Willas Cavalheiro Araujo Lacerda (RA 252433)

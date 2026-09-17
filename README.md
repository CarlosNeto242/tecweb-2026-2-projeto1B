**Link do site em deploy**: https://tecweb-2026-2-projeto1b-fg29.onrender.com/

## 🚀 Como rodar o projeto localmente

### 1. Clone o repositório

bash
git clone https://github.com/CarlosNeto242/tecweb-2026-2-projeto1B.git
cd tecweb-2026-2-projeto1B


### 2. Crie um ambiente virtual

bash
python -m venv venv


### 3. Ative o ambiente virtual

No *PowerShell*:

powershell
.\venv\Scripts\Activate.ps1


> Quando o ambiente estiver ativo, (venv) deverá aparecer no início da linha do terminal.

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Prepare o banco de dados

Crie as migrações:

```bash
python manage.py makemigrations
```

Aplique as migrações:

```bash
python manage.py migrate
```

> Sempre que houver alterações nos models.py, execute novamente makemigrations e migrate.

### 6. Rode o servidor

```bash
python manage.py runserver
```

Acesse o projeto pelo navegador em:

text
http://127.0.0.1:8000/


Para parar o servidor, pressione Ctrl + C.

### 🔄 Resumo

Depois da configuração inicial, o fluxo básico para rodar o projeto é:

powershell
.\venv\Scripts\Activate.ps1
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
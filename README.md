# Django Tutorial

Este projeto faz parte do **Curso de Desenvolvimento em Python**, com foco na criação de aplicações web com Django.

Este projeto é um tutorial prático de como construir aplicações com o framework **Django** em Python. Ele cobre conceitos fundamentais como criação de modelos, rotas, views, templates, formulários e painel administrativo.
## 🚀 Funcionalidades

- Sistema de gerenciamento de contatos
- Integração com Django Admin
- CRUD completo com formulários
- Templates com HTML e Django Template Language
- Validação e rotas nomeadas

## 🧱 Estrutura do Projeto

```
Django-Tutorial/
├── contact/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── templates/
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── django_tutorial/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── db.sqlite3
```

## ⚙️ Requisitos

- Python 3.8+
- Pip
- Virtualenv (opcional, mas recomendado)

## 📦 Instalação

```bash
# Clone o repositório
git clone https://github.com/PBreno/Django-Tutorial.git
cd Django-Tutorial

# Crie um ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Crie um superusuário para acessar o Django Admin
python manage.py createsuperuser

# Inicie o servidor
python manage.py runserver
```

Acesse a aplicação em: [http://localhost:8000](http://localhost:8000)

Admin: [http://localhost:8000/admin](http://localhost:8000/admin)

## 🛠️ Comandos úteis

```bash
# Criar novas migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Rodar o servidor
python manage.py runserver
```

## ✍️ Autor

Desenvolvido por [PBreno](https://github.com/PBreno)

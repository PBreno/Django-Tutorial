FROM python:3.12-slim

# Define diretório de trabalho
WORKDIR /var/www

# Copia os arquivos da aplicação
COPY ../src/public .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta padrão (caso use Django, geralmente 8000)
EXPOSE 8000

# Comando padrão (pode ser ajustado para Flask, FastAPI ou outro)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

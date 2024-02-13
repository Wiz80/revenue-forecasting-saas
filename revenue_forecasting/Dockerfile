# Usar una imagen base oficial de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar dependencias de sistema para PostgreSQL
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Copiar el archivo de requisitos primero para aprovechar la caché de Docker
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . /app/

# Recolectar archivos estáticos
RUN python manage.py collectstatic --no-input

# Comando para ejecutar la aplicación
CMD ["gunicorn", "-b", "0.0.0.0:8000", "revenue_forecasting.wsgi:application"]

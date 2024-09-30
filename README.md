Цель: Создать ETL-пайплайн для обработки данных о продажах из CSV-файлов, очистки данных и загрузки их в реляционную базу данных для последующего анализа.

Постановка задачи
- Extract: Извлечь данные о продажах из файлов формата CSV, которые поступают ежедневно.
- Transform: Очистить данные, преобразовать их в нужный формат и провести агрегацию (например, подсчет общего дохода, количества продаж по каждому товару).
- Load: Загрузить обработанные данные в PostgreSQL для хранения и аналитики.

Выбор инструментов
- Язык программирования: Python (с библиотеками Pandas для обработки данных)
- Хранилище данных: PostgreSQL
- ETL-оркестратор: Apache Airflow для автоматизации
- Файлы данных: CSV-файлы с данными о продажах
- Обработка данных: Pandas для трансформации и обработки данных
- Инфраструктура (опционально): Docker для контейнеризации

Настройка среды
1. Установка PostgreSQL:
   - Установи PostgreSQL на локальной машине или используй облачное решение
   - Создать базу данных sales_db и таблицу для хранения данных о продажах:
  CREATE TABLE sales_data (
    id SERIAL PRIMARY KEY,
    order_id VARCHAR(50),
    customer_id VARCHAR(50),
    product_id VARCHAR(50),
    quantity INT,
    price NUMERIC(10, 2),
    total_price NUMERIC(10, 2),
    sale_date DATE
);

2. Установка Python и необходимых библиотек: Установи Python и библиотеки для обработки данных:
   -> pip install pandas sqlalchemy psycopg2 airflow
     
3. Установка и настройка Apache Airflow:
   -> pip install apache-airflow


from sqlalchemy import create_engine, MetaData, Table, select, delete

engine = create_engine("mysql+pymysql://bn_opencart:@localhost:3306/bitnami_opencart")

metadata = MetaData()
customer_table = Table("oc_customer", metadata, autoload_with=engine)

def select_users_info():
    with engine.connect() as conn:
        result = conn.execute(select(customer_table).limit(10))
        for row in result.mappings():  # <-- возвращает dict-подобные строки
            print(dict(row))           # <-- теперь это безопасно

def delete_user_by_email(email: str):
    with engine.begin() as conn:
        stmt = delete(customer_table).where(customer_table.c.email == email)
        result = conn.execute(stmt)
        print(f"Удалено пользователей: {result.rowcount}")

# Пример вызова
select_users_info()

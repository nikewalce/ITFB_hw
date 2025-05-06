from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker

# Подключение к базе данных OpenCart с использованием SQLAlchemy
DATABASE_URL = 'mysql+mysqlconnector://username:password@localhost/opencart_db'

# Создание подключения и сессии
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def delete_user_from_opencart(user_id):
    # Загружаем метаданные
    metadata = MetaData()

    # Определяем таблицы
    oc_customer = Table('oc_customer', metadata, autoload_with=engine)
    oc_address = Table('oc_address', metadata, autoload_with=engine)
    oc_customer_group = Table('oc_customer_group', metadata, autoload_with=engine)

    try:
        # Удаляем пользователя из таблицы oc_customer
        session.execute(oc_customer.delete().where(oc_customer.c.customer_id == user_id))

        # Удаляем связанные адреса из таблицы oc_address
        session.execute(oc_address.delete().where(oc_address.c.customer_id == user_id))

        # Удаляем группы пользователя из таблицы oc_customer_group
        session.execute(oc_customer_group.delete().where(oc_customer_group.c.customer_id == user_id))

        # Фиксируем изменения
        session.commit()

        print(f"User with ID {user_id} has been successfully deleted.")

    except Exception as e:
        print(f"Error: {e}")
        session.rollback()

    finally:
        # Закрываем сессию
        session.close()


# Вызов функции с ID пользователя
delete_user_from_opencart(123)  # Замените 123 на нужный ID пользователя

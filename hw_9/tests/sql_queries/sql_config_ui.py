from sqlalchemy import create_engine, MetaData, Table, insert, update, select, func, delete
from datetime import datetime
import random
import hashlib
import string

engine = create_engine("mysql+pymysql://bn_opencart:@localhost:3306/bitnami_opencart")

metadata = MetaData()
customer_table = Table("oc_customer", metadata, autoload_with=engine)
cart_table = Table("oc_cart", metadata, autoload_with=engine)
address_table = Table("oc_address", metadata, autoload_with=engine)
order_table = Table("oc_order", metadata, autoload_with=engine)

def generate_oc_password(password):
    salt = ''.join(random.choices(string.ascii_letters + string.digits, k=9))
    hashed = hashlib.sha1((salt + hashlib.sha1((salt + hashlib.sha1(password.encode('utf-8')).hexdigest()).encode('utf-8')).hexdigest()).encode('utf-8')).hexdigest()
    return hashed, salt

def create_customer_with_address(firstname: str, lastname: str, email: str, phone: str,
                                 password: str, address_1: str, city: str, postcode: str,
                                 country_id: int, zone_id: int):
    # Вставка пользователя
    result_customer = execute_customer(firstname, lastname, email, phone, password)
    customer_id = result_customer.inserted_primary_key[0]
    # Вставка адреса
    result_address = execute_address(customer_id, firstname, lastname, address_1, city, postcode, country_id, zone_id)
    address_id = result_address.inserted_primary_key[0]
    # Привязка адреса к пользователю
    with engine.begin() as conn:
        conn.execute(update(customer_table).where(
            customer_table.c.customer_id == customer_id
        ).values(address_id=address_id))


def execute_customer(firstname: str, lastname: str, email: str, phone: str, password: str):
    hashed_password, salt = generate_oc_password(password)
    # Вставка пользователя
    with engine.begin() as conn:
        result = conn.execute(insert(customer_table).values(
            customer_group_id=1,
            store_id=0,
            language_id=1,
            firstname=firstname,
            lastname=lastname,
            email=email,
            telephone=phone,
            fax='',
            password=hashed_password,
            salt=salt,
            cart=None,
            wishlist=None,
            newsletter=0,
            address_id=0,  # временно
            custom_field='',
            ip='127.0.0.1',
            status=1,
            safe=0,
            token='',
            code='',
            date_added=datetime.now()
        ))
        return result

def execute_address(customer_id: int, firstname: str, lastname: str, address_1: str,
                    city: str, postcode: str, country_id: int, zone_id: int):
    # Вставка адреса
    with engine.begin() as conn:
        result = conn.execute(insert(address_table).values(
            customer_id=customer_id,
            firstname=firstname,
            lastname=lastname,
            company='',
            address_1=address_1,
            address_2='',
            city=city,
            postcode=postcode,
            country_id=country_id,
            zone_id=zone_id,
            custom_field=''
        ))
        return result

def select_users_info():
    with engine.connect() as conn:
        result = conn.execute(select(customer_table).limit(10))
        for row in result.mappings():  # <-- возвращает dict-подобные строки
            print(dict(row))

def delete_user_by_email(email: str):
    with engine.begin() as conn:
        stmt = delete(customer_table).where(customer_table.c.email == email)
        conn.execute(stmt)

def delete_order_by_email(email: str):
    with engine.begin() as conn:
        stmt = delete(order_table).where(order_table.c.email == email)
        conn.execute(stmt)

def delete_cart_by_product_id(product_id: int):
    with engine.begin() as conn:
        stmt = delete(cart_table).where(cart_table.c.product_id == product_id)
        conn.execute(stmt)

def delete_address_by_firstname(firstname: str):
    with engine.begin() as conn:
        stmt = delete(address_table).where(address_table.c.firstname == firstname)
        conn.execute(stmt)

# # Пример вызова
# select_users_info()
# delete_user_by_email("test@test.ru")
# delete_address_by_firstname('Testname')

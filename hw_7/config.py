import os
from dotenv import load_dotenv
from pathlib import Path

class Config:
    def __init__(self, env_file: str = ".env"):
        env_path = Path(__file__).resolve().parent / env_file
        load_dotenv(dotenv_path=env_path)

        self.username = os.getenv("ADMIN_USERNAME")
        self.password = os.getenv("ADMIN_PASSWORD")
        self.product_name = os.getenv("PRODUCT_NAME")
        self.meta_tag_title = os.getenv("META_TAG_TITLE")
        self.model = os.getenv("MODEL")
        self.keyword = os.getenv("KEYWORD")
        self.register_firstname = os.getenv("REGISTER_FIRSTNAME")
        self.register_lastname = os.getenv("REGISTER_LASTNAME")
        self.register_email = os.getenv("REGISTER_EMAIL")
        self.register_password = os.getenv("REGISTER_PASSWORD")



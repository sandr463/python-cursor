import os


class Config:
    PG_USER = "jeniatrofimenko"
    PG_PASSWORD = "password"
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "cursor_lesson"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"


class DevConfig(Config):
    TEST_VARIABLE = "Dev Config"


class TestConfig(Config):
    TEST_VARIABLE = "Test Config"


def runtime_config():
    env = os.environ.get("ENV")
    if env == "DEV":
        return DevConfig
    if env == "TEST":
        return TestConfig
    else:
        return Config

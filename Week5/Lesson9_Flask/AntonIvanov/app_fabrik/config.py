import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    TEST_VARIABLE = "Config"
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    DEBUG = True
    TEST_VARIABLE = "Dev Config"



class TestConfig(Config):
    TEST_VARIABLE = "Test Config"
    TESTING = True


def runtime_config():
    env = os.environ.get("ENV")
    if env == "DEV":
        return DevConfig
    if env == "TEST":
        return TestConfig
    else:
        return Config
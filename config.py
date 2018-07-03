import os


class Config:
    '''
    General configuration parent class
    '''
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ephantus:switcher12@localhost/hustle'
=======

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neville:quelde@localhost/hustle'
>>>>>>> f3c85e1a363b75a9e9f2c986dce5303e1fbd3bb5


class ProdConfig(Config):
    '''
    Pruduction configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}

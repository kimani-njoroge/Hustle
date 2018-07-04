import os


class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sam:  @localhost/hustle'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mzaza:password@localhost/hustle'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://neville:quelde@localhost/hustle'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://midik:12345@localhost/hustle'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ephantus:switcher12@localhost/hustle'


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

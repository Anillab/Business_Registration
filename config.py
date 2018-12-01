
class Config:
    '''Parent Configuration class
    '''
    SQLALCHEMY_DATABSE_URI='postgresql://anilla:Busolo@1997@localhost/andelabiz'
    SECRET_KEY='maishamagumukaka'
    SQLALCHEMY_TRACK_MODIFICATIONS=True

class DevelopmentConfig(Config):
    DEBUG=True

class ProductionConfig(Config):
    pass

class TestConfig(Config):
    pass

config_options={
'development':DevelopmentConfig,
'production':ProductionConfig,
'testing':TestConfig
}

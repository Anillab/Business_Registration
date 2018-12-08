
class Config:
    '''Parent Configuration class
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://anilla:Busolo@1997@localhost/andelabiz'
    UPLOADED_PHOTOS_DEST='app/static/photos'
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

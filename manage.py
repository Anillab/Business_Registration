from app import db,create_app
from flask_script import Manager,Server
from config import config_options
from app.models import User,Business
from flask_migrate import Migrate,MigrateCommand

app=create_app('development')

manager=Manager(app)
migrate=Migrate(app, db)
manager.add_command('db',MigrateCommand)


manager.add_command('server',Server)

if __name__ == '__main__':
    manager.run()

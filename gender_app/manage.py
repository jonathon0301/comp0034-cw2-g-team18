from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from app import create_app, db
from models import Gender_pay
from config import DevConfig

app = create_app(DevConfig)
manage = Manager(app)
migrate = Migrate(app, db)
manage.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manage.run()

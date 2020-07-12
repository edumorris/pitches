from app import create_app, db
from flask_script import Manager, Server
# from app.models import
from flask_migrate import Migrate, MigrateCommand

# App instance
app = create_app('test')

manager = Manager(app)

migrate = Migrate(app, db)
migrate.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ehealthcorp.db'
    db = SQLAlchemy(app)

    from eHealthCorp.models import User

    @app.cli.command()
    def create_db():
        db.create_all()
        print('Database created!')


    @app.cli.command()
    def drop_db():
        db.drop_all()
        print('Database deleted!')


    @app.cli.command()
    def show_tables():
        print(db.engine.table_names())
        # print(db.engine.execute("SELECT * FROM user"))

    #register the blueprints
    from eHealthCorp.home import home
    from eHealthCorp.login import login
    from eHealthCorp.register import register

    app.register_blueprint(home)
    app.register_blueprint(login)
    app.register_blueprint(register)

    return app

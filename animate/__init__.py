
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.debug = True
    app.secret_key = 'BetterSecretNeeded123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///animate.sqlite'


    db.init_app(app)
    
    Bootstrap(app)

    from . import views
    app.register_blueprint(views.main_bp)
    
    @app.errorhandler(404) 
    def not_found(e): 
      return render_template("error.html", error=e)

    @app.errorhandler(500)
    def internal_error(e):
      return render_template("error.html", error=e)
   
    return app
""" Flask Factory
 """

import os
from flask import Flask

def create_app(test_config=None):
    # Create and config the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SESSION_TYPE='filesystem',
        SECURITY_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flask.sqlite'),
    )
    app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'
    # app.secret_key or app.security_key maybe not 
    # 
    app.config['SESSION_TYPE'] = 'filesystem'
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 注册DB
    from . import db
    db.init_app(app)
    
    # 注册 Blueprint
    from . import auth
    app.register_blueprint(auth.bp)
    
    # Import blog blueprint
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    # The 'Hello World !' Page
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
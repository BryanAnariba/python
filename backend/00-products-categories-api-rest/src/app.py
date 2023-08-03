from flask import Flask
from routes.categories import categories_bp

app = Flask(__name__)

app.register_blueprint(
    categories_bp
)

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask
from flask_cors import CORS
from config import Config
from database import db
from routes import chat_blueprint
from auth import auth_blueprint

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CORS(app)

app.register_blueprint(chat_blueprint, url_prefix="/api")
app.register_blueprint(auth_blueprint)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # Add mock data
        from models import Product

        if not Product.query.first():
            products = [
                Product(
                    name="Product 1",
                    description="Description for product 1",
                    price=10.99,
                ),
                Product(
                    name="Product 2",
                    description="Description for product 2",
                    price=12.99,
                ),
                # Add more products as needed
            ]
            db.session.bulk_save_objects(products)
            db.session.commit()
    app.run(debug=True)

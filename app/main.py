# from flask import Flask
from app import create_app

# try:
#     # import routes
#     from .routes import register_routes

#     app = Flask(__name__)

#     register_routes(app)

#     if __name__ == "__main__":
#         app.run(host='127.0.0.1', port=8080, debug=True)
# except Exception as e:
#     print(f"Failed to start Flask app: {e}")


app = create_app()

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
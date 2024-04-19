from flask import Flask


try:
    import routes

    app = Flask(__name__)

    routes.register_routes(app)

    if __name__ == "__main__":
        app.run(host='127.0.0.1', port=8080, debug=True)
except Exception as e:
    print(f"Failed to start Flask app: {e}")
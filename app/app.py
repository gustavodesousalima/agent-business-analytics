from flask import Flask
from routes.agent_routes import agent_routes

app = Flask(__name__)
app.register_blueprint(agent_routes)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
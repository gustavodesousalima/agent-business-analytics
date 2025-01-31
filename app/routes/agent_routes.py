from flask import Blueprint
from controllers.agent_controller import process_user_query

agent_routes = Blueprint("agent_routes", __name__)

agent_routes.route("/ask", methods=["POST"])(process_user_query)

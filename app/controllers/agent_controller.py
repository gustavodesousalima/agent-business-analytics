from flask import request, jsonify
from services.agent_service import AgentService
from config.config import OPENAI_API_KEY

agent_service = AgentService(openai_api_key=OPENAI_API_KEY)

def process_user_query():
    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"error": "A pergunta é obrigatória"}), 400
    
    response = agent_service.process_query(question)
    return jsonify({"response": response})
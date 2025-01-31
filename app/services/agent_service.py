from flask import json
import openai
from services.web_search_service import search_web
from utils.prompt_templates import reformulate_prompt, generate_final_response

class AgentService:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key

    def is_relevant_query(self, question: str) -> bool:
        keywords = ["análise preditiva empresarial", "análise preditiva", "análise empresarial", "tendências de mercado", "machine learning", "inteligência artificial"]
        return any(keyword in question.lower() for keyword in keywords)
    
    def reformulate_query(self, question: str) -> str:
        prompt = reformulate_prompt.format(question=question)
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt}
            ],
            max_tokens=150
        )

        print(json.loads(response.choices[0].message.content))
        return json.loads(response.choices[0].message.content)

    def process_query(self, question: str) -> str:
        if not self.is_relevant_query(question):
            return "Desculpe, não consigo responder a essa pergunta. Pergunte sobre análise preditiva empresarial."
        
        processed_question = self.reformulate_query(question)
        web_data = search_web(processed_question)
        final_prompt = generate_final_response.format(
            question=question,
            web_data=web_data
        )
        response = openai.chat.completions.create(

            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": final_prompt}
            ],
            max_tokens=500
        )
        print(response.choices[0].message.content)
        return response.choices[0].message.content
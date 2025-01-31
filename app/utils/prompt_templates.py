reformulate_prompt = """
Você é um especialista em reformulação de perguntas para busca na web. 
Dado a pergunta:
"{question}"
Reformule-a para otimizar a pesquisa na internet, tornando-a detalhista e clara.
Mantenha o contexto original da pergunta e mantenha a relevância na pesquisa.
"""

generate_final_response ="""
Baseado na pergunta original:
"{question}"

No seu conhecimento sobre análise preditiva empresarial e tendências de mercado.

E nas informações encontradas na web:
"{web_data}"

Crie uma resposta detalhada, usando nomes de empresas e marcas de acordo com as informações que você possui, sendo que a resposta seja útil para um analista de negócios. Garantindo que seja relevante e clara. Essa resposta deve ter no máximo 500 palavras.

Se a perguntar solicitar um número especifico, seja valores monetários, datas, ou qualquer outro tipo de número, forneça uma resposta com base nas informações que você possui.

Se a perguntar solicitar que retorne somente o valor sem mais detalhes, forneça o valor solicitado sem nenhum texto
"""
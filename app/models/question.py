class QueryModel:
    def __init__(self, question: str, processed_question: str = None, response: str = None):
        self.question = question
        self.processed_question = processed_question
        self.response = response
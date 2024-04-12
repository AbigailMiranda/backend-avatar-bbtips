from app.config.connection_mysql import ConnectionMySQL
from app.core.OpenAIAssistant.AIAssistant import AIAssistant
import uuid


class AvatarController:

    def __init__(self) -> None:
        self.connection = ConnectionMySQL()
        self.assistant = AIAssistant()

    def get_response_for_question(self, data: any):
        question = data.get('question')

        additional_instructions = "Sé amable y comprensiva con el usuario"
        response = self.assistant.ask_question_and_get_response(question, additional_instructions)
        return {'data': response}




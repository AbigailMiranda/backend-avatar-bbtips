from app.config.connection_mysql import ConnectionMySQL
from app.core.OpenAIAssistant.AIAssistant import AIAssistant


class AvatarController:

    def __init__(self) -> None:
        self.connection = ConnectionMySQL()
        self.assistant = AIAssistant()

    def get_response_for_question(self, data: any):
        try:
            question = data.get('question')
            user_id = data.get('user-id')
            additional_instructions = "Sé amable y comprensiva con el usuario"
            response = self.assistant.ask_question_and_get_response(question, additional_instructions)
            query = f"INSERT INTO preguntas_usuarios (IDUser, Pregunta, Respuesta) VALUES ('{user_id}','{question}','{response}');"
            self.connection.execute_query(query)

            return {'error': False, 'data': response}
        except Exception as e:
            print(str(e))
            return {'error': True, 'data': str(e)}




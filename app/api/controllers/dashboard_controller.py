from app.config.connection_mysql import ConnectionMySQL


class DashboardController:

    def __init__(self) -> None:
        self.connection = ConnectionMySQL()
        pass

    def comments_users(self):

        query = f'SELECT * FROM comentarios_usuarios'
        response = self.connection.fetch_query(query)

        if len(response) == 0:
            return {'error': False, 'data': 'No hay comentarios'}

        return {'error': False, 'data': response}

    def user_parents_info(self, skip: int = 0, limit: int = 10):
        try:
            query = f'SELECT * FROM usuarios_papas LIMIT {limit} OFFSET {skip};'
            res = self.connection.fetch_query(query)

            query = 'SELECT COUNT(*) AS count FROM usuarios_papas;'
            count = self.connection.fetch_query(query)[0]['count']

            if len(res) == 0:
                return {'error': False, 'data': 'No hay información', 'total_count': count}

            return {'error': False, 'data': res, 'total_count': count}

        except Exception as e:
            print(str(e))
            return {'error': True, 'data': str(e)}

    def user_questions(self, skip: int = 0, limit: int = 10):
        try:
            query = f'SELECT * FROM preguntas_usuarios LIMIT {limit} OFFSET {skip};'
            res = self.connection.fetch_query(query)

            query = 'SELECT COUNT(*) AS count FROM preguntas_usuarios;'
            count = self.connection.fetch_query(query)[0]['count']

            if len(res) == 0:
                return {'error': False, 'data': 'No hay información', 'total_count': count}

            return {'error': False, 'data': res, 'total_count': count}

        except Exception as e:
            print(str(e))
            return {'error': True, 'data': str(e)}

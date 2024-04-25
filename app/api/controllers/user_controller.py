from app.config.connection_mysql import ConnectionMySQL
import dotenv
import os
import jwt
import uuid


class UserController:

    def __init__(self) -> None:
        self.connection = ConnectionMySQL()
        pass

    def validate_id_user(self, req):
        user_id = req.get('id')
        try:
            query = f"SELECT * FROM `usuarios_papas` WHERE IDUser ='{user_id}';"
            return self.connection.fetch_query(query)[0]
        except Exception as e:
            print(e)

    def validate_access_token(self, req):
        dotenv.load_dotenv()
        token = req

        try:
            secret_key = os.getenv('SECRET_JWT')
            token_decode = jwt.decode(token, secret_key, algorithms=['HS256'])
            user_id = token_decode['user']
            query = f'SELECT * FROM usuarios WHERE IDUser = {user_id}'
            response = self.connection.fetch_query(query)
            if len(response) > 0:
                return {'error': False, 'data': response[0]}

            return {'error': True}

        except Exception as e:
            print(f'error in valid_access_token user: {e}')

            return {'error': True, 'data': 'Error en la validacion del token'}

    def authentication(self, req):
        dotenv.load_dotenv()
        mail = req.get('mail')
        password = req.get('pass')

        try:

            query = f'SELECT * FROM usuarios WHERE Mail ="{mail}"'
            response = self.connection.fetch_query(query)

            if len(response) == 0:
                return {'error': True, 'data': 'Correo o contraseña incorrectos'}

            user = response[0]

            if user['Mail'] == mail and user['Pass'] == password:
                secret_key = os.getenv('SECRET_JWT')
                payload = {
                    'user': user['IDUser'],
                    'role': user['IDRole']
                }
                token = jwt.encode(payload, secret_key, algorithm='HS256')
                query = f'UPDATE usuarios SET Access_Token ="{token}"'
                res = self.connection.execute_query(query)
                print(res)
                return {'error': False, 'data': user, 'token': token}
            else:
                return {'error': True, 'data': 'Correo o contraseña incorrectos'}
        except Exception as e:
            print(f'error in authentication user: {e}')
            return 'Error en la autentificación'

    def user_accept_privacity(self, data: any):
        try:
            accept = data.get('accept')
            if (accept == '1'):
                # todo: crea el usuario en la bd y le asigna el id
                user_id = uuid.uuid4()
                user_id = str(user_id)
                user_id = user_id[:5]
                query = f"INSERT INTO usuarios_papas (IDUser) VALUES ('{user_id}');"
                self.connection.execute_query(query)
                return {'error': False, 'data': user_id}
            else:
                return {'error': False, 'data': 'user not accepted'}
        except Exception as e:
            print(f'error in user accept privacy {str(e)}')
            return {'error': True, 'data': f'{str(e)}'}

    def get_data_user_form(self, data: any):
        try:
            user_form = data.get("user-form")
            user_feedback_form = data.get("user-feedback")
            user_id = user_form['id']
            city = user_form['city']
            country = user_form['state']
            type_parent = user_form['primerize']
            birthdate = user_form['birthday']
            genere = user_form['genere']
            baby_stage = user_form['babystage']
            baby_weight = user_form['babyweight']
            baby_clothe = user_form['babyclothe']

            user_state = user_feedback_form['state']
            user_feedback = user_feedback_form['feedback']

            query = f"""UPDATE usuarios_papas SET 
            Ciudad= '{city}',
            Estado='{country}', 
            Primerizo='{type_parent}', 
            Edad='{birthdate}', 
            Genero='{genere}',
            TipoEtapaBebe='{baby_stage}',
            TipoPanial='{baby_clothe}',
            PesoBebe={baby_weight},
            RealizoEncuesta=1
            WHERE IDUser ='{user_id}';
            """
            self.connection.execute_query(query)
            query = f"""
            INSERT INTO comentarios_usuarios (IDUser, Comentario, Tipo, Visto) VALUES (
            '{user_id}',
            '{user_feedback}',
            {int(user_state)}, 0);
            """
            res = self.connection.execute_query(query)
            return {'error': False, 'data': res}
        except Exception as e:
            print(f'error in insert form: {e}')
            return {'error': True, 'data': f'{str(e)}'}

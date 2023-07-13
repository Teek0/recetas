from app_recetas.config.mysqlconnection import connectToMySQL
from app_recetas import EMAIL_REGEX,BASE_DATOS
from flask import flash

class Usuario:
    def __init__(self, data):
        self.id=data['id']
        self.nombre=data['nombre']
        self.apellido=data['apellido']
        self.email=data['email']
        self.password=data['password']
        self.creado=data['creado']
        self.editado=data['editado']

    @classmethod
    def obtener_uno_con_email(cls,data):
        query = """
                SELECT *
                FROM usuarios
                WHERE email = %(email)s
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query,data)
        if len(resultado)==0:
            return None
        else:
            return Usuario(resultado[0])
    
    @classmethod
    def crear_uno(cls,data):
        query = """
                INSERT INTO usuarios(nombre,apellido,email,password)
                VALUES (%(nombre)s,%(apellido)s,%(email)s,%(password)s)
                """
        id_usuario = connectToMySQL(BASE_DATOS).query_db(query,data)
        return id_usuario
    
    @staticmethod
    def validar_registro(data,usuario_existe):
        es_valido = True
        if len(data['nombre'])<2:
            es_valido = False
            flash("Tu nombre necesita al menos 2 carácteres","error_nombre")
        if len(data['apellido'])<2:
            es_valido = False
            flash("Tu apellido necesita al menos 2 carácteres","error_apellido")
        if not EMAIL_REGEX.match(data['email']):
            es_valido = False
            flash("Por favor ingresa un email válido.","error_email")
        if data['password'] != data['confirmacion_password']:
            es_valido = False
            flash("Tus passwords no coinciden, intenta nuevamente.","error_password")
        if usuario_existe != None:
            es_valido=False
            flash("Correo ya registrado.","error_email")

        return es_valido
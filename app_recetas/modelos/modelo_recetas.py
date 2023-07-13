from app_recetas.config.mysqlconnection import connectToMySQL
from app_recetas.modelos.modelo_usuarios import Usuario
from app_recetas import BASE_DATOS
from flask import flash

class Receta:
    def __init__(self, data):
        self.id=data['id']
        self.nombre=data['nombre']
        self.descripcion=data['descripcion']
        self.instrucciones=data['instrucciones']
        self.menos_de_treinta=data['menos_de_treinta']
        self.fecha_cocinado=data['fecha_cocinado']
        self.id_usuario=data['id_usuario']
        self.creado=data['creado']
        self.editado=data['editado']
        
    @classmethod
    def crear_uno(cls,data):
        query="""
        INSERT INTO recetas (nombre,descripcion,instrucciones,menos_de_treinta,fecha_cocinado,id_usuario)
        VALUES (%(nombre)s,%(descripcion)s,%(instrucciones)s,%(menos_de_treinta)s,%(fecha_cocinado)s,%(id_usuario)s)
        """
        id_receta=connectToMySQL(BASE_DATOS).query_db(query,data)
        return id_receta
    
    @classmethod
    def obtener_todas_con_usuario(cls,data):
        query = """
                SELECT *
                FROM recetas r JOIN usuarios u
                ON r.id_usuario=u.id;
                """
        resultado=connectToMySQL(BASE_DATOS).query_db(query)
        lista_recetas=[]
        for renglon in resultado:
            receta=Receta(renglon)
            data_usuario={
                "id":renglon['u.id'],
                "nombre":renglon['u.nombre'],
                "apellido":renglon['apellido'],
                "email":renglon['email'],
                "password":renglon['password'],
                "creado":renglon['u.creado'],
                "editado":renglon['u.editado'],
            }
            usuario=Usuario(data_usuario)
            receta.usuario=usuario
            lista_recetas.append(receta)
        return lista_recetas
    
    @classmethod
    def elimina_uno(cls,data):
        query = """
                DELETE FROM recetas
                WHERE id = %(id)s;
                """
        return connectToMySQL(BASE_DATOS).query_db(query,data)

    @staticmethod
    def validar_formulario_recetas(data):
        es_valido=True
        if len(data['nombre'])<3:
            es_valido=False
            flash("Debes de proporcionar un nombre válido a la receta (mín. 3 carácteres)","error_nombre")
        if len(data['descripcion'])<3:
            es_valido=False
            flash("Debes de proporcionar una descripción válida para la receta (mín. 3 carácteres)","error_descripcion")
        if len(data['instrucciones'])<3:
            es_valido=False
            flash("Debes de proporcionar instrucciones válidas para la receta (mín. 3 carácteres)","error_instrucciones")
        if data['fecha_cocinado']=="":
            es_valido=False
            flash("Debes de proporcionar la fecha de la receta","error_fecha_cocinado")
        if 'menos_de_treinta' not in data:
            es_valido=False
            flash("Debes seleccionar si la receta se elabora en menos de 30 min o no","error_menos_de_treinta")
        return es_valido
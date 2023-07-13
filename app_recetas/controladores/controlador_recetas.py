from flask import render_template,request,session,redirect
from app_recetas.modelos.modelo_recetas import Receta
from app_recetas import app

@app.route('/recetas', methods=['GET'])
def desplegar_recetas():
    #obtener las recetas y enviar la lista de recetas al template
    lista_recetas=Receta.obtener_todas_con_usuario()
    return render_template('recetas.html',lista_recetas=lista_recetas)

@app.route('/formulario/receta', methods=["GET"])
def desplegar_formulario_receta():
    return render_template('formulario_receta.html')

@app.route('/crear/receta', methods=['POST'])
def nueva_receta():
    data={
        **request.form,
        "id_usuario":session['id_usuario']
    }
    #validaciones
    if Receta.validar_formulario_recetas(data)==False:
        return redirect('/formulario/receta')
    else:
        id_receta=Receta.crear_uno(data)
        return redirect('/recetas')

@app.route('/eliminar/receta/<int:id>', methods=['POST'])
def eliminar_receta(id):
    data={
        "id":id
    }
    Receta.elimina_uno(data)
    return redirect('/recetas')
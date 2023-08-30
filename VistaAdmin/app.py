#modulos que vamos a usar
from flask import Flask
from flask import render_template,request,redirect,url_for
from flaskext.mysql import MySQL
from flask import send_from_directory
from datetime import datetime
import os


from empleados.empleados import empleados_blueprint
from clientes.clientes import clientes_blueprint
from proyectos.proyectos import proyectos_blueprint
from VistaClie.VistaClie import VistaClie_blueprint



#creamos una aplicacion
app=Flask(__name__)


app.register_blueprint(proyectos_blueprint, url_prefix='/proyectos')
app.register_blueprint(VistaClie_blueprint, url_prefix='/VistaClie')
app.register_blueprint(empleados_blueprint, url_prefix='/empleados')
app.register_blueprint(clientes_blueprint, url_prefix='/clientes')

##conexion a base de datos
mysql= MySQL()
#creamos referencia a el host
#para que se conecte a la base de datos mysql vamos a usar el localhost
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PORT']=3307
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema'
#hacemos que mysql inicie la conexion
mysql.init_app(app)


@app.route('/')
def incio():
    return render_template('/index.html')




@app.route('/login')
def mostrar_login():

    return render_template('login/login.html')



if __name__== '__main__':
    app.run(debug=True)
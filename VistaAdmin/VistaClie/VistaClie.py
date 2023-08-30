from flask import Blueprint, render_template, request, redirect, send_from_directory, current_app
from flaskext.mysql import MySQL  # O desde 'your_app import mysql', según tu configuración
import os
from datetime import datetime
#modulos que vamos a usar
from flask import Flask
from flask import render_template,request,redirect,url_for
from flaskext.mysql import MySQL
from flask import send_from_directory
from datetime import datetime
import os

app=Flask(__name__)


mysql= MySQL()

VistaClie_blueprint = Blueprint('VistaClie', __name__)

app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PORT']=3306
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema'
#hacemos que mysql inicie la conexion
mysql.init_app(app)



@VistaClie_blueprint.route('/')
def index():
    return  render_template('VistaClie/index.html')



@VistaClie_blueprint.route('/config')
def config():
    return  render_template('/VistaClie/config.html')


@VistaClie_blueprint.route('/logout')
def logout():
    return  render_template('/VistaClie/logout.html')

@VistaClie_blueprint.route('/reportar')
def reportar():
    return  render_template('/VistaClie/reportar.html')

@VistaClie_blueprint.route('/notificaciones')
def notificaciones():
    return  render_template('/VistaClie/notifiaciones.html')


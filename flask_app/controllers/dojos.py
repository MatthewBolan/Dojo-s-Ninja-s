from flask import render_template, redirect, request

from flask_app import app

from flask_app.models.dojo import Dojo




@app.route('/')
def index():
    return redirect("/create/dojos")



@app.route('/create/dojos')
def dojos_create():

    return render_template("create_display_dojos.html", dojos=Dojo.display_all_dojos())





@app.route('/added/dojo', methods=['POST'])
def dojo_added():

    Dojo.save_dojo(request.form)

    return redirect ('/')



@app.route('/show/dojo/<int:id>')
def dojo_show_ninjas(id):
    
    data ={

        "id":id

    }

    return render_template("show_dojo_ninjas.html",dojos=Dojo.get_one_dojo_ninjas(data))
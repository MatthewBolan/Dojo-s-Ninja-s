from flask import render_template, redirect, request

from flask_app import app

from flask_app.models.dojo import Dojo

from flask_app.models.ninja import Ninja



@app.route('/add/ninja')
def ninja_add():

    return render_template("create_ninja.html", dojos=Dojo.display_all_dojos())


@app.route('/added/ninja', methods=['POST'])
def ninja_added():

    Ninja.save_ninja(request.form)

    return redirect ('/')

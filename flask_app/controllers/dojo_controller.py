from pprint import pprint
from flask_app import app, render_template, redirect, request
from flask_app.models.dojo_model import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

# display all dojos
@app.get('/dojos')
def all_dojos():
    dojos = Dojo.find_all()
    print(f'**** FOUND - ALL DOJOS: ****')
    pprint(dojos)
    return render_template('all_dojos.html', dojos = dojos)

@app.post('/dojos')
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

# display one dojo by id
@app.get('/dojos/<int:dojo_id>')
def one_dojo(dojo_id):
    data = {
        'id': dojo_id
    }
    # need to use the correct methods to obtain the correct id with model!!!!!!!!!!!
    dojo = Dojo.find_by_id_with_models(data)
    print(f'**** FOUND - DOJO ID: {dojo.id} ****')
    return render_template('one_dojo.html', dojo=dojo)


# display form to edit a dojo by id
@app.get('/dojos/<int:dojo_id>/edit')
def edit_dojo(dojo_id):
    data = {
        'id': dojo_id
    }
    dojo = Dojo.find_by_id(data)
    print(f'**** FOUND - DOJO ID: {dojo.id} ****')
    return render_template('edit_dojo.html', dojo = dojo)

# process form and update a dojo by id
@app.post('/dojos/<int:dojo_id>/update')
def update_dojo(dojo_id):
    Dojo.find_by_id_and_update(request.form)
    print(f'**** UPDATED - DOJO ID: {dojo_id} ****')
    return redirect(f'/dojos/{dojo_id}')

# delete one dojo by id
@app.get('/dojos/<int:dojo_id>/delete')
def delete_dojo(dojo_id):
    data = {
        'id': dojo_id
    }
    Dojo.find_by_id_and_delete(data)
    print(f'**** DELETED - DOJO ID: {dojo_id} ****')
    return redirect('/dojos')
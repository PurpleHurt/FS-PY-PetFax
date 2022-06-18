from flask import ( Blueprint, render_template ) 
import json 

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)

@bp.route('/pets/<int:id>')
def show(id): 
    pet = pets[id - 1]
    return render_template('show.html', pet=pet)

#tried to create URL using the pet name but wasn't able to get it working
#@bp.route('/pets/<pet_name>')
#def show(pet_name):
    #pets = pets[pet_name - 1]
    #return render_template('show.html')

@bp.route('/new')
def new():
    return render_template('new.html')
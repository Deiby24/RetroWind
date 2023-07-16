from flask import Flask, render_template,request,make_response,jsonify


app = Flask(__name__)
juegos = [
    {
        "id": 1,
        "name": "doblin",
        "description": "",
        "img": "doblin.jpg"
    },
    {           
        "id": 2,
        "name": "mega",
        "description": "",
        "img": "mega.jpg"
    },
    {            
        "id": 3,
        "name": "doom",
        "description": "",
        "img": "doom.jpg"
    },
    {            
        "id": 4,
        "name": "Juego 4",
        "description": "",
        "img": "donk.jpg"
    },
    {            
        "id": 5,
        "name": "Juego 5",
        "description": "",
        "img": "drive.jpg"
    },
]


@app.route('/')
def home():
    return render_template('home.html' ,juegos=juegos)

mivariable = []

@app.route('/guardar', methods=['POST'])
def guardar():
    global mivariable
    try:
        button_value = int(request.form.get('button_value'))
        # print("El valor del botón es:", button_value)

        mivariable = request.cookies.get('mivariable')

        if not mivariable:
            mivariable = []
        else:
            mivariable = list(map(int, mivariable.split(',')))
         
        if button_value not in mivariable:
            mivariable.append(button_value)
            mivariable_str = ','.join(map(str, mivariable))
            response = make_response('')
            response.set_cookie('mivariable', mivariable_str)
            print("El valor del botón es:", mivariable)
            return response
        else:
            print("ya fue agregado")
            return ''
    except Exception as e:
        # Manejar cualquier excepción y devolver una respuesta de error
        error_message = "Ocurrió un error: " + str(e)
        return jsonify({'error': error_message}), 500
    

@app.route('/borrar_cookie', methods=['POST'])
def borrar_cookie():
    # Crear una respuesta vacía
    response = make_response('')

    # Borrar la cookie
    response.delete_cookie('mivariable')

    return response

@app.route('/cart')
def cart():
    add = []
    for juego in juegos:
        if juego['id'] in mivariable:
            add.append(juego) 
        else:
         print("no hay juego")
    
    return render_template('cart.html', juegos=juegos , mivariable=mivariable,add=add)


if __name__ == '__main__':
    app.run(debug=True)
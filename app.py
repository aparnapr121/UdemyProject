from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name' : 'My wonderful store',
        'items': [
            {
            'name': 'My item',
            'price': 15.99
            }
        ]
    }
]


@app.route('/store',methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)



@app.route('/store/<string:name>')
def get_store(name):
    #iterate over stores and return the matching store name
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})

@app.route('/store/<string:name>/item')
def get_items_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'store not found'})

@app.route('/store/<string:name>/item',methods = ['POST'])
def create_items_store(name):
    request_data = request.get_json()
    
    for store in stores:
        if store['name'] == name:
            new_item = {
                 'name':request_data['name'],
                 'price': request_data['price']
                } 
            store['items'].append(new_item)
            return jsonify(store)
    return jsonify({'message' :'store not found'})

@app.route('/')
def home():
    return render_template('index.html')

app.run(port = 5000)


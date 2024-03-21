from flask import Flask, request, Response
from dicttoxml import dicttoxml
from roots import Roots

app = Flask(__name__)

@app.route(Roots.START_ROOT, methods=['GET'])
def get_salutations():
    return Response(dicttoxml({'Français': "Bonjour"}), mimetype='text/xml')

@app.route(Roots.END_ROOT, methods=['GET'])
def get_good_bye():
    return Response(dicttoxml({'Français': 'Au revoir!'}), mimetype='text/xml')

@app.route(Roots.PALINDROME_ROOT, methods=['POST'])
def validate_palindrome():
    # Lire la valeur de l'en-tête "Palindrome"
    palindrome_value = request.headers.get('Palindrome')
    if palindrome_value:
        return Response(dicttoxml({'message': 'Palindrome ou pas ? on verra !'}), status=201, mimetype='text/xml')
    else:
        return Response(dicttoxml({'message': 'La valeur de palindrome non definis dans la requette !'}), status=201, mimetype='text/xml')    	

if __name__ == '__main__':
    app.run(debug=True, port=5000)

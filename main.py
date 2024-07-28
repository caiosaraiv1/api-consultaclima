from flask import Flask, jsonify, request
import requests
from googletrans import Translator
from dotenv import load_dotenv
import os

load_dotenv()
translator = Translator()
app = Flask(__name__)

URL_BASE = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = os.getenv("API_KEY")

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

@app.route('/clima',methods = ['GET'])
def clima_cidade ():

    cidade = request.args.get('cidade')

    url = URL_BASE + "appid=" + API_KEY + "&q=" + cidade

    response = requests.get(url).json()

    temp_kelvin = response['main']['temp']
    temp_celsius = kelvin_to_celsius(temp_kelvin)

    sensacao_kelvin = response['main']['feels_like']
    sensacao_celsius = kelvin_to_celsius(sensacao_kelvin)

    umidade = response['main']['humidity']
    descricao = response['weather'][0]['description']

    translation = translator.translate(descricao, src='en', dest='pt')

    return jsonify({
        'Cidade': cidade,
        'Temperatura': f"{temp_celsius:.2f}°C",
        'Sensação': f"{sensacao_celsius:.2f}°C",
        'Descrição': translation.text,
        'Umidade': f"{umidade}%",
    })

if __name__ == '__main__':
    app.run(debug=True)


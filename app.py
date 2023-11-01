from flask import Flask,jsonify,request
from flask_cors import CORS
import random

possible_responses = [
    "ESTO ES FALO, ME CREO EL GOBIERNO",
    "Hola, ¿en qué puedo ayudarte?",
    "Lo siento, no puedo ayudarte. Soy un programa de chat.",
    "¡JAJAJA!",
    "¡Eres muy gracioso!",
    "Hola, ¿cómo estás? 😊",
    "No entiendo tu pregunta, ¿puedes ser más específico?",
    "¿En qué puedo asistirte hoy?",
    "¡Hola! Si tienes alguna pregunta, estaré encantado de ayudarte.",
    "Lamento que no pueda ser de más ayuda. 😔",
    "Eres increíble, ¡gracias por tu amabilidad!",
    "¡Hola! Estoy aquí para responder tus preguntas.",
    "¿En qué puedo orientarte hoy?",
    "No entiendo bien lo que dices. ¿Puedes reformular tu pregunta?",
    "Si tienes alguna duda, no dudes en preguntar.",
    "¡Hola, querido usuario! Estoy listo para ayudarte.",
    "Lo siento, mi conocimiento es limitado, pero haré lo mejor que pueda.",
    "¡Hola! ¿En qué puedo colaborar contigo hoy?",
]


class chat:
    chat_response = ""
    meta = []
    question = ""
    offensive_message = False


app = Flask(__name__)
CORS(app)
    
@app.route('/query')
def query():
    text = request.args.get('text')
    return jsonify(makeResponse(text))

@app.route('/train')
def train():
    return jsonify("Trained jiji")

@app.route('/')
def index():
    return "ESTE ES EL INDEX"

def makeResponse(query):
    new_chat = chat()
    random.shuffle(possible_responses)
    new_chat.chat_response = random.choice(possible_responses)
    new_chat.question = query
    data = {
        "chat_response": new_chat.chat_response,
        "question": new_chat.question,
        "meta":[],
        "offensive_message":new_chat.offensive_message
    }
    
    return data



if __name__ == '__main__':
    app.run(host="0.0.0.0")








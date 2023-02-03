from flask import Flask, request, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer



app = Flask(__name__)

portuguese_bot = ChatBot('Chatterbot', storage_adapter='chatterbot.storage.SQLStorageAdapter')

trainer = ListTrainer(portuguese_bot)

trainer.train([
    
    #Digite a mensagem de pergunta, e resposta esperada pelo boot
])

trainer.train([
    
    #Digite a mensagem de pergunta, e resposta esperada pelo boot
])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    userText = request.args.get('msg')
    return str(portuguese_bot.get_response(userText))





if __name__ == '__main__':
    app.run()
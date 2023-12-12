from boggle import Boggle
from flask import Flask, render_template, redirect, session, request, jsonify

app = Flask(__name__)
app.secret_key = 'baba-yaga'

boggle_game = Boggle()

@app.route("/")
def home_page():
    board = boggle_game.make_board()
    session['board'] = board
    return render_template("home.html")

@app.route("/guess", methods=['POST'])
def check_guess():
    guess = request.json.get("user-guess")
    print(guess)
    word_check = boggle_game.check_valid_word(session['board'], guess)
    return jsonify({'result': word_check})
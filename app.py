from flask import Flask, request, redirect, render_template
from sorting_hat import SortingHat

app = Flask(__name__)

sorting_hat = SortingHat(0, 0, 0, 0)

IMG_DIR = './static'

@app.route('/')
def hello_wizarding_world():
    """a simple HTTP print"""
    return 'hello wizarding world!'

@app.route('/image')
def serve_image():
    "a simple HTTP image"
    return render_template('image.html')

@app.route('/hat')
def hat():
    """prints the current values for sorting hat"""
    return list(sorting_hat.houses.items())

@app.route('/reset')
def reset():
    """resets the current values of sorting hat"""
    sorting_hat.clear()
    return 'the sorting hat has been reset!'

@app.route('/question/1', methods = ['GET', 'POST'])
def first_question():
    """asks the first question"""
    answers = ['dog', 'badger', 'magpie', 'cobra']

    if request.method == 'GET':
        return render_template('question_1.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            sorting_hat.add('gryffindor')
        if selected == answers[1]:
            sorting_hat.add('hufflepuff')
        if selected == answers[2]:
            sorting_hat.add('ravenclaw')
        if selected == answers[3]:
            sorting_hat.add('slytherin')

        return redirect('/question/2')

@app.route('/question/2', methods = ['GET', 'POST'])
def second_question():
    """asks the second question"""
    answers = ['oak', 'yew', 'maple', 'ash']

    if request.method == 'GET':
        return render_template('question_2.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            sorting_hat.add('gryffindor')
        if selected == answers[1]:
            sorting_hat.add('hufflepuff')
        if selected == answers[2]:
            sorting_hat.add('ravenclaw')
        if selected == answers[3]:
            sorting_hat.add('slytherin')

        return redirect('/question/3')

@app.route('/question/3', methods = ['GET', 'POST'])
def third_question():
    """asks the third question"""
    answers = ['expelliarmus', 'petrificus totalus', 'winguardium leviosa', 'avada kedavra']

    if request.method == 'GET':
        return render_template('question_3.html', answers = answers)

    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            sorting_hat.add('gryffindor')
        if selected == answers[1]:
            sorting_hat.add('hufflepuff')
        if selected == answers[2]:
            sorting_hat.add('ravenclaw')
        if selected == answers[3]:
            sorting_hat.add('slytherin')

        return redirect('/house')

@app.route('/house')
def get_house():
    """presents the house quiz results"""
    return 'congratulations, you are in ' + sorting_hat.sort() + '!'

if __name__ == '__main__':
    app.run(host='localhost', port=8081)

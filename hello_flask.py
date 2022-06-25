from crypt import methods
from flask import Flask, render_template, request



def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))



app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello worldasdasd"

@app.route('/search4', methods = ['POST','GET'])
def do_search():
    return str(search4letters(request.form["phrase"],request.form["letters"]))    
    
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')



app.run(debug=True)

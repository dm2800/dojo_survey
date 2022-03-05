
from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)  
app.secret_key = 'safekey'

@app.route('/')
def index():
    session.clear()
    print(session)
    return render_template('index.html')


@app.route('/userinfo', methods=['POST'])
def create_user():
    print('Printing session info:')
    print(session)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    session['gender'] = request.form['gender']
    print('Printing request.form info')
    print(request.form)
    return redirect('/results')

@app.route('/results')
def results():
    print("Showing user info from form")
    print(request.form)
    print("Showing what's in session!")
    print(session)
    return render_template('results.html', name_on_template=session['name'], location_on_template=session['location'], language_on_template=session['language'], comments_on_template=session['comments'], gender_on_template=session['gender'])



if __name__ == "__main__":
    app.run(debug=True)












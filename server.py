from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it serect'

@app.route('/', methods=['GET', 'POST'])
def count_visit():
    if request.method == 'POST':
        if request.form.get('two_count'):
            session['count'] += 1
            session['visit'] -= 1   # exclude visits cause by redirect; only count re-visit for user
            return redirect('/')    # prevent resubmission
        if request.form.get('user_count'):
            session['count'] += int(request.form.get('user_count')) - 1
            session['visit'] -= 1   # same as above
            return redirect('/')
        if request.form.get('reset'):
            return redirect('/destroy_session')
        
    elif request.method == 'GET':
        if 'count' in session:
            session['count'] += 1
            session['visit'] += 1
        else: 
            session['count'] = 1
            session['visit'] = 1
    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    # session.pop('count')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

# decode cookie info
# import base64
# >>> import base64
# >>> base64.urlsafe_b64decode('eyJjb3VudCI6MTUsInZpc2l0IjoyfQ===')
# b'{"count":15,"visit":2}'
from flask import Flask, request, render_template,redirect, flash
from convert import result,code_validity,num_validity

app = Flask(__name__)

app.config['SECRET_KEY'] = 'apples'

@app.route('/')
def index_page():
    """Returns home page"""
    return render_template('index.html')

@app.route('/', methods=["POST"])
def handler():
    """Post route for result of user data"""
    curr_orig = request.form.get("InitialCurr").upper()
    if not code_validity(curr_orig) or not curr_orig:
        flash('Original Currency is not valid!')
        return redirect('/')
    
    curr_to = request.form.get("DesiredCurr").upper()
    if not code_validity(curr_to) or not curr_to:
        flash('Desired Currency is not valid!')
        return redirect('/')

    amount = request.form.get('Amount')
    if not num_validity(amount):
        flash('Please enter a valid currency amount!')
        return redirect('/')

    res_data = result(curr_orig,curr_to,amount)


    print(res_data)
    
    return render_template('index.html', res_data = res_data)
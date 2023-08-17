from flask import Flask, render_template, request 
import random
import time 
from timeit import default_timer as timer
from utils import auth_required

app = Flask(__name__,template_folder="templates")

start = 0 
end = 0 

@app.route('/index.html')
@auth_required
def index():
    return render_template('index.html')

@app.route('/anim-t.html')
@auth_required
def animation_t():
        global random_key
        random_key = random.randint(1,4)
        # time.sleep(2)
        global start 
        start = timer()
        if random_key == 1:
            return render_template('anim1.html', css_template='stylesheet1')
        if random_key == 2:
            return render_template('anim2.html', css_template='stylesheet1')
        if random_key == 3:
            return render_template('anim3.html', css_template='stylesheet1')
        if random_key == 4:
            return render_template('anim4.html', css_template='stylesheet1')
        
@app.route('/anim-c.html')
@auth_required
def animation_c():
        global random_key
        random_key = random.randint(1,4)
        # time.sleep(2)
        global start 
        start = timer()
        if random_key == 1:
            return render_template('anim1.html', css_template='stylesheet2')
        if random_key == 2:
            return render_template('anim2.html', css_template='stylesheet2')
        if random_key == 3:
            return render_template('anim3.html', css_template='stylesheet2')
        if random_key == 4:
            return render_template('anim4.html', css_template='stylesheet2')

@app.route('/results1.html')
@auth_required
def results1():
    end = timer()
    return render_template('results1.html', stop_time = round(end-start, 2), rkey = random_key)

@app.route('/results2.html')
@auth_required
def results2():
    end = timer()
    return render_template('results2.html', stop_time = round(end-start, 2), rkey = random_key)

@app.route('/results3.html')
@auth_required
def results3():
    end = timer()
    return render_template('results3.html', stop_time = round(end-start, 2), rkey = random_key)

@app.route('/results4.html')
@auth_required
def results4():
    end = timer()
    return render_template('results4.html', stop_time = round(end-start, 2), rkey = random_key)

@app.route('/anim1.html')
@auth_required
def animation1():
    global start 
    start = timer()
    return render_template('anim1.html')

@app.route('/anim2.html')
@auth_required
def animation2():
    global start 
    start = timer()
    return render_template('anim2.html')

@app.route('/anim3.html')
@auth_required
def animation3():
    global start 
    start = timer()
    return render_template('anim3.html')

@app.route('/anim4.html')
@auth_required
def animation4():
    global start 
    start = timer()
    return render_template('anim4.html')

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, redirect, url_for, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index3.html')

@app.route('/index2', methods= ['POST','GET'])
def index2():
        index2 = request.form
        return render_template('index2.html')
        os.system('python D:\GAN\GANgogh.py')
   
if __name__ == "__main__":
    app.run(host='0.0.0.0')


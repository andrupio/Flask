from flask import Flask
from flask import render_template
from flask.globals import request
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/mypage/me')
def me():
    print("We received GET")
    return render_template("o_mnie.html")

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
   if request.method == 'GET':
       print("We received GET")
       return render_template("kontakt.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/mypage/contact")

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
app = Flask("MyApp")
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/tda", methods=["POST"])
def tda():
    form_data = request.form
    tda = form_data["tda"]
    print (tda)
    return render_template("tda.html")
    #return render_template("tda.html")

app.run(debug=True)

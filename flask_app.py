from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return '<h2>WELCOME TO MY FLASK APP</h2>'

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# Route with parameter
@app.route("/user/<username>")
def user(username):
    return render_template("user.html", username=username)

#route for GET and POST
@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        return render_template("thank.html", name=name, email=email)
    else:
        return render_template("submit.html")

if __name__ == "__main__":
    app.run(debug=True)

# Form Handling:
# Create a form with Flask that takes user input (e.g., name, email) and displays it on a new page after submission.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Route to display the form
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get data from form
        name = request.form["name"]
        email = request.form["email"]

        # Redirect to the display page with form data
        return redirect(url_for("display", name=name, email=email))
    return render_template("form.html")


# Route to display submitted form data
@app.route("/display")
def display():
    # Retrieve the name and email from the URL parameters
    name = request.args.get("name")
    email = request.args.get("email")

    return render_template("display.html", name=name, email=email)


if __name__ == "__main__":
    app.run(debug=True)

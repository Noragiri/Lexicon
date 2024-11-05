# Create a Flask application with three routes:

# Route 1: Display a welcome message on the home page.
# Route 2: Display information about yourself on a separate page.
# Route 3: Create a custom 404 error page.

from flask import Flask, render_template

app = Flask(__name__)


# Route 1: Home page with a welcome message
@app.route("/")
def home():
    return "<h1>Welcome to the Home Page!</h1><p>This is the main page of our Flask app.</p>"


# Route 2: About page with information about yourself
@app.route("/about")
def about():
    return "<h1>About Me</h1><p>Hello! I am a Flask developer learning how to build web apps.</p>"


# Route 3: Custom 404 error page
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Oops! The page you're looking for doesn't exist.</p>", 404


if __name__ == "__main__":
    app.run(debug=True)

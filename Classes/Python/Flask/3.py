from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Route for file upload form
@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"
        file = request.files["file"]
        if file.filename == "":
            return "No selected file"
        if file:
            # Save the file
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
            return redirect(url_for("uploaded_files"))
    return render_template("upload.html")


# Route to display list of uploaded files
@app.route("/files")
def uploaded_files():
    # List all files in the upload folder
    files = os.listdir(app.config["UPLOAD_FOLDER"])
    return render_template("files.html", files=files)


if __name__ == "__main__":
    app.run(debug=True)

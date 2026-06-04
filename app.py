from flask import Flask, render_template, request
from sql_generator import generate_sql
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    generated_sql = ""
    results = None
    error = ""

    if request.method == "POST":

        question = request.form["question"]

        try:
            generated_sql = generate_sql(question)

            conn = sqlite3.connect("employees.db")

            results = pd.read_sql_query(
                generated_sql,
                conn
            )

            conn.close()

        except Exception as e:
            error = str(e)

    return render_template(
        "index.html",
        sql=generated_sql,
        results=results,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
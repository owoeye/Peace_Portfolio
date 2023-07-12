from flask import Flask, render_template, request
# import requests
import smtplib
import os

app = Flask(__name__)

MY_MAIL = os.environ.get("MY_MAIL")
PASSWORD = os.environ.get("PASSWORD")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_MAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=email,
                to_addrs=MY_MAIL,
                msg=f"Subject:{subject}\n\n"
                    f"Name: {name}\n"
                    f"Email: {email}\n"
                    f"Message: {message}\n"
            )
            return render_template("index.html", msg_sent=True)

    else:
        return render_template("index.html", msq_sent=False)
    # return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

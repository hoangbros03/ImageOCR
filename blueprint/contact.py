from flask import Blueprint, Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField

import pandas as pd
import uuid
import requests
import config

contact_bp = Blueprint("contact", __name__)


class ContactForm(FlaskForm):
    """
    Every field needed in the contact form
    """

    name = StringField("Name")
    email = StringField("Email")
    subject = StringField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")


@contact_bp.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        object_to_save = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message,
        }
        mail = pd.DataFrame(object_to_save, index=[0])
        mail.to_csv("contactMails/" + str(uuid.uuid4()) + ".csv")

        return render_template("contact-success.html")
    else:
        return render_template("contact.html", form=form, my_email=config.EMAIL_RECEIVE)

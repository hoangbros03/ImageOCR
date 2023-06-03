from flask import Blueprint, Flask, render_template, request
from flask_mail import  Message
from app import mail

contact_bp = Blueprint("contact", __name__)

@contact_bp.route('/contact', methods=['GET','POST'])
def contact():
    if request.method =="POST":
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        
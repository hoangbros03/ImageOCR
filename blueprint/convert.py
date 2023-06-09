from flask import Blueprint, Flask, render_template, request, send_from_directory
from flask_wtf import FlaskForm
import pandas as pd
import uuid
from pdf2image import convert_from_path
import config
import os
from zipfile import ZipFile

pdf2image_bf = Blueprint("convert", __name__)


@pdf2image_bf.route("/convert", methods=["GET", "POST"])
def convert():
    """
    Show website when user go to "/convert" page
    """
    if request.method == "POST":
        file = request.files["file"]
        # Check if file is pdf
        file_name = file.filename
        file_extension = file_name.split(".")[-1]
        print("test")
        if file_extension != "pdf":
            return render_template("cvt-fail.html")

        file_name = str(uuid.uuid4())
        if not os.path.exists("uploads/pdf"):
            os.makedirs("uploads/pdf")

        filepath = "uploads/pdf/" + file_name + ".pdf"
        file.save(filepath)

        pages = convert_from_path(filepath)

        images = []
        if not os.path.exists(f"pdf_images/{file_name}"):
            os.makedirs(f"pdf_images/{file_name}")

        for i, page in enumerate(pages):
            image_path = os.path.join("pdf_images/", file_name, f"{i}.jpg")
            page.save(image_path)
            images.append(image_path)

        # zip file
        zip_file_path = f"pdf_images/{file_name}/{file_name}.zip"
        with ZipFile(zip_file_path, "w") as zip:
            for file in images:
                zip.write(file)

        return render_template(
            "cvt-success.html", images=images, zip_file_path=zip_file_path
        )
    else:
        return render_template("pdf2image.html")


@pdf2image_bf.route("/pdf_images/<dir1>/<dir2>")
def get_zip_file(dir1, dir2):
    """
    Return the zip file with specified local url
    Args:
    dir1, dir2: like the route above
    Return:
    File that specified. Can be any file.
    """
    return send_from_directory("pdf_images/" + dir1, dir2)

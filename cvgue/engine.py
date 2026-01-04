from jinja2 import Environment, FileSystemLoader
import os
from typing import Literal
from weasyprint import HTML, CSS

TEMPLATE_TYPE = Literal["ats", "creative"]

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(THIS_DIR, "templates")


def create_cv(
    data: dict, template_type: TEMPLATE_TYPE = "ats", output_path: str = "cv.pdf"
):

    # TEMPLATE PATH
    template_path = os.path.join(TEMPLATE_DIR, template_type)

    jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)

    template = jinja_env.get_template("template.html")
    html_content = template.render(**data)

    # CSS PATH
    css_path = os.path.join(template_path, "styles.css")
    css = CSS(filename=css_path)

    # EXPORT CV
    HTML(string=html_content, base_url=template_path).write_pdf(
        output_path, stylesheets=[css]
    )

from flask import Blueprint, render_template, flash
from models.projects import Project
from models.KeyValue import KeyValue
from forms import ContactForm
home = Blueprint('home', __name__)

languages = [KeyValue("HTML", "90%"), KeyValue(
    "Python", "80%"), KeyValue("GML", "75%"), KeyValue("JavaScript", "75%"),
    KeyValue("SQL", "65%"), KeyValue("ReactJS", "65%"), KeyValue("NodeJS", "55%"), KeyValue("CSS", "50%"), KeyValue("Git", "35%")]

frameworks = [KeyValue("Bootstrap", "100%"), KeyValue("VSCode", "95%"), KeyValue("Jinja", "90%"), KeyValue("Flask", "85%"), KeyValue(
    "Flask-WTForms", "85%"), KeyValue("Flask-SQLAlchemy", "85%"), KeyValue("Axios", "80%"), KeyValue("PostgreSQL", "75%"),
    KeyValue("Heroku", "70%"), KeyValue("jQuery", "65%"), KeyValue("Express", "55%")]

projects = [Project("Meads' Meal-kit Planner", "Python, SQL, HTML, CSS, JavaScript", "../static/mealPlannerLogo.jpg", "https://meads-meal-planner-app.herokuapp.com/"), Project("JeoTool/Game Show Creator", "Node, React, SQL, HTML, CSS", "../static/jeotool.png", "https://jeotool.herokuapp.com/"),
            Project("Guess The Capital", "HTML, CSS, JavaScript", "../static/guessthatcapitalLogo.jpg", "https://ameads21.github.io/guess-the-capital/"), Project(
    "Conquest", "GML", "../static/conquestLogo.jpg", "https://ameads21.github.io/conquest/")]


def flash_errors(form):
    # flash("testing", "danger")
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            return flash(error, 'danger')


@home.route('/', methods=['GET', 'POST'])
def home_page():
    form = ContactForm()
    if form.validate_on_submit():
        raise
    else:
        flash_errors(form)
    return render_template('index.html', projects=projects, languages=languages, frameworks=frameworks, form=form)

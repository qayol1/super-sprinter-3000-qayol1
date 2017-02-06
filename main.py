import os

from flask import *

from build import Build
from create_html import Create_html
from story import Story

app = Flask(__name__, static_url_path="", static_folder="static")
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default',
    DEBUG='True'))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/')
@app.route('/list')
def show_start_html():
    Create_html.create_list_html()
    return render_template('list.html')


@app.route('/story')
def show_form_thml():
    Create_html.create_form_html()
    return render_template('form.html')


@app.route('/save_story', methods=['POST'])
def save_story():
    if request.method == 'POST':
        story_title = request.form['story_title']
        user_story = request.form['user_story']
        acceptance_criteria = request.form['acceptance_criteria']
        business_value = request.form['business_value']
        estimation_hour = request.form['estimation_hour']
        status = request.form['status']
        story = Story(title=story_title, description=user_story, acceptance_criteria=acceptance_criteria,
                      business_value=business_value, estimation_hour=estimation_hour, status=status)
        story.save()
        return redirect("/list")


@app.route('/delete/<story_id>')
def del_story(story_id):
    story = Story.get(Story.id == story_id)
    story.delete_instance()
    return redirect("/list")


@app.route('/story/<story_id>')
def create_update_form_html(story_id):
    Create_html.create_form_html(story_id)
    return render_template('form.html')


@app.route('/story/update_story/<story_id>', methods=['POST'])
def update_story(story_id):
    if request.method == 'POST':
        story_title = request.form['story_title']
        user_story = request.form['user_story']
        acceptance_criteria = request.form['acceptance_criteria']
        business_value = request.form['business_value']
        estimation_hour = request.form['estimation_hour']
        status = request.form['status']
        story = Story.update(title=story_title, description=user_story, acceptance_criteria=acceptance_criteria,
                             business_value=business_value, estimation_hour=estimation_hour, status=status).where(
            Story.id == story_id)
        story.execute()
        return redirect("/list")


if __name__ == '__main__':
    Build.create_table()
    app.run()

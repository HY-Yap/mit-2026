from flask import Flask, render_template, request, url_for
from planner import generate_training_plan, get_scoring_data, parse_time_str, seconds_to_time

app = Flask(__name__)


DEFAULT_FORM_VALUES = {
    "age": "18",
    "weeks": "8",
    "current_pushups": "20",
    "current_situps": "20",
    "current_run": "15:00",
    "target_pushups": "40",
    "target_situps": "40",
    "target_run": "14:00",
}


def form_values(source):
    return {
        key: source.get(key, default)
        for key, default in DEFAULT_FORM_VALUES.items()
    }


def render_form(values=None):
    return render_template(
        "index.html",
        scoring_data=get_scoring_data(),
        values=values or DEFAULT_FORM_VALUES,
    )


@app.route("/")
def index():
    return render_form(form_values(request.args))


@app.route("/fitness")
def fitness():
    return render_form(form_values(request.args))


@app.route('/result', methods=['POST'])
def result():
    form = request.form
    values = form_values(form)
    try:
        current_pushups = int(form.get('current_pushups', 0))
        current_situps = int(form.get('current_situps', 0))
        target_pushups = int(form.get('target_pushups', 0))
        target_situps = int(form.get('target_situps', 0))
        weeks = int(form.get('weeks', 8))
        current_run = parse_time_str(form.get('current_run', '15:00'))
        target_run = parse_time_str(form.get('target_run', '14:00'))
        age = int(form.get('age', 18))
    except Exception:
        return "Invalid input", 400

    if current_run is None or target_run is None:
        return "Invalid run timing", 400

    plan = generate_training_plan(
        current_pushups,
        target_pushups,
        current_situps,
        target_situps,
        current_run,
        target_run,
        weeks,
        age,
    )

    back_url = url_for('fitness', **values)

    return render_template('result.html',
                            plan=plan,
                            current_run=current_run,
                            target_run=target_run,
                            seconds_to_time=seconds_to_time,
                            back_url=back_url)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request

import utils

app = Flask(__name__)


@app.route('/')
def index():
    candidates = utils.get_all_candidates()
    return render_template('index.html', candidates=candidates)



@app.route('/candidates/<int:pk>')
def candidate(pk):
    candidate = utils.get_candidate_pk(pk)
    return render_template('candidate.html', candidate=candidate)

@app.route('/search/')
@app.route('/search/<name>')
def candidate_name(name=None):
    if name is None:
        name = request.args.get('name')
    candidates = utils.get_candidates_by_name(name)
    return render_template('search.html', candidates=candidates, count_names=len(candidates))


@app.route('/skill/<skill_name>')
def candidate_skill(skill_name=None):
    candidates_skill = utils.get_candidates_by_skill(skill_name)
    return render_template('search.html', candidates=candidates_skill, count_names=len(candidates_skill))


if __name__ == "__main__":
    app.run(debug=True)

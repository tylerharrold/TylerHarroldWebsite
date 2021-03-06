from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('landing_page.html')

@app.route("/projects")
def projects():
	return render_template('projects_page.html')

@app.route("/construction")
def construction():
	return render_template('under_construction.html')

if __name__ == "__main__":
	app.run()

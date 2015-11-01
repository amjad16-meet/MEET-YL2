from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
app = Flask(__name__)




@app.route('/')
def index():
	return render_template('home.html')


@app.route('/aboutme/')
def aboutme():
	return render_template('aboutme.html')


@app.route('/contactme/')
def contact():
	return render_template('contactme.html')




@app.route('/post/')
def post():
	email = request.form['email']
	facebook = request.form['facebook']
	return render_template('post.html',email=email,facebook=facebook)






if __name__ == '__main__':
        app.debug = True	
        app.run()

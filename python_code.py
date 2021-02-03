from flask import Flask,render_template, request, redirect, url_for
app= Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')
	#return 'hello'

@app.route('/rule', methods=["POST","GET"])
def rule():
	if request.method=="POST":
		user=request.form["user"]
		print(user)
		return redirect(url_for("user",usr=user))
	else:
		return render_template("rule.html")

@app.route("/<usr>")
def user(usr):
	return render_template("rule.html",name=usr)

if __name__ == '__main__':
	app.run(debug=True)
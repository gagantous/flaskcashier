from flask import Flask as fl, render_template as render, request

app = fl(__name__)

@app.route('/')
def hello():
	return render('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
    _username = request.form.get('username')  # get(attr) returns None if attr is not present
 
    # Validate and send response
    if _username:
        return render('process.html', username=_username)
    else:
        return 'Please go back and enter your name...', 400  # 400 Bad Request



if __name__ == "__main__":
	app.run(debug=True)
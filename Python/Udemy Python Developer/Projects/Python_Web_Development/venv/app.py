from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def route():
    return redirect('http://127.0.0.1:5000/index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

def get_data():
    with open("data.json", "r", encoding="UTF-8") as handel:
        return json.load(handel)

def add_post(post):
    data = get_data()
    data.append(post)
    with open("data.json", "w", encoding="UTF-8") as handel:
        handel.write(json.dumps(data))

@app.route('/')
def index():
    blog_posts = get_data()
    return render_template('index.html', posts=blog_posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        add_post(dict(request.form))
        return redirect(url_for('index'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

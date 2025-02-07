from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

def get_data():
    with open("data.json", "r", encoding="UTF-8") as handel:
        return json.load(handel)

def add_post(post):
    data = get_data()
    ids = [post["id"] for post in data]
    post["id"] = max(ids) + 1
    data.append(post)
    with open("data.json", "w", encoding="UTF-8") as handel:
        handel.write(json.dumps(data))

def delete_post(post_id):
    data = get_data()
    filtered_data = [post for post in data if post["id"] != post_id]
    with open("data.json", "w", encoding="UTF-8") as handel:
        handel.write(json.dumps(filtered_data))


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

@app.route('/delete/<int:post_id>')
def delete(post_id):
    delete_post(post_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

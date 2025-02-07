from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

def get_data():
    with open("data.json", "r", encoding="UTF-8") as handel:
        return json.load(handel)

def write_data(data):
    with open("data.json", "w", encoding="UTF-8") as handel:
        handel.write(json.dumps(data))

def add_post(post):
    data = get_data()
    ids = [post["id"] for post in data]
    post["id"] = max(ids) + 1
    data.append(post)
    write_data(data)

def fetch_post_by_id(post_id):
    data = get_data()
    post = [post for post in data if post["id"] == post_id][0]
    return post

def delete_post(post_id):
    data = get_data()
    filtered_data = [post for post in data if post["id"] != post_id]
    write_data(filtered_data)


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


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    # Fetch the blog posts from the JSON file
    post = fetch_post_by_id(post_id)
    if post is None:
        # Post not found
        return "Post not found", 404

    if request.method == 'POST':
    # Update the post in the JSON file
    # Redirect back to index
        updated_post = dict(request.form)
        updated_post["id"] = post_id
        data = get_data()
        data.remove(post)
        data.append(updated_post)
        write_data(data)
        return redirect(url_for('index'))


    # Else, it's a GET request
    # So display the update.html page
    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

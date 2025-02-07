from flask import Flask, render_template, request, redirect, url_for
from data_management import get_data, add_post, delete_post, fetch_post_by_id, update_post

app = Flask(__name__)



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
        updated_post = dict(request.form)
        updated_post["id"] = post_id
        updated_post["nb_likes"] = post["nb_likes"]
        update_post(updated_post)
        return redirect(url_for('index'))
    return render_template('update.html', post=post)



@app.route('/like/<int:post_id>')
def like(post_id):
    post = fetch_post_by_id(post_id)
    post["nb_likes"] += 1
    update_post(post)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

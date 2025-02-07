import json


def get_data():
    with open("data.json", "r", encoding="UTF-8") as handel:
        data = json.load(handel)
        data.sort(key=lambda x:x["id"])
        return data


def write_data(data):
    with open("data.json", "w", encoding="UTF-8") as handel:
        handel.write(json.dumps(data))


def add_post(post):
    data = get_data()
    ids = [post["id"] for post in data]
    post["id"] = max(ids) + 1
    post["nb_likes"] = 0
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


def update_post(updated_post):
    data = get_data()
    data = [post for post in data if post["id"] != updated_post["id"]]
    data.append(updated_post)
    write_data(data)
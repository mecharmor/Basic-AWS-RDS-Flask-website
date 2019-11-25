from flask import Flask
from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

# PATH_TO_DATABASE = './proxy/database.json'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    # admin_username = request.form.get("admin_username")
    # admin_password = request.form.get("admin_password")
    # blocked_site = request.form.get("blocked_site")
    # clear_cache = request.form.get("clear_cache")
    # user_username = request.form.get("user_username")
    # user_password = request.form.get("user_password")
    # new_site = request.form.get("new_site")

    return redirect("/main")


# @app.route("/main")
# def proxy_settings():
#     # pm = ProxyManager(PATH_TO_DATABASE) 
    
#     return render_template("proxy-settings.html",
#                             cached_sites = pm.list_of_cached_sites(),
#                             blocked_sites = pm.list_of_blocked_sites(),
#                             admins = pm.list_of_admins(),
#                             private_mode_users = pm.list_of_managers(),
#                             manager_sites = pm.list_of_manager_sites())


@app.route("/home.html", methods=["POST"])
def get_user_input():
    # fetch user credentials
    # username = request.form.get("username")
    # password = request.form.get("password")

    # url = request.form.get("url")
    # is_private_mode = 0
    # if request.form.get("private"):
    #     is_private_mode = 1
    # if "proxy-settings" in url:
    #     return proxy_settings()
    # data = {"url": url, "is_private_mode": is_private_mode, "username": username, "password": password}
    # client = Client()
    # client.request_to_proxy(data)

    # return client.response_from_proxy()

    return ""


if __name__ == "__main__":
    app.run()


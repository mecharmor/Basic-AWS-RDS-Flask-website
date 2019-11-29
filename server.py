from flask import Flask
from flask import Flask, render_template, request, redirect
import requests
import sqlite3

conn = sqlite3.connect('./db/main.db')
db = conn.cursor()
app = Flask(__name__)

def query(string):
    db.execute(string) # run SQL query
    conn.commit() # save changes
    return db.fetchone() # returns None if query is empty

def generate_db():
    query('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''') # Create table
    query("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)") # Insert a row of data

@app.route("/")
def home():
    return redirect("/main")

@app.route("/main")
def main():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    # sample = request.form.get("sample")
    return redirect("/main")
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


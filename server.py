from flask import Flask
from flask import Flask, render_template, request, redirect
import requests
app = Flask(__name__)
import pymysql

class Database:
    def __init__(self):
        host = "rds-mysql-csc675.c4pugfa5ehgs.us-west-1.rds.amazonaws.com"
        user = "CSC675Database"
        password = "management"
        db = "sys"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()
    def query(self, string):
        self.cur.execute(str(string))
        return self.cur.fetchall()

    def getEmployees(self):
        return self.query("SELECT * FROM sys.Employee;")
    def getOrders(self):
        return self.query("SELECT * FROM sys.Orders;")
    def getMenu(self):
        return self.query("SELECT * FROM sys.Menu;")
    def getMenuItems(self):
        return self.query("SELECT * FROM sys.Menu_Item;")
    def getEmployeeTypes(self):
        return self.query("SELECT * FROM sys.Employee_Type;")
    def getInventory(self):
        return self.query("SELECT * FROM sys.Inventory;")
    def completeOrder(self, order_id):
        self.query("UPDATE Orders O SET O.Order_is_complete = 1 WHERE O.order_id = " + order_id + ";")

db = Database()

@app.route("/")
def home():
    return redirect("/main")

@app.route("/main")
def main():
    return render_template("index.html", menu = db.getMenu())

@app.route("/employee")
def employee():
    return render_template("employee.html", 
                            employees = db.getEmployees(), 
                            employee_types = db.getEmployeeTypes() ) 

@app.route("/order")
def order():
    return render_template("order.html", 
                            orders = db.getOrders() ) 

@app.route("/inventory")
def inventory():
    return render_template("inventory.html", 
                            inventory = db.getInventory() ) 

@app.route("/order", methods=["POST"])
def place_order():
    order_sample = request.form.get("order_sample")
    print("Sample output: " + str(order_sample))

    return redirect("/order")

@app.route("/complete_order", methods=["POST"])
def complete_order():
    order_id = request.form.get("order_id")

    print("id: " + str(order_id))

    return redirect("/order")

if __name__ == "__main__":
    app.run()









# import sqlite3

# conn = sqlite3.connect('./db/main.db')
# db = conn.cursor()

# def query(string):
#     db.execute(string) # run SQL query
#     conn.commit() # save changes
#     return db.fetchone() # returns None if query is empty

# def generate_db():
#     query('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''') # Create table
#     query("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)") # Insert a row of data


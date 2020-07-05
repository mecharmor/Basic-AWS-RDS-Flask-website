from flask import Flask
from flask import Flask, render_template, request, redirect
import requests
app = Flask(__name__)
import pymysql
import random

class Database:
    def __init__(self):
        host = "host_info_here"
        user = "user_name_here"
        password = "password_here"
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
        return self.query("""
            SELECT 
            O.order_id AS order_number,
            E.first_name AS cashier_name,
            O.receipt_id AS receipt,
            SUM(M.cost) AS total_cost,
            O.order_is_complete AS completed
            FROM sys.Employee E
            INNER JOIN sys.Orders O ON E.employee_id = O.employee_id
            INNER JOIN sys.Menu M ON O.menu_id = M.menu_id
            GROUP BY O.receipt_id;
                         """)
    def getMenu(self):
        return self.query("SELECT * FROM sys.Menu;")
    def getMenuItems(self):
        return self.query("SELECT * FROM sys.Menu_Item;")
    def getEmployeeTypes(self):
        return self.query("SELECT * FROM sys.Employee_Type;")
    def getInventory(self):
        return self.query("SELECT * FROM sys.Inventory;")
    def completeOrder(self, receipt):
        self.query(r"UPDATE sys.Orders O SET O.order_is_complete=1 WHERE O.receipt_id='" + str(receipt) + r"';")
    def markIncompleteOrder(self, receipt):
        self.query(r"UPDATE sys.Orders O SET O.order_is_complete=0 WHERE O.receipt_id='" + str(receipt) + r"';")

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
    receipt = "%032x" % random.getrandbits(127) # generated receipt
    print("Sample output: " + str(order_sample))

    return redirect("/order")

@app.route("/complete_order", methods=["POST"])
def complete_order():
    receipt = request.form.get("receipt")
    db.completeOrder(receipt)
    return redirect("/order")

@app.route("/incomplete_order", methods=["POST"])
def incomplete_order():
    receipt = request.form.get("receipt")
    db.markIncompleteOrder(receipt)
    return redirect("/order")

if __name__ == "__main__":
    app.run()



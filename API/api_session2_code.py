from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234567890",
    database="db2"
)


@app.route('/customers', methods=['GET'])
def get_customers():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM db2.customers")
    results = cursor.fetchall()
    return jsonify(results)


@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM db2.customers WHERE CusID = {id}")
    result = cursor.fetchone()
    return jsonify(result)


@app.route('/customers', methods=['POST']) # Create a route for the application
def add_customer(): # Create a function to add a new customer
    data = request.get_json() # Get the JSON data
    cursor = mydb.cursor() # Create a cursor object
    query = "INSERT INTO db2.customers (CusID, CusName, Gender, Phone, Address) VALUES (%s, %s, %s, %s, %s)" # Create the query
    values = (data['CusID'], data['CusName'], data['Gender'], data['Phone'], data['Address']) # Get the values from the JSON data
    cursor.execute(query, values) # Execute the query
    mydb.commit()  # Commit the changes
    return jsonify({'message': 'Customer added successfully'}) # Return a message


@app.route('/customers/<int:id>', methods=['PUT']) # Create a route for the application
def update_customer(id): # Create a function to update a customer
    data = request.get_json() # Get the JSON data
    cursor = mydb.cursor() # Create a cursor object
    query = "UPDATE db2.customers SET CusName = %s, Gender = %s, Phone = %s, Address = %s WHERE CusID = %s" # Create the query
    values = (data['CusName'], data['Gender'], data['Phone'], data['Address'], id) # Get the values from the JSON data
    cursor.execute(query, values) # Execute the query
    mydb.commit() # Commit the changes
    return jsonify({'message': 'Customer updated successfully'}) # Return a message


@app.route('/customers/<int:id>', methods=['DELETE']) # Create a route for the application
def delete_customer(id): # Create a function to delete a customer
    cursor = mydb.cursor() # Create a cursor object
    cursor.execute(f"DELETE FROM db2.customers WHERE CusID = {id}") # Execute the query
    mydb.commit() # Commit the changes
    return jsonify({'message': 'Customer deleted successfully'}) # Return a message


if __name__ == '__main__':
    app.run(debug=True)
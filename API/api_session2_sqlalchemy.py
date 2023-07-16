from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a Flask application instance named app.
app = Flask(__name__)
engine = create_engine('mysql+mysqlconnector://root:1234567890@localhost/db2')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Customer(Base):
    __tablename__ = 'customers'
    CusID = Column(Integer, primary_key=True)
    CusName = Column(String(255))
    Gender = Column(String(1))
    Phone = Column(String(255))
    Address = Column(String(255))

class Product(Base):
    __tablename__ = 'products'
    ProductID = Column(Integer, primary_key=True)
    ProductName = Column(String(255))
    StockQty = Column(Integer)
    UnitPrice = Column(Float)
    Discount = Column(Float)

@app.route('/products', methods=['GET'])
def get_products():
    products = session.query(Product).all()
    results = [
        {
            'ProductID': product.ProductID,
            'ProductName': product.ProductName,
            'StockQty': product.StockQty,
            'UnitPrice': product.UnitPrice,
            'Discount': product.Discount
        }
        for product in products
    ]
    return jsonify(results)

# Retrieve all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    customers = session.query(Customer).all()
    results = [
        {
            'CusID': customer.CusID,
            'CusName': customer.CusName,
            'Gender': customer.Gender,
            'Phone': customer.Phone,
            'Address': customer.Address
        }
        for customer in customers
    ]
    return jsonify(results)

# Retrieve a specific customer by ID
@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    customer = session.query(Customer).get(id)
    if customer:
        result = {
            'CusID': customer.CusID,
            'CusName': customer.CusName,
            'Gender': customer.Gender,
            'Phone': customer.Phone,
            'Address': customer.Address
        }
        return jsonify(result)
    else:
        return jsonify({'message': 'Customer not found'})

# Add a new customer
@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.get_json()
    customer = Customer(
        CusID=data['CusID'],
        CusName=data['CusName'],
        Gender=data['Gender'],
        Phone=data['Phone'],
        Address=data['Address']
    )
    session.add(customer)
    session.commit()
    return jsonify({'message': 'Customer added successfully'})

# Update an existing customer
@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    data = request.get_json()
    customer = session.query(Customer).get(id)
    if customer:
        customer.CusName = data['CusName']
        customer.Gender = data['Gender']
        customer.Phone = data['Phone']
        customer.Address = data['Address']
        session.commit()
        return jsonify({'message': 'Customer updated successfully'})
    else:
        return jsonify({'message': 'Customer not found'})

# Delete a customer
@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = session.query(Customer).get(id)
    if customer:
        session.delete(customer)
        session.commit()
        return jsonify({'message': 'Customer deleted successfully'})
    else:
        return jsonify({'message': 'Customer not found'})


if __name__ == '__main__':
    app.run(debug=True)
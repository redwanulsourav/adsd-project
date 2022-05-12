import pymongo
from bson.objectid import ObjectId
from app.models import *

# Mongo database
client = pymongo.MongoClient("mongodb+srv://rsourave:ncc3xtDvl5YnT5bY@cluster0.m125c.mongodb.net/orders?retryWrites=true&w=majority")
db = client.orders

def getuser(username):
    user = db.users.find_one({'username':username})
    print(user)
    if user is not None:
        return User(username, user['password'])
    else:
        return None

def insert_order(order):
    db.orders.insert_one(
        {
            'customer_name':order.customer_name, 
            'unit_price':order.unit_price, 
            'quantity':order.quantity, 
            'product_name':order.product_name,
            'total_price':order.quantity * order.unit_price
        })

def get_all_orders():
    orders = db.orders.find({})
    return orders
def delete_single_order(order_id):
    db.orders.delete_one({
        '_id':ObjectId(order_id)
    })
    
def get_single_order(order_id):
    order = db.orders.find_one({'_id': ObjectId(order_id)})
    print(order['_id'])
    return order

def update_order(order_id, new_order):
    query = {
        '_id' : ObjectId(order_id)
    }

    updated_value = {
        '$set': {
            'customer_name': new_order.customer_name,
            'unit_price': new_order.unit_price,
            'quantity':new_order.quantity,
            'product_name': new_order.product_name,
            'total_price':new_order.unit_price * new_order.quantity
        }
    }
    
    #print(updated_value)
    queried = db.orders.update_one(query, updated_value)
    #print('order_id',order_id)
    #print(queried)

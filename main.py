import pymongo

CONNECTION_STRING = 'mongodb+srv://<username>:<password>@cluster0.m125c.mongodb.net/<database_name>?retryWrites=true&w=majority'
# client = pymongo.MongoClient("")

# db = client.test



def parse_secrets():
    f = open('SECRETS.txt')
    contents = f.read()
    f.close()

    contents = contents.split('\n')
    assert(len(contents) == 2), 'Incorrect secret file format'

    username = contents[0].split('=')
    assert(len(username) == 2), 'Incorrect secret file format'
    assert(username[0] == 'USERNAME'), 'Incorrect secret file format'

    password = contents[1].split('=')
    assert(len(password) == 2), 'Incorrect secret file format'
    assert(password[0] == 'PASSWORD'), 'Incorrect secret file format'

    return {
        'username': username[1],
        'password': password[1]
    }


def insert_order(mongo_client):
    product_name = input('Please enter the product name ')
    # price = input('Please enter the product price')
    customer_first_name = input('Please enter the customer\'s first name ')
    customer_last_name = input('Please enter the customer\'s last name ')
    quantity = input('Please enter the quantity ')
    unit_price = input('Please enter the unit price ')

    order = {
        'product_name': product_name,
        'customer': {
            'first_name': customer_first_name,
            'last_name': customer_last_name
        },
        'quantity': quantity,
        'unit_price': unit_price
    }

    print(mongo_client.orders.insert_one(order).inserted_id)

    

def main():
    secrets = parse_secrets()
    CONNECTION_STRING.replace('<password>', secrets['password'].strip())
    CONNECTION_STRING.replace('<username>', secrets['username'].strip())
    CONNECTION_STRING.replace('<database_name>','orders')
    client = pymongo.MongoClient(
        "mongodb+srv://rsourave:ncc3xtDvl5YnT5bY@cluster0.m125c.mongodb.net/orders?retryWrites=true&w=majority")
    db = client.orders
    print(db.orders)
    id_ = db.orders.insert_one({'name': 'value'}).inserted_id
    print(id_)
    insert_order(db)
    
if __name__ == '__main__':
    main()


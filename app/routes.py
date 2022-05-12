from flask import render_template, flash, redirect, url_for, session, current_app
from werkzeug.utils import send_from_directory
from app import app
from flask_login import current_user, login_user, logout_user, login_required
# from app.models import *    
from app.forms import *
from datetime import datetime
# from app import db
from flask import request
import random
import json
import os
from app.database_interface import *


@app.route('/login', methods=['GET','POST'])
def login_view_method():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        user = getuser(username)
        print(user)
        print(form.password.data)
        print(user.password)
        if user is None or user.password != form.password.data:
            return redirect(url_for('login_view_method'))
        print('login successful')
        return redirect(url_for('add_new_order'))
        
    return render_template('login.html',form = form)

@app.route('/logout')
def logout():
    pass

@app.route('/view_all_orders', methods=['GET', 'POST'])
def view_all_orders():
    orders = get_all_orders()
    data = {
        'active_page':'view_all_orders',
        'page_title':'View All Orders',
        'orders' : orders
    }
    print(orders)
    return render_template('view_all_orders.html', data=data)


@app.route('/edit_order/<order_id>', methods=['GET', 'POST'])
def edit_order(order_id):
    order = get_single_order(order_id)
    print(order['customer_name'])
    data = {
        'active_page':'edit_order',
        'page_title':'Edit Order',
        'order' : order
    }

    form = EditOrderForm()
    
    if form.validate_on_submit():
        new_order = Order()
        new_order.customer_name = form.customer_name.data
        new_order.unit_price = form.unit_price.data
        new_order.quantity = form.quantity.data
        new_order.product_name = form.product_name.data

        update_order(order_id, new_order)
        return redirect(url_for('view_all_orders'))
    return render_template('edit_order.html',data=data, form = form)
    # return render_template('view_all_orders.html', data=data)
@app.route('/delete_order/<order_id>', methods=['GET', 'POST'])
def delete_order(order_id):
    delete_single_order(order_id)
    return redirect(url_for('view_all_orders'))


@app.route('/add_new_order', methods=['GET', 'POST'])
def add_new_order():
    
    form = NewOrderForm()

    data = {
        'active_page':'add_new_order',
        'page_title':'Add New Order',
    }
    if form.validate_on_submit():
    #     customer_id = int(form.customer_id.data)
        
    #     order = CustomerOrder(product_name = form.product_name.data, customer_id = customer_id)
    #     order.customer_first_name = User.query.filter_by(id=form.customer_id.data).first().first_name
    #     order.customer_last_name = User.query.filter_by(id=form.customer_id.data).first().last_name
    #     order.exchange_rate = User.query.filter_by(id=form.customer_id.data).first().exchange_rate
    #     order.weight_rate = User.query.filter_by(id=form.customer_id.data).first().weight_rate
        new_order = Order()
        if form.product_name.data is not None:
            new_order.product_name = form.product_name.data
        
    #     if form.platform_link.data is not None:
    #         order.platform_link = form.platform_link.data
        
    #     if form.order_ref.data is not None:
    #         order.order_ref = form.order_ref.data
        
        if form.unit_price.data is not None:
            new_order.unit_price = form.unit_price.data

        if form.quantity.data is not None:
            new_order.quantity = form.quantity.data
        
        if form.customer_name.data is not None:
            new_order.customer_name = form.customer_name.data
        
        insert_order(new_order)
        # return redirect(url_for('admin_view_all_orders'))
    return render_template('add_new_order.html', data=data, form=form)

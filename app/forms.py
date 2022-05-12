from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, Optional

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')

class NewOrderForm(FlaskForm):
    quantity = IntegerField('Quantity', validators=[Optional(),])
    product_name = StringField('Product Name', validators=[Optional(),])
    customer_name = StringField('Customer Name',validators=[DataRequired()])
    weight = FloatField('Weight',validators=[Optional(),])
    unit_price = FloatField('Unit Price',validators=[DataRequired(),])
    submit_add_order_form = SubmitField('Submit')

class EditOrderForm(FlaskForm):
    quantity = IntegerField('Quantity', validators=[Optional(),])
    product_name = StringField('Product Name', validators=[Optional(),])
    customer_name = StringField('Customer Name',validators=[DataRequired()])
    weight = FloatField('Weight',validators=[Optional(),])
    unit_price = FloatField('Unit Price',validators=[DataRequired(),])
    submit_edit_order_form = SubmitField('Submit')


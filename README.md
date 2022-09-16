# EcommerceAPI
ECommerce’s API platform provides many products, and resources that enable you to harness the power of ECommerce’s open, global, and real-time network.
This page describes what’s possible to build with the different API endpoints that are available on the platform, and how to get the access and information that you need to get started.
We regularly update and improve the experience and products available on the platform. These improvements make it important for you to stay informed so you don’t miss any updates.
Here you can Signup, Login, Add, View, Update and Delete Products. In this API there's two type of User, AdminUser or NormalUser.


<div id="requirements">
<h2>Requirements to use!</h2>
<ol>
    <li>you need to have Python v3, Django v4 and MySQL installed on your machine</li>
    <li>create MySQL database and name it <strong>"ecommerceapi"</strong></li>
    <li>enter your database credentials(password, id, port, db name) in settings.py</li>
    <li>type: pip3 -r install requirements.txt (pip3 because this project runs on python3 and django version 3)</li>
    <li>open your CMD(Command Line) on Windows or Terminal on Mac</li>
    <li>go to the project directory</li>
    <li>type: source env/bin/activate - (to activate virtual env)</li>
    <li>type: cd ecommerce/</li>
    <li>type: python3 manage.py makemigrations</li>
    <li>type: python3 manage.py migrate</li>
    <li>type: python3 manage.py runserver</li>
</ol>
</div>

## Endpoints  Instruction 
Method | Endpoint | Functionanlity
--- | --- | ---
GET | `/api/v1/` | API Documentation

#### User Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/ecom/auth/` | Create an user
GET | `/api/v1/ecom/auth/` | List all users
GET | `/api/v1/ecom/auth/{id}` | User details
PUT | `/api/v1/ecom/auth/{id}` | User update
PATCH | `/api/v1/ecom/auth/{id}` | User partial update
DELETE | `/api/v1/ecom/auth/{id}` | User delete

#### Products Endpoints

Method | Endpoint | Functionality
--- | --- | ---
GET | `/api/v1/ecom/` | List all products
POST | `/api/v1/ecom/product/create` | Creates a product
GET | `/api/v1/ecom/product/detail/{id}/` | Product details
PUT | `/api/v1/ecom/product/update/{id}/` | Product update
PATCH | `/api/v1/ecom/product/update/{id}/` | Product partial update
DELETE | `/api/v1/ecom/product/delete/{id}/` | Product delete

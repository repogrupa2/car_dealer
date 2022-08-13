# car_dealer
Best car rental.

# <Name of the project: Car_dealer>


## Description

This repository contains a website design for a car rental company which allows individuals and companies to rent cars. The project was created 
as a team work at the end of a Python course. Four fans of cars and programming wanted to verify the acquired knowledge by creating a virtual car rental.
Simplicity with the use of basic backend and frontend tools to build the most important functionalities for business and clients - these were the basic 
principles and goals. Thanks to the use of Django / Python, its libraries as well as the Bootstrap framework, it has become possible.


## Technologies used

Django (4.0.6) - the web back-end framework
python-dotenv (0.17.1)
Pillow (9.2.0) - Python Imaging Library
Boostrap3 - the web front-end framework


## Installation

To install the project follow these steps:

use the package manager pip to install all required packages, which are listed in the requirements.txt file:
pip install -r requirements.txt

install Django:
python3 -m pip install Django

check django-admin version to check Django work:
django-admin --version

create virtual environment for the project (open a terminal in your project directory):
python3 -m venv env

activate python environment from env:
/env/Scrips/activate

make necessary migrations:
python manage.py makemigrations
python manage.py migrate

how to get the development environment running?

run the server:

python3 manage.py runserver

click and open the displayed url in your browser

create admin account in the terminal to access superuser:

python3 manage.py createsuperuser


## Usage

For entrepreneur/admin:
	after registering create/add branch(es) where you run your business - use ...button
	view list of the branches - use ...button
	edit/modify/update the branch - use ...button
	delete the branch from the list - use ...button
	
	before adding vehicles to the database create/add brands and then models of the cars, use ...buttons
	you can list them, view, edit and delete
	
	create/add new vehicle(s) to offer - use ...button
	view list of the vehicles - use ...button
	edit/modify/update the vehicle - use ...button
	delete the vehicle from the list - use ...button

	having vehicles, create/add rental offers the customer can view and choose - use ...button
	view list of the offers - use ...button
	edit/modify/update the offer - use ...button
	delete the offer from the list - use ...button
	
	view car_rental list which shows rentings in progress - use ...button

for customer:
	register yourself by entering name, surname and email
	view the list of offers - use ...button
	choose and click for details the offer you are interesed in
	fill in the data required and confirm the offer you accepted, the car rental contract has been concluded, 
	the car is waiting for you in the appropriate branch
		

## Features

The web application allows the user:
    create a new account or log in to an existing one
    view the rental offers
    rent the car she/he choose for required period
and the entrepreneur/admin:
    add, modify and delete the rental offer
    add, modify and delete the branches of the company where the cars are available for the customers


## Credits

List of collaborators and their GitHub profiles:

Piotr Rapinski (https://github.com/piotr-rapinski)
Tomasz Broniak (https://github.com/TomekBr)
Sebastian Kujawa (https://github.com/Sebastian-Kujawa)
Paweł Bąkowski (https://github.com/Pwlbkw)

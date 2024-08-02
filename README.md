# Tailored Donuts Django Project

Welcome to the Tailored Donuts project! This is an ecommerce project for a donut shop named Tailored Donuts, which primarily caters to custom orders and is seasonally present at farmers' markets. The shop is sensitive to gluten and dairy requirements.

## Table of Contents
1. [Introduction](#introduction)
2. [Modules](#modules)
   - [Home](#home)
   - [Menu](#menu)
   - [Inquiry](#inquiry)
   - [Gallery](#gallery)
   - [Reviews/Ratings](#reviews-ratings)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction
The Tailored Donuts Django Project aims to provide a user-friendly platform for managing donut menus, handling customer inquiries, showcasing donut designs through a gallery, and collecting feedback through reviews and ratings.

## Modules

### Home
The Home module serves as the landing page for the Tailored Donuts website. It welcomes visitors, introduces the catering service, and encourages exploration of the menu, gallery, and reviews.

### Menu
The Menu module displays Tailored Donuts' menu items, including customizable donuts, toppings, flavors, and special offers. Customers can browse, customize, and place orders directly from the menu.

### Inquiry
The Inquiry module allows customers to make inquiries about Tailored Donuts' services, pricing, customization options, and event availability. The catering service can manage and respond to inquiries efficiently through this module.

### Gallery
The Gallery module showcases Tailored Donuts' creations, including custom-designed donuts, event setups, customer testimonials, and special promotions. It provides a visual representation of the catering service's capabilities and offerings.

### Reviews/Ratings
The Reviews/Ratings module collects feedback from customers who have enjoyed Tailored Donuts' products and services. Customers can leave reviews, rate their experience, and provide suggestions for improvement, helping the catering service maintain quality and customer satisfaction.

## Setup
To set up and run the Tailored Donuts Django Project locally, follow these steps:
1. Clone the repository: `git clone https://github.com/mikec95/tailoreddonuts.git`
2. Navigate to the project directory: `cd tailoreddonuts`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Apply database migrations: `python manage.py migrate`
7. Create a superuser for admin access: `python manage.py createsuperuser`
8. Start the development server: `python manage.py runserver`
9. Access the project in your web browser: [http://localhost:8000/](http://localhost:8000/)

## Usage
Once the project is set up, you can:
- Log in to the admin panel using the superuser credentials to manage data.
- Navigate through the different modules (Home, Menu, Inquiry, Gallery, Reviews/Ratings) to view and interact with Tailored Donuts' features.
- Customize templates, styles, and functionality as needed to tailor the project to Tailored Donuts' branding and requirements.

## Contributing
Contributions to the Tailored Donuts Django Project are welcome! If you have suggestions, bug fixes, or new features to add, please fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License.

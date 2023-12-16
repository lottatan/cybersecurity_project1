# PIZZA SERVICE

The idea is to create an online pizza service where users can order pizza and drinks.

Once a user has created an account, they can view their past orders, see how much money they've spent in total on the pizza service, view their most ordered pizza and drink, and leave reviews and comments.

On the pizza service website, in addition to placing orders, users can also see given reviews and the average star rating the service has received. The page also displays the most popular pizza and drink.

During an order, users can select 0-5 units of each pizza and drink. The customer must provide their delivery address and detailed arrival instructions.


## Application functions

- Users can register a new account or log in
- If a user is logged in, they can leave comments or reviews
- Anyone can view reviews and comments
- Users can view their order history and favorite products
- It's possible to see PizzaService's most popular pizza and drink

## Application Startup instructions

1. Clone the repository and navigate to its root using the command "cd pizzaservice"

2. Create a new file named ".env" in the root directory and add the following information:

    DATABASE_URL= local-database-url
    SECRET_KEY= secret-key

3. Activate the virtual environment and install the application's dependencies:

        $ python3 -m venv venv
        $ source venv/bin/activate

4. Add the requirements file:
        
        venv $ pip install -r ./requirements.txt

5. If you haven't installed PostgreSQL functions on your computer yet, do it now. The process might be different for different computers, but there are good instructions online.

6. Once you've started the database in another terminal window using the command:

        $ start-pg.sh

7. You can configure the database for the PizzaService repository using the command at the root of the repository:

        venv $ psql < schema.sql

8. Start the application with command:

        venv $ flask run

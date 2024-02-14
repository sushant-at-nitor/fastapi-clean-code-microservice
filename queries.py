from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Customer, Base

# Create an engine and a session factory for the database
engine = create_engine("sqlite:///customers.db")
Session = sessionmaker(bind=engine)


# Define the base class for the queries
class Query:
    # Define the execute method that will be overridden by the subclasses
    def execute(self):
        raise NotImplementedError


# Define the query for getting a customer by id
class GetCustomerQuery(Query):
    # Define the constructor with the parameter
    def __init__(self, customer_id):
        self.customer_id = customer_id

    # Define the execute method that performs the logic
    def execute(self):
        # Create a new session
        session = Session()
        # Query the customer by id
        customer = session.query(Customer).get(self.customer_id)
        # Close the session
        session.close()
        # Return the customer as a dictionary
        return customer.__dict__


# Define the query for getting all customers
class GetAllCustomersQuery(Query):
    # Define the constructor with no parameters
    def __init__(self):
        pass

    # Define the execute method that performs the logic
    def execute(self):
        # Create a new session
        session = Session()
        # Query all customers
        customers = session.query(Customer).all()
        # Close the session
        session.close()
        # Return the customers as a list of dictionaries
        return [customer.__dict__ for customer in customers]

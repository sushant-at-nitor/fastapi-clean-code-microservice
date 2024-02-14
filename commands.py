from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Customer, Base

# Create an engine and a session factory for the database
engine = create_engine("sqlite:///customers.db")
Session = sessionmaker(bind=engine)

# Create the tables if they don't exist
Base.metadata.create_all(engine)


# Define the base class for the commands
class Command:
    # Define the execute method that will be overridden by the subclasses
    def execute(self):
        raise NotImplementedError


# Define the command for creating a customer
class CreateCustomerCommand(Command):
    # Define the constructor with the parameters
    def __init__(
        self,
        id,
        optradio,
        name,
        email,
        phone,
        url,
        tags,
        misc,
        companyId,
        reference,
        intervalNotes,
        bankDetails,
        gst,
        taxId,
    ):
        self.id = id
        self.optradio = optradio
        self.name = name
        self.email = email
        self.phone = phone
        self.url = url
        self.tags = tags
        self.misc = misc
        self.companyId = companyId
        self.reference = reference
        self.intervalNotes = intervalNotes
        self.bankDetails = bankDetails
        self.gst = gst
        self.taxId = taxId

    # Define the execute method that performs the logic
    def execute(self):
        # Create a new session
        session = Session()
        # Create a new customer object with the parameters
        customer = Customer(
            id=self.id,
            optradio=self.optradio,
            name=self.name,
            email=self.email,
            phone=self.phone,
            url=self.url,
            tags=self.tags,
            misc=self.misc,
            companyId=self.companyId,
            reference=self.reference,
            intervalNotes=self.intervalNotes,
            bankDetails=self.bankDetails,
            gst=self.gst,
            taxId=self.taxId,
        )
        # Add the customer to the session
        session.add(customer)
        # Commit the changes
        session.commit()
        # Close the session
        session.close()
        # Return the customer as a dictionary
        return customer.__dict__


# Define the command for updating a customer
class UpdateCustomerCommand(Command):
    # Define the constructor with the parameters
    def __init__(
        self,
        customer_id,
        optradio,
        name,
        email,
        phone,
        url,
        tags,
        misc,
        companyId,
        reference,
        intervalNotes,
        bankDetails,
        gst,
        taxId,
    ):
        self.customer_id = customer_id
        self.optradio = optradio
        self.name = name
        self.email = email
        self.phone = phone
        self.url = url
        self.tags = tags
        self.misc = misc
        self.companyId = companyId
        self.reference = reference
        self.intervalNotes = intervalNotes
        self.bankDetails = bankDetails
        self.gst = gst
        self.taxId = taxId

    # Define the execute method that performs the logic
    def execute(self):
        # Create a new session
        session = Session()
        # Query the customer by id
        customer = session.query(Customer).get(self.customer_id)
        # Update the customer attributes with the parameters
        customer.optradio = self.optradio
        customer.name = self.name
        customer.email = self.email
        customer.phone = self.phone
        customer.url = self.url
        customer.tags = self.tags
        customer.misc = self.misc
        customer.companyId = self.companyId
        customer.reference = self.reference
        customer.intervalNotes = self.intervalNotes
        customer.bankDetails = self.bankDetails
        customer.gst = self.gst
        customer.taxId = self.taxId
        # Commit the changes
        session.commit()
        # Close the session
        session


# Define the command for deleting a customer
class DeleteCustomerCommand(Command):
    # Define the constructor with the parameter
    def __init__(self, customer_id):
        self.customer_id = customer_id

    # Define the execute method that performs the logic
    def execute(self):
        # Create a new session
        session = Session()
        # Query the customer by id
        customer = session.query(Customer).get(self.customer_id)
        # Delete the customer from the session
        session.delete(customer)
        # Commit the changes
        session.commit()
        # Close the session
        session.close()
        # Return a success message
        return f"Customer with id {self.customer_id} deleted successfully"

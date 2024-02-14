from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for the models
Base = declarative_base()

# Define the customer model
class Customer(Base):
    # Specify the table name
    __tablename__ = "customers"

    # Define the columns
    id = Column(Integer, primary_key=True)
    optradio = Column(String)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    url = Column(String)
    tags = Column(String)
    misc = Column(String)
    companyId = Column(String)
    reference = Column(String)
    intervalNotes = Column(String)
    bankDetails = Column(String)
    gst = Column(String)
    taxId = Column(String)

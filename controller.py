from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
from typing import Optional
from commands import CreateCustomerCommand, UpdateCustomerCommand, DeleteCustomerCommand
from queries import GetCustomerQuery, GetAllCustomersQuery
# from routers import customer_router
from view_models import CustomerViewModel

# app = FastAPI()

# Register the customer router
# app.include_router(customer_router)

# Define the endpoints
class CustomerController:
    # @app.post("/customers", response_model=CustomerViewModel)
    @staticmethod
    def create_customer(request: CustomerViewModel):
        # Validate the request data using the view model
        request = CustomerViewModel(**request.dict())
        # Create a command object from the request data
        command = CreateCustomerCommand(
            id=request.id,
            optradio=request.optradio,
            name=request.name,
            email=request.email,
            phone=request.phone,
            url=request.url,
            tags=request.tags,
            misc=request.misc,
            companyId=request.companyId,
            reference=request.reference,
            intervalNotes=request.intervalNotes,
            bankDetails=request.bankDetails,
            gst=request.gst,
            taxId=request.taxId,
        )
        # Invoke the command handler and get the result
        result = command.execute()
        # Return the result as a view model
        return CustomerViewModel(**result)


    #@app.get("/customers/{customer_id}", response_model=CustomerViewModel)
    @staticmethod
    def get_customer(customer_id: int):
        # Create a query object from the customer id
        query = GetCustomerQuery(customer_id)
        # Invoke the query handler and get the result
        result = query.execute()
        # Return the result as a view model
        return CustomerViewModel(**result)


    #@app.get("/customers", response_model=list[CustomerViewModel])
    @staticmethod
    def get_all_customers():
        # Create a query object with no parameters
        query = GetAllCustomersQuery()
        # Invoke the query handler and get the result
        result = query.execute()
        # Return the result as a list of view models
        return [CustomerViewModel(**customer) for customer in result]


    #@app.put("/customers/{customer_id}", response_model=CustomerViewModel)
    @staticmethod
    def update_customer(customer_id: int, request: CustomerViewModel):
        # Validate the request data using the view model
        request = CustomerViewModel(**request.dict())
        # Create a command object from the request data and the customer id
        command = UpdateCustomerCommand(
            customer_id=customer_id,
            optradio=request.optradio,
            name=request.name,
            email=request.email,
            phone=request.phone,
            url=request.url,
            tags=request.tags,
            misc=request.misc,
            companyId=request.companyId,
            reference=request.reference,
            intervalNotes=request.intervalNotes,
            bankDetails=request.bankDetails,
            gst=request.gst,
            taxId=request.taxId,
        )
        # Invoke the command handler and get the result
        result = command.execute()
        # Return the result as a view model
        return CustomerViewModel(**result)


    #@app.delete("/customers/{customer_id}")
    @staticmethod
    def delete_customer(customer_id: int):
        # Create a command object from the customer id
        command = DeleteCustomerCommand(customer_id)
        # Invoke the command handler and get the result
        result = command.execute()
        # Return the result as a plain message
        return result


# from fastapi import FastAPI, Request, Response
# from pydantic import BaseModel
# from typing import Optional
# from commands import CreateCustomerCommand, UpdateCustomerCommand, DeleteCustomerCommand
# from queries import GetCustomerQuery, GetAllCustomersQuery
# from routers import customer_router

# app = FastAPI()


# # Define the request and response models
# class CustomerRequest(BaseModel):
#     optradio: Optional[str] = None
#     name: Optional[str] = None
#     email: Optional[str] = None
#     phone: Optional[str] = None
#     url: Optional[str] = None
#     tags: Optional[str] = None
#     misc: Optional[str] = None
#     companyId: Optional[str] = None
#     reference: Optional[str] = None
#     intervalNotes: Optional[str] = None
#     bankDetails: Optional[str] = None
#     gst: Optional[str] = None
#     taxId: Optional[str] = None


# class CustomerResponse(BaseModel):
#     id: int
#     optradio: Optional[str] = None
#     name: Optional[str] = None
#     email: Optional[str] = None
#     phone: Optional[str] = None
#     url: Optional[str] = None
#     tags: Optional[str] = None
#     misc: Optional[str] = None
#     companyId: Optional[str] = None
#     reference: Optional[str] = None
#     intervalNotes: Optional[str] = None
#     bankDetails: Optional[str] = None
#     gst: Optional[str] = None
#     taxId: Optional[str] = None


# # Register the customer router
# app.include_router(customer_router)


# # Define the endpoints
# @app.post("/customers", response_model=CustomerResponse)
# def create_customer(request: CustomerRequest):
#     # Create a command object from the request data
#     command = CreateCustomerCommand(
#         optradio=request.optradio,
#         name=request.name,
#         email=request.email,
#         phone=request.phone,
#         url=request.url,
#         tags=request.tags,
#         misc=request.misc,
#         companyId=request.companyId,
#         reference=request.reference,
#         intervalNotes=request.intervalNotes,
#         bankDetails=request.bankDetails,
#         gst=request.gst,
#         taxId=request.taxId,
#     )
#     # Invoke the command handler and get the result
#     result = command.execute()
#     # Return the result as a response model
#     return CustomerResponse(**result)


# @app.get("/customers/{customer_id}", response_model=CustomerResponse)
# def get_customer(customer_id: int):
#     # Create a query object from the customer id
#     query = GetCustomerQuery(customer_id)
#     # Invoke the query handler and get the result
#     result = query.execute()
#     # Return the result as a response model
#     return CustomerResponse(**result)


# @app.get("/customers", response_model=list[CustomerResponse])
# def get_all_customers():
#     # Create a query object with no parameters
#     query = GetAllCustomersQuery()
#     # Invoke the query handler and get the result
#     result = query.execute()
#     # Return the result as a list of response models
#     return [CustomerResponse(**customer) for customer in result]


# @app.put("/customers/{customer_id}", response_model=CustomerResponse)
# def update_customer(customer_id: int, request: CustomerRequest):
#     # Create a command object from the request data and the customer id
#     command = UpdateCustomerCommand(
#         customer_id=customer_id,
#         optradio=request.optradio,
#         name=request.name,
#         email=request.email,
#         phone=request.phone,
#         url=request.url,
#         tags=request.tags,
#         misc=request.misc,
#         companyId=request.companyId,
#         reference=request.reference,
#         intervalNotes=request.intervalNotes,
#         bankDetails=request.bankDetails,
#         gst=request.gst,
#         taxId=request.taxId,
#     )
#     # Invoke the command handler and get the result
#     result = command.execute()
#     # Return the result as a response model
#     return CustomerResponse(**result)


# @app.delete("/customers/{customer_id}")
# def delete_customer(customer_id: int):
#     # Create a command object from the customer id
#     command = DeleteCustomerCommand(customer_id)
#     # Invoke the command handler and get the result
#     result = command.execute()
#     # Return the result as a plain message
#     return result


# from fastapi import FastAPI, Request, Response
# from pydantic import BaseModel
# from typing import Optional
# from routers import customer_router
# from view_models import CustomerViewModel

# app = FastAPI()

# # Register the customer router
# app.include_router(customer_router)

# # Define the endpoints
# @app.post("/customers", response_model=CustomerViewModel)
# def create_customer(request: CustomerViewModel):
#     # Validate the request data using the view model
#     request = CustomerViewModel(**request.dict())
#     # Import the command class locally
#     from commands import CreateCustomerCommand
#     # Create a command object from the request data
#     command = CreateCustomerCommand(
#         optradio=request.optradio,
#         name=request.name,
#         email=request.email,
#         phone=request.phone,
#         url=request.url,
#         tags=request.tags,
#         misc=request.misc,
#         companyId=request.companyId,
#         reference=request.reference,
#         intervalNotes=request.intervalNotes,
#         bankDetails=request.bankDetails,
#         gst=request.gst,
#         taxId=request.taxId
#     )
#     # Invoke the command handler and get the result
#     result = command.execute()
#     # Return the result as a view model
#     return CustomerViewModel(**result)

# @app.get("/customers/{customer_id}", response_model=CustomerViewModel)
# def get_customer(customer_id: int):
#     # Import the query class locally
#     from queries import GetCustomerQuery
#     # Create a query object from the customer id
#     query = GetCustomerQuery(customer_id)
#     # Invoke the query handler and get the result
#     result = query.execute()
#     # Return the result as a view model
#     return CustomerViewModel(**result)

# @app.get("/customers", response_model=list[CustomerViewModel])
# def get_all_customers():
#     # Import the query class locally
#     from queries import GetAllCustomersQuery
#     # Create a query object with no parameters
#     query = GetAllCustomersQuery()
#     # Invoke the query handler and get the result
#     result = query.execute()
#     # Return the result as a list of view models
#     return [CustomerViewModel(**customer) for customer in result]

# @app.put("/customers/{customer_id}", response_model=CustomerViewModel)
# def update_customer(customer_id: int, request: CustomerViewModel):
#     # Validate the request data using the view model
#     request = CustomerViewModel(**request.dict())
#     # Import the command class locally
#     from commands import UpdateCustomerCommand
#     # Create a command object from the request data and the customer id
#     command = UpdateCustomerCommand(
#         customer_id=customer_id,
#         optradio=request.optradio,
#         name=request.name,
#         email=request.email,
#         phone=request.phone,
#         url=request.url,
#         tags=request.tags,
#         misc=request.misc,
#         companyId=request.companyId,
#         reference=request.reference,
#         intervalNotes=request.intervalNotes,
#         bankDetails=request.bankDetails,
#         gst=request.gst,
#         taxId=request.taxId
#     )
#     # Invoke the command handler and get the result
#     result = command.execute()
#     # Return the result as a view model
#     return CustomerViewModel(**result)

# @app.delete("/customers/{customer_id}")
# def delete_customer(customer_id: int):
#     # Import the command class locally
#     from commands import DeleteCustomerCommand
#     # Create a command object from the customer id
#     command = DeleteCustomerCommand(customer_id)
#     # Invoke the command handler and get the result
#     result = command.execute()
#     # Return the result as a plain message
#     return result

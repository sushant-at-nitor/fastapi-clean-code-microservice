from fastapi import APIRouter, Depends
from controller import CustomerController

# from controller import (
#     create_customer,
#     get_customer,
#     get_all_customers,
#     update_customer,
#     delete_customer,
# )
from view_models import CustomerViewModel

# Create a router object for the customers resource
customer_router = APIRouter(
    prefix="/customers",
    tags=["customers"],
    responses={418: {"description": "Customer API"}},
)


# Define the dependencies for the router
def get_customer_id(customer_id: int):
    return customer_id


def get_customer_request(request: CustomerViewModel):
    return request


# Register the endpoints with the router
customer_router.post("/", response_model=CustomerViewModel)(
    CustomerController.create_customer
)

customer_router.get(
    "/{customer_id}",
    response_model=CustomerViewModel,
    dependencies=[Depends(get_customer_id)],
)(CustomerController.get_customer)

customer_router.get("/", response_model=list)(
    CustomerController.get_all_customers
)

customer_router.put(
    "/{customer_id}",
    response_model=CustomerViewModel,
    dependencies=[Depends(get_customer_id), Depends(get_customer_request)],
)(CustomerController.update_customer)

customer_router.delete("/{customer_id}", dependencies=[Depends(get_customer_id)])(
    CustomerController.delete_customer
)

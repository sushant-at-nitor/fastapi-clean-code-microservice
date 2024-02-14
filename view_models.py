from pydantic import BaseModel, validator
from typing import Optional


# Define the view model for the customer
class CustomerViewModel(BaseModel):
    id: int = 0,
    optradio: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = ""
    phone: Optional[str] = ""
    url: Optional[str] = ""
    tags: Optional[str] = None
    misc: Optional[str] = None
    companyId: Optional[str] = None
    reference: Optional[str] = None
    intervalNotes: Optional[str] = None
    bankDetails: Optional[str] = None
    gst: Optional[str] = None
    taxId: Optional[str] = None

    # Define some validators for the fields
    @validator("email")
    def email_must_be_valid(cls, v):
        # Check if the email is valid
        if "@" not in v:
            raise ValueError("Invalid email address")
        return v

    @validator("phone")
    def phone_must_be_valid(cls, v):
        # Check if the phone is valid
        if not v.isdigit():
            raise ValueError("Invalid phone number")
        return v

    @validator("url")
    def url_must_be_valid(cls, v):
        # Check if the url is valid
        if not v.startswith("http"):
            raise ValueError("Invalid url")
        return v

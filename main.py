# main.py

# Import the app object from the controller module
from api import app

# Run the Uvicorn server if this file is executed as the main script
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

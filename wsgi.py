from app import create_app
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create the application instance
app = create_app()

if __name__ == "__main__":
    app.run()

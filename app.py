# Importing Flask for web application
from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define the main route
@app.route('/')
def home():
    return "Hello, AWS hi CodePipeline!"  # Modify this message

# Run the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

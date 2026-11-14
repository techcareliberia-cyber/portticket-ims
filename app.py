from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>PortTicket IMS</h1>
    <h2>Vehicle Entry & Ticketing Management System</h2>
    <p>System is running successfully!</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

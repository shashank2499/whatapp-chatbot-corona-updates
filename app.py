from testing import corona
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from country import countrycheck

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    phone_no=request.form.get('From')
    reply=corona(msg)
    if reply=="not matching":
        reply=countrycheck(msg)
    if reply=="not":
        reply="Please correct the spelling!"
    if msg.lower()=="hi":
        reply="Please enter the name of the state or country you want to check."
    if msg.lower()=="hello":
        reply="Please enter the name of the state or country you want to check."

    # Create reply
    resp = MessagingResponse()
    resp.message(reply)
    return str(resp)
if __name__ == "__main__":
    app.run(debug=True)

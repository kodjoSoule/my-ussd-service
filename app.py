from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ussd', methods=['POST'])
def ussd():
    session_id = request.values.get("sessionId")
    service_code = request.values.get("serviceCode")
    phone_number = request.values.get("phoneNumber")
    text = request.values.get("text")

    # Logique pour traiter les requêtes USSD
    if text == "":
        response = "CON Welcome to our USSD service. Choose an option:\n"
        response += "1. Check Balance\n"
        response += "2. Deposit Money\n"
        response += "3. Withdraw Money\n"
    elif text == "1":
        response = "END Your balance is 1000 FCFA."
    elif text == "2":
        response = "CON Enter amount to deposit:"
    elif text.startswith("2*"):
        amount = text.split("*")[1]
        response = f"END You have deposited {amount} FCFA."
    elif text == "3":
        response = "CON Enter amount to withdraw:"
    elif text.startswith("3*"):
        amount = text.split("*")[1]
        response = f"END You have withdrawn {amount} FCFA."
    else:
        response = "END Invalid option."

    return response

if __name__ == '__main__':
    app.run(debug=True)

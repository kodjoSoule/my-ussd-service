from flask import Flask, request

app = Flask(__name__)

@app.route('/ussd', methods=['GET', 'POST'])
def ussd():
    session_id = request.values.get('sessionId')
    service_code = request.values.get('serviceCode')
    phone_number = request.values.get('phoneNumber')
    text = request.values.get('text', '')

    if text == '':
        response = "CON Welcome to our service\n"
        response += "1. Check Balance\n"
        response += "2. Transfer Money\n"
    elif text == '1':
        response = "END Your balance is $100"
    elif text == '2':
        response = "CON Enter recipient number"
    else:
        response = "END Invalid option"

    return response

if __name__ == '__main__':
    app.run(debug=True)

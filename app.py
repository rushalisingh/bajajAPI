from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample user data (replace with your logic)
user_data = {
    "full_name": "John Doe",
    "dob": "17-09-1999",
    "email": "john@xyz.com",
    "roll_number": "ABCD123"
}

@app.route('/bfhl', methods=['POST', 'GET'])
def bfhl():
    if request.method == 'POST':
        try:
            data = request.json['data']
            numbers = [d for d in data if isinstance(d, int) or (isinstance(d, str) and d.isdigit())]
            alphabets = [d for d in data if isinstance(d, str) and d.isalpha()]
            highest_alphabet = [max(alphabets, key=lambda x: ord(x.lower()))] if alphabets else []

            response = {
                "is_success": True,
                "user_id": f"{user_data['full_name'].replace(' ', '_')}_{user_data['dob'].replace('-', '')}",
                "email": user_data['email'],
                "roll_number": user_data['roll_number'],
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_alphabet": highest_alphabet
            }

            return jsonify(response), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 400

    elif request.method == 'GET':
        return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)

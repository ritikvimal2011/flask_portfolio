from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from flask_mail import Mail, Message

app = Flask(__name__)

# ✅ DIRECT API KEY (for now to fix error)
client = OpenAI(api_key="AIzaSyDlSe6mZkjH8zNA2SfUessC2r0qwBgHAos")

# ---------------- ROUTES ---------------- #

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ritik")
def ritik():
    return render_template("ritik.html")

# ---------------- CHATBOT ---------------- #

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_msg = request.json.get("message")

        print("User:", user_msg)  # debug

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=user_msg
        )

        print("Response:", response)  # debug

        reply = response.output[0].content[0].text

        return jsonify({"reply": reply})

    except Exception as e:
        print("FULL ERROR:", e)   # 👈 THIS IS KEY
        return jsonify({"reply": "Server error, check terminal!"})
    
# ---------------- EMAIL CONFIG ---------------- #

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "your_email@gmail.com"
app.config['MAIL_PASSWORD'] = "your_app_password"

mail = Mail(app)

# ---------------- CONTACT FORM ---------------- #

@app.route("/contact", methods=["POST"])
def contact():
    data = request.json

    msg = Message(
        subject=f"New Message from {data['name']}",
        sender=app.config['MAIL_USERNAME'],
        recipients=[app.config['MAIL_USERNAME']],
        body=f"""
Name: {data['name']}
Email: {data['email']}
Message: {data['message']}
"""
    )

    mail.send(msg)

    return jsonify({"message": "Message sent successfully!"})

# ---------------- RUN ---------------- #

if __name__ == "__main__":
    app.run(debug=True)

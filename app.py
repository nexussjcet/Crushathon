from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(_name_)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message")

        # Generate AI response using Ollama
        response = ollama.chat(model="your_model_name", messages=[{"role": "user", "content": user_input}])

        ai_reply = response["message"]["content"] if "message" in response else "Sorry, I didn't understand that. 💔"

        return jsonify({"reply": ai_reply})

    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 500

if _name_ == "_main_":
    app.run(debug=True)
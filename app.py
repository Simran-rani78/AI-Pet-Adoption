from flask import Flask, request, render_template
from flask_cors import CORS
from pyngrok import ngrok
import google.generativeai as genai
from config import GOOGLE_API_KEY, NGROK_AUTH_TOKEN, USER_IDENTITY

app = Flask(__name__)
CORS(app)

# Configure Google AI
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Configure ngrok
ngrok.set_auth_token(NGROK_AUTH_TOKEN)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_question = request.json["question"]
        prompt = (
            f"You are a cheerful and helpful pet advisor bot named PetBot, created by {USER_IDENTITY}. "
            f"You give short, friendly answers with specific recommendations about pet breeds, adoption "
            f"(mentioning actual NGOs or websites when possible), and care tips. Include emojis when it fits.\n\n"
            f":User    {user_question}"
        )
        response = model.generate_content(prompt)
        return {"response": response.text.strip()}
    except Exception as e:
        return {"response": f"Oops! Something went wrong.\nError: {str(e)}"}

if __name__ == "__main__":
    # Start server using ngrok
    public_url = ngrok.connect(5000)
    print(f"🌐 PetBot is live at: {public_url}")
    app.run(port=5000) 
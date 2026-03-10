from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import openai
import os

app = Flask(__name__)

# Keys will come from Render Environment Variables
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
openai.api_key = OPENAI_API_KEY

@app.route("/healthz")
def health():
    return "OK", 200

@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():
    incoming_msg = request.values.get("Body", "")
    resp = MessagingResponse()
    
    if incoming_msg.strip() == "":
        resp.message("Namaste! Tapai le message pathaunuhos.")
        return str(resp)

    # Generate AI response in Roman Nepali
    prompt = f"Apex Fitness Gym WhatsApp bot. Reply in Roman Nepali. User said: {incoming_msg}"
    try:
        completion = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        answer = completion.choices[0].text.strip()
    except Exception as e:
        answer = "Maile bujhna sakina. Kripaya feri try garnuhos."

    resp.message(answer)
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
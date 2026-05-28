from django.shortcuts import render
from .models import Chat

import pickle

# Load trained model
model = pickle.load(open("emotion_model.pkl", "rb"))

# Load vectorizer
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))


def home(request):

    response = ""

    if request.method == "POST":

        user_message = request.POST.get('message')

        # Convert text into numbers
        transformed_text = vectorizer.transform([user_message])

        # Predict emotion
        emotion = model.predict(transformed_text)[0]

        # Generate response
        if emotion == "happy":
            response = "I'm happy to hear that!"

        elif emotion == "sad":
            response = "I'm sorry you're feeling sad."

        elif emotion == "angry":
            response = "Please stay calm. I'm here to help."

        else:
            response = "I understand."

        # Save to database
        Chat.objects.create(
            user_message=user_message,
            bot_response=response,
            detected_emotion=emotion
        )

    # Load all chats
    all_chats = Chat.objects.all()

    return render(request, 'index.html', {
        'chat_history': all_chats
    })
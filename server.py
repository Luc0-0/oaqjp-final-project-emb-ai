"""
Flask server for Emotion Detection web application.
Provides an endpoint to analyze emotions from user text input.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the home page for the application.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    """
    Endpoint to detect emotions from input text.
    Handles both GET and POST requests.
    Returns a formatted string response for the user.
    """
    # Handle GET or POST input
    if request.method == "GET":
        text_to_analyze = request.args.get("textToAnalyze", "")
    else:
        text_to_analyze = request.form.get("text", "")

    result = emotion_detector(text_to_analyze)

    # Handle blank entries
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is "
        f"{result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

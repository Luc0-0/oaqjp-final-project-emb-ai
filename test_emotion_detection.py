import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        response = emotion_detector("I am glad this happened")
        self.assertIn("joy", response)
        self.assertGreater(response["joy"], response["anger"])

    def test_anger(self):
        response = emotion_detector("I am really mad about this")
        self.assertIn("anger", response)
        self.assertGreater(response["anger"], response["joy"])

    def test_disgust(self):
        response = emotion_detector("I feel disgusted just hearing about this")
        self.assertIn("disgust", response)
        self.assertGreater(response["disgust"], response["joy"])

    def test_sadness(self):
        response = emotion_detector("I am so sad about this")
        self.assertIn("sadness", response)
        self.assertGreater(response["sadness"], response["joy"])

    def test_fear(self):
        response = emotion_detector("I am really afraid that this will happen")
        self.assertIn("fear", response)
        self.assertGreater(response["fear"], response["joy"])

if __name__ == "__main__":
    unittest.main()

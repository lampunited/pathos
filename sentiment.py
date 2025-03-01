from transformers import pipeline
from transformers import pipeline
classifier = pipeline("sentiment-analysis", model="michellejieli/emotion_text_classifier")
text = "I am really happy today!"

result = classifier(text)

print(result)

from google import genai
from redditfunction import search_reddit
import os

client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

def ask_llm(question: str) -> str:
    # Append the instruction to the user's question.
    prompt = f"{question}\nMake this into a reddit search that is a few words long. Make sure that you only give a single search and that your response is under 7 words long."
    response = client.models.generate_content(
        model="gemini-2.0-flash",  # Replace with the correct model identifier if needed.
        contents=prompt
    )
    return response.text

def ask_question(question: str, data: str) -> str:
    # Append the instruction to the user's question.
    prompt = f"{question}\nCan you summarize this text in a few sentences in a legible answer: \n {data}"
    response = client.models.generate_content(
        model="gemini-2.0-flash",  # Replace with the correct model identifier if needed.
        contents=prompt
    )
    return "pathOS AI Summary: " + response.text

if __name__ == "__main__":
    user_question = input("Enter your debugging or programming question: ")
    query = ask_llm(user_question)
    print(query)
    answers = search_reddit(query)
    doc = ""
    for answer in answers:
        doc += answer.body[:200] + "\n"
    answer = ask_question(user_question, doc)
    print(answer)


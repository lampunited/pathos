from google import genai
from redditfunction import get_reddit

client = genai.Client(api_key="AIzaSyCgOJpua5_yNc8JBuFI9f17Ysq03cUgkCU")

def ask_llm(question: str) -> str:
    """
    Sends the provided question along with an instruction to convert it into a 1-2 sentence search input,
    then returns the generated content from the Gemini API.

    Parameters:
        question (str): The user's debugging or programming question.
    
    Returns:
        str: The response generated by the Gemini API.
    """
    # Append the instruction to the user's question.
    prompt = f"{question}\nMake this into a reddit search that is a few words long."
    response = client.models.generate_content(
        model="gemini-2.0-flash",  # Replace with the correct model identifier if needed.
        contents=prompt
    )
    return response.text

def ask_question(question: str, data: str) -> str:
    # Append the instruction to the user's question.
    prompt = f"{question}\nCan you summarize this text in a few sentences using the data below in a legible answer: \n {data}"
    response = client.models.generate_content(
        model="gemini-2.0-flash",  # Replace with the correct model identifier if needed.
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    user_question = input("Enter your debugging or programming question: ")
    query = ask_llm(user_question)
    print(query)
    answers = get_reddit(query)
    doc = ""
    for answer in answers:
        doc += answer.body[:200] + "\n"
    answer = ask_question(user_question, doc)
    print(answer)
    #print("\nLLM Response:\n", result)


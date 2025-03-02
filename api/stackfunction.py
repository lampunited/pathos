import requests
from tqdm import tqdm

def search_stack(query):
    API_KEY = "rl_UUDhk4wTovnZBQsWCve1PCKtV"  # Replace with your actual Stack Exchange API key

    # First request
    response = requests.get(
        "https://api.stackexchange.com/2.3/similar",
        params={
            "order": "desc",
            "sort": "relevance",
            "title": query,
            "site": "stackoverflow",
            "key": API_KEY  # Add your API key here
        }
    )

    question_data = response.json()["items"]
    results_list = []

    for i in tqdm(range(min(10, len(question_data)))):
        question_id = question_data[i]["question_id"]
        answer_count = question_data[i]["answer_count"]

        # Second request (formatted like the first one)
        response = requests.get(
            f"https://api.stackexchange.com/2.3/questions/{question_id}/answers",
            params={
                "order": "desc",
                "sort": "activity",
                "site": "stackoverflow",
                "filter": "withbody",
                "key": API_KEY  # Add your API key here
            }
        )

        answer_data = response.json()["items"]

        for i in range(min(3, answer_count)):
            result_obj = {
                "source": "stack",
                "question_text": question_data[i]["title"],
                "answer_text": truncate_to_words(answer_data[i]["body"]),
                "score": answer_data[i]["score"],
                "url": "https://stackoverflow.com/a/" + str(answer_data[i]["answer_id"])
            }
            results_list.append(result_obj)

    return results_list

def truncate_to_words(text, word_limit=250):
    words = text.split()  # Split text into words
    if len(words) > word_limit:
        return " ".join(words[:word_limit]) + "..."  # Add ellipsis if truncated
    return text  # Return full text if within limit




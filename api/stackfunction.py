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

    for i in tqdm(range(min(20, len(question_data)))):
        question_id = question_data[i]["question_id"]
        answer_count = question_data[i]["answer_count"]
        #print(question_id)

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
            ##print(answer_data[i]["body"])
            result_obj = {
                "source": "stack",
                "question_text": question_data[i]["title"],
                "answer_text": answer_data[i]["body"],
                "score": answer_data[i]["score"],
                "url": question_data[i]["link"]
            }
            results_list.append(result_obj)

    return results_list



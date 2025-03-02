import praw
import json
from tqdm import tqdm

def search_reddit(query):
    #authentication
    reddit = praw.Reddit(
        client_id="8sZIJdk__UZwu_fJmx9Rew",
        client_secret="scG0wV9ZXr7SWBjMP44Lkj4PWaY0iw",
        user_agent="hackillinois_reddit_bot",
        username = "Gullible_Drummer_471",
        password = "Gunnersbo6a#"
    )

    print(f"Authenticated as: {reddit.user.me()}")

    search_amount = 200
    search_results = reddit.subreddit("all").search(query, sort="relevance", syntax="lucene", limit=search_amount)

    results_list = []

    for submission in search_results:
        question_text = submission.title
        print(question_text)

search_reddit("Downloading GitHub program")


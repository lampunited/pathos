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

    search_amount = 10
    search_results = reddit.subreddit("all").search(query, sort="relevance", limit=search_amount)

    results_list = []

    for submission in tqdm(search_results, desc="Processing reddit search: ", total=search_amount):
        post_url = "https://www.reddit.com" + submission.permalink
        question_text = submission.title

        submission.comments.replace_more(limit=0)
        all_comments = submission.comments.list()
        
        depth0_comments = [c for c in all_comments if c.depth == 0]
        
        sort_key = lambda c: (c.score, len(c.body))
        depth0_sorted = sorted(depth0_comments, key=sort_key, reverse=True)[:3]
        
        combined_comments = depth0_sorted
        
        post_score = submission.score
        
        # Append a single result object per submission
        for comment in combined_comments:
            author_name = comment.author.name if comment.author else "[deleted]"  # Handle deleted users
            answer_text = comment.body
            comment_url = f"https://www.reddit.com{comment.permalink}"
            result_obj = {
                "username": author_name,  # Add username here
                "source": "reddit",
                "question_text": question_text,
                "answer_text": truncate_to_words(answer_text),
                "score": post_score,
                "url": comment_url
            }
            results_list.append(result_obj)

    return results_list

def truncate_to_words(text, word_limit=250):
    words = text.split()  # Split text into words
    if len(words) > word_limit:
        return " ".join(words[:word_limit]) + "..."  # Add ellipsis if truncated
    return text  # Return full text if within limit
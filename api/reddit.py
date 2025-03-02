import praw
import json
#authentication
reddit = praw.Reddit(
    client_id="8sZIJdk__UZwu_fJmx9Rew",
    client_secret="scG0wV9ZXr7SWBjMP44Lkj4PWaY0iw",
    user_agent="hackillinois_reddit_bot",
    username = "Gullible_Drummer_471",
    password = "Gunnersbo6a#"
)

print(f"Authenticated as: {reddit.user.me()}")


query = "can't login to github"
search_results = reddit.subreddit("all").search(query, sort="relevance", limit=10)

results_list = []

for submission in search_results:
    post_url = "https://www.reddit.com" + submission.permalink
    question_text = submission.title
    if submission.selftext:
        question_text += "\n\n" + submission.selftext

    submission.comments.replace_more(limit=0)
    all_comments = submission.comments.list()
    
    depth0_comments = [c for c in all_comments if c.depth == 0]
    depth1_comments = [c for c in all_comments if c.depth == 1]
    other_comments  = [c for c in all_comments if c.depth > 1]
    
    sort_key = lambda c: (c.score, len(c.body))
    depth0_sorted = sorted(depth0_comments, key=sort_key, reverse=True)[:3]
    depth1_sorted = sorted(depth1_comments, key=sort_key, reverse=True)[:3]
    other_sorted  = sorted(other_comments, key=sort_key, reverse=True)[:3]
    
    combined_comments = depth0_sorted + depth1_sorted + other_sorted
    
    post_score = submission.score
    
    # Append a single result object per submission
    for comment in combined_comments:
        answer_text = comment.body
        author_name = comment.author.name if comment.author else "[deleted]"  # Handle deleted users
        result_obj = {
            "username": author_name,
            "source": "reddit",
            "question_text": question_text,
            "answer_text": answer_text,
            "score": post_score,
            "url": post_url
        }
        results_list.append(result_obj)

with open("api/reddit_results.json", "w", encoding="utf-8") as f:
    json.dump(results_list, f, ensure_ascii=False, indent=4)

print("Results written to reddit_results.json")
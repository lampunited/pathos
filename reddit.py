import praw
#authentication
reddit = praw.Reddit(
    client_id="8sZIJdk__UZwu_fJmx9Rew",
    client_secret="scG0wV9ZXr7SWBjMP44Lkj4PWaY0iw",
    user_agent="hackillinois_reddit_bot",
    username = "Gullible_Drummer_471",
    password = "Gunnersbo6a#"
)

print(f"Authenticated as: {reddit.user.me()}")




query = "harry maguire"
results = reddit.subreddit("all").search(query, sort="relevance", limit=5)

# Iterate over each result and display some metrics
for submission in results:
    print("Title:", submission.title)
    print("Score:", submission.score)
    print("Upvote Ratio:", submission.upvote_ratio)
    print("Comments:", submission.num_comments)
    print("Created UTC:", submission.created_utc)
    print("-" * 40)
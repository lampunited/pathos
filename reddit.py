import praw

reddit = praw.Reddit(
    client_id="8sZIJdk__UZwu_fJmx9Rew",
    client_secret="scG0wV9ZXr7SWBjMP44Lkj4PWaY0iw",
    user_agent="hackillinois_reddit_bot",
    username = "Gullible_Drummer_471",
    password = "Gunnersbo6a#"
)

print(f"Authenticated as: {reddit.user.me()}")


subreddit = reddit.subreddit("python")

# Retrieve the top 10 posts from the subreddit
print("Top posts in r/python:")
for submission in subreddit.top(limit=10):
    print("Title:", submission.title)
    print("Score:", submission.score)
    print("URL:", submission.url)
    print("-" * 40)

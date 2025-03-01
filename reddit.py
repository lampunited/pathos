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


query = "how do substrings work in c++"

results = reddit.subreddit("all").search(query, sort="relevance", limit=1)

for submission in results:
    post_url = "https://www.reddit.com" + submission.permalink

    print("----- Post -----")
    print("Title:", submission.title)
    print("Selftext:", submission.selftext)
    print("URL:", post_url)
    print("Score:", submission.score)
    print("Upvote Ratio:", submission.upvote_ratio)
    print("\n--- Comments ---")
    
    submission.comments.replace_more(limit=0)
    all_comments = submission.comments.list()

    # Separate comments by depth
    depth0_comments = [c for c in all_comments if c.depth == 0]
    depth1_comments = [c for c in all_comments if c.depth == 1]
    other_comments  = [c for c in all_comments if c.depth > 1]

    # Sorting: We sort by score first and then by comment text length (as a proxy for more content)
    sort_key = lambda comment: (comment.score, len(comment.body))
    depth0_sorted = sorted(depth0_comments, key=sort_key, reverse=True)
    depth1_sorted = sorted(depth1_comments, key=sort_key, reverse=True)
    other_sorted  = sorted(other_comments,  key=sort_key, reverse=True)

    # Priority 1: Top 5 depth 0 comments
    print("Top 5 Depth 0 Comments:")
    for comment in depth0_sorted[:5]:
        print("Depth:", comment.depth, "| Score:", comment.score, "| Length:", len(comment.body))
        print("Comment:", comment.body)
        print("-" * 40)

    # Priority 2: Top 5 depth 1 comments
    print("Top 5 Depth 1 Comments:")
    for comment in depth1_sorted[:5]:
        print("Depth:", comment.depth, "| Score:", comment.score, "| Length:", len(comment.body))
        print("Comment:", comment.body)
        print("-" * 40)

    # Priority 3: Other high-quality comments (sorted by score and length)
    print("Other High-Quality Comments:")
    for comment in other_sorted[:5]:
        print("Depth:", comment.depth, "| Score:", comment.score, "| Length:", len(comment.body))
        print("Comment:", comment.body)
        print("-" * 40)

    print("=" * 60)

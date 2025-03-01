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

results = reddit.subreddit("all").search(query, sort="relevance", limit=5)

# Iterate over each search result
for submission in results:
    print("Submission Title:", submission.title)
    
    # Optional: Set comment sort order to 'top'
    submission.comment_sort = "top"
    
    # Replace "more comments" to fetch all comments in the thread.
    submission.comments.replace_more(limit=0)
    
    # Flatten the comment tree into a list.
    all_comments = submission.comments.list()
    
    # Sort comments by score (upvotes) in descending order.
    sorted_comments = sorted(all_comments, key=lambda comment: comment.score, reverse=True)
    
    # Print the top 3 upvoted comments for this submission.
    print("Top 3 Comments:")
    for comment in sorted_comments[:3]:
        print("Score:", comment.score)
        # Print a snippet of the comment body (for readability).
        print("Comment:", comment.body[:200])
        print("-" * 40)
    print("=" * 60)
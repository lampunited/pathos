import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import gemini
import redditfunction
import stack_overflow  # Ensure this file is named "stack_overflow.py"

app = Flask(__name__, static_folder='build', static_url_path='')
CORS(app)  # Enable CORS if you are developing the front end separately

@app.route('/api/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "No query provided"}), 400
    try:
        # Use Gemini to transform the user's query.
        gemini_summary = gemini.ask_llm(query)
        
        # Use the Gemini summary as the search query for Reddit.
        reddit_comments = redditfunction.get_reddit(gemini_summary)
        reddit_results = []
        for comment in reddit_comments:
            reddit_results.append({
                "text": comment.body[:200],
                "score": comment.score
            })
        
        # Get Stack Overflow answers using the original query.
        so_answers = stack_overflow.get_stackoverflow_answers(query)
        
        return jsonify({
            "gemini": gemini_summary,
            "stackoverflow": so_answers,
            "reddit": reddit_results
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Serve static files from the React build folder.
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)  # Runs on http://localhost:5000 by default

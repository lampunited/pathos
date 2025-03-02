import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from gemini import ask_llm
from stackfunction import search_stack
from createindex import create_index
from search import search_faiss

app = Flask(__name__, static_folder='build', static_url_path='')
CORS(app)  # Enable CORS if you are developing the front end separately

@app.route('/api/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "No query provided"}), 400
    try:
        #print(query)
        gemini_query = ask_llm(query)
        #print(gemini_query)
        reddit_data = search_reddit(gemini_query)
        stack_data = search_stack(gemini_query)

        data = reddit_data + stack_data
        create_index(data)
        results = search_faiss(query, top_k=10)
        return results
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

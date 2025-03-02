from redditfunction import search_reddit
from createindex import create_index
from search import search_faiss
from gemini import ask_llm
from stackfunction import search_stack

question = "How can I download Github?"
query = ask_llm(question)
print("Query: " + query)
data = search_stack(query)
print("Data length: " + str(len(data)))
create_index(data)
results = search_faiss(query, top_k=10)
#print(results)

# Print results
for res in results:
    #print(f"Question: {res['question_text']}")
    print(f"Answer: {res['answer_text']}")
    print(f"Distance: {res['distance']:.4f}")
    #print(f"URL: {res['url']}\n")


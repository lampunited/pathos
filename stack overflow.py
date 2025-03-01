import tkinter as tk
import requests

def get_stackoverflow_answers(query):
    url = 'https://api.stackexchange.com/2.3/search/advanced'
    params = {'order': 'desc', 'sort': 'relevance', 'q': query, 'site': 'stackoverflow', 'filter': 'withbody'}
    response = requests.get(url, params=params)
    data = response.json()

    answers = []
    
    # Loop through questions, then fetch their answers (the actual solutions)
    for item in data['items']:
        title = item['title']
        link = item['link']
        question_id = item['question_id']
        
        # Fetch the answers to this question
        answers_url = f'https://api.stackexchange.com/2.3/questions/{question_id}/answers'
        answers_response = requests.get(answers_url, params={'site': 'stackoverflow'})
        answers_data = answers_response.json()
        
        if 'items' in answers_data:
            for answer in answers_data['items']:
                body = answer.get('body', 'No answer text available')
                answers.append(f"Question: {title}\nAnswer: {body}\nLink to question: {link}\n\n")
    
    return answers

def display_answers():
    query = entry.get()
    answers = get_stackoverflow_answers(query)
    output_text.delete(1.0, tk.END)  # Clear previous text
    if answers:
        for answer in answers:
            output_text.insert(tk.END, answer)
    else:
        output_text.insert(tk.END, "No answers found.\n")

# Create the GUI
root = tk.Tk()
root.title('Stack Overflow Answer Finder')

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

search_button = tk.Button(root, text='Search', command=display_answers)
search_button.pack(pady=5)

output_text = tk.Text(root, height=10, width=70)
output_text.pack(pady=10)

root.mainloop()

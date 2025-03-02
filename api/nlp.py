import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download required NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_query(query):
    #common english words - is, and, that
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(query.lower())

    # PorterStemmer filter - changes words like ran, running, into base form "run"
    filtered_tokens = [PorterStemmer().stem(word) for word in tokens if word.isalnum() and word not in stop_words]
    return ' '.join(filtered_tokens)

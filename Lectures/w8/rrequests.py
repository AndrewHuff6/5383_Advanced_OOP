import requests
import nltk
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

#nltk.download('wordnet')

url = "https://msutexas.edu"
response = requests.get(url)

print(len(response.text))
soup = BeautifulSoup(response.text, "html.parser")

piece_of_information = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'p'])

text = ""
clean_words = []

for piece_of_information in piece_of_information:
    text += piece_of_information.get_text(" ", strip=True) + " "

sw = stopwords.words('english')
words = word_tokenize(text)

for word in words:
    if word not in sw:
        clean_words.append(word)

clean_clean_words = []
lemmatizer = WordNetLemmatizer()
for cw in clean_words:
    ccw = lemmatizer.lemmatize(cw.lower())
    clean_clean_words.append(ccw)

print(clean_words)
print(len(words))
print(len(clean_words))

print("clean clean words")
print(clean_clean_words)
print(len(clean_clean_words))

unique_clean_clean_words = set(clean_clean_words)
print(unique_clean_clean_words)
print(len(unique_clean_clean_words))
import os
os.system('cls')

#Q.No.1
"""
Write Python code to:

Remove leading/trailing spaces
Convert text to lowercase
Remove punctuation: . , ! &
Replace multiple spaces with single space
Print final cleaned text
"""

text = "  NLP   is AMAZING!!! Python, ML & AI are the FUTURE...   "
cleaned = text.strip().lower()
punc = ".,!&"
for char in punc:
    cleaned = cleaned.replace(char, "")
#remove extra spaces
print(" ".join(cleaned.split()))


#Another way about punctuation
import string
text = "  NLP   is AMAZING!!! Python, ML & AI are the FUTURE...   "
cleaned = text.strip().lower()
punc = string.punctuation
for char in punc:
    cleaned = cleaned.replace(char, "")
#remove extra spaces
print(" ".join(cleaned.split()))


#Q.No.2
"""
Convert text to lowercase
Split into words
Count frequency of each word
Store in dictionary
Print dictionary
"""
text = "AI will change AI and ML will change the world of AI"
cleaned_split = text.lower().split()
dct = {}
for word in cleaned_split:
    if word in dct:
        dct[word] += 1
    else:
        dct[word] = 1
print(dct)

#Q.No.3
"""
Write Python code to:

Convert text to lowercase
Split into words
Keep only words with length >= 4
Print final list
"""
text = "AI will change the world of machine learning"
cleaned = text.lower().split()
final_list = []
for word in cleaned:
    if len(word) >= 4:
        final_list.append(word)
print(final_list)


#Q.No.4
"""
Write Python code to:

Convert text to lowercase
Split into words
Remove words with length <= 3
Print final list
"""
text = "AI is revolutionizing the world of deep learning and ML"
cleaned = text.lower().split()
final_list = [word for word in cleaned if len(word) >= 4]
print(final_list)


#Q.No.5
"""
Write Python code to:

Convert text to lowercase
Replace word "ai" with "artificial_intelligence"
Print final sentence
"""
text = "I love AI and AI loves me"
print(" ".join([
    "artificial_intelligence" if word=="ai" else word
     for word in text.lower().split()
    ]))


#Q.No.6
"""
Write Python code to:

Convert text to lowercase
Remove stopwords:
["i", "and", "to", "is", "a"]
Print final cleaned sentence
"""

text = "I love artificial intelligence and machine learning"
stop_words = ["i", "and", "to", "is", "a"]
words = text.lower().split()
cleaned = []
for word in words:
    if word not in stop_words:
        cleaned.append(word)
print(" ".join(cleaned))

#Another way
text = "I love artificial intelligence and machine learning"
stop_words = ["i", "and", "to", "is", "a"]
words = text.lower().split()
print(" ".join([word for word in words if word not in stop_words]))


#Q.No.7
"""
Write Python code to:

Convert to lowercase
Remove punctuation ,
Split into words
Count frequency of each word
Print dictionary
"""
import string
text = "AI is amazing, AI is powerful and AI is the future"
cleaned = text.lower()
for char in string.punctuation:
    cleaned = cleaned.replace(char,"")
words = cleaned.split()
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print(dct)


#Q.No8
"""
Write Python code to:

Convert text to lowercase
Remove punctuation: ! , - . &
Split into words
Remove words with length ≤ 2
Print final list
"""
text = "AI!!! is,,, changing---the world... fast & rapidly"
cleaned = text.lower()
for char in "!,-.&":
    cleaned = cleaned.replace(char, "")
words = cleaned.split()
print([word for word in words if len(word) > 2])



#Q.No.9
"""
Write Python code to:

Convert text to lowercase
Remove stopwords:
["is", "the", "and", "of"]
Split into words
Count frequency of remaining words
Print dictionary
"""
text = "AI is the future and AI is the power of the future"
cleaned = text.lower()
stop_words = ["is", "the", "and", "of"]
words = cleaned.split()
freq = {}
for word in words:
    if word not in stop_words:
        freq[word] = freq.get(word, 0) + 1
print(freq)


#Q.No.10
"""
Write Python code to:

1. Convert text to lowercase
2. Remove punctuation: ! . , ?
3. Split into words
4. Remove stopwords:
["is", "not", "only", "but", "also", "and"]
5. Count frequency of remaining words
6. Print final dictionary
"""
text = "AI!!! is... not only powerful, but also VERY VERY fast!!! and reliable???"
stop_words = ["is", "not", "only", "but", "also", "and"]
cleaned = text.lower()
for char in "!,.?":
    cleaned = cleaned.replace(char, "")
words = cleaned.split()
freq = {}
for word in words:
    if word not in stop_words:
        freq[word] = freq.get(word, 0) + 1
print(freq)


#Q.No.11
"""
Write Python code to:

1. Convert text to lowercase
2. Split text into sentences using ., !, ?
3. Remove empty sentences
4. For each sentence:
split into words
remove stopwords:
["is", "it", "the", "and"]
5. Print list of cleaned sentences
"""

text = "AI is amazing. Machine Learning is powerful! NLP is the future? Yes, it is."

stop_words = ["is", "it", "the", "and"]

# convert to lowercase
cleaned = text.lower()

# replace sentence punctuation with one common separator
for char in ".!?":
    cleaned = cleaned.replace(char, "|")

# split into sentences
sentences = cleaned.split("|")

# remove empty sentences
sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

final_sentences = []

for sentence in sentences:
    
    # split sentence into words
    words = sentence.split()
    
    # remove stopwords
    filtered_words = [
        word for word in words
        if word not in stop_words
    ]
    
    # join words back into sentence
    final_sentences.append(" ".join(filtered_words))

print(final_sentences)
es = []

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
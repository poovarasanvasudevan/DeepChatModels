regex_replace = {
    (r"https?:\/\/"
     r"(www\.)?"
     r"[^\s\.]+"
     r"\.\S{2,}"): "<link>",             # Raw link.
    r"\[[^\(\)]*\]\(.*\)": "<link>",     # Markdown link.
    r"\r?\n": " ",                       # Newlines.
    r"\d+": "<number>",
    r"\.{2,}": ".",
    r"(&gt;|\*|)": "",
    r"[_-]+": " "
}

contractions = {
    "sha'n't": "shall not",
    "I've": "I have",
    "who's": "who has",
    "you're": "you are",
    "can't've": "cannot have",
    "could've": "could have",
    "shan't": "shall not",
    "he'd've": "he would have",
    "hadn't've": "had not have",
    "couldn't've": "could not have",
    "y'all've": "you all have",
    "when've": "when have",
    "that'd've": "that would have",
    "it'll": "it shall",
    "oughtn't've": "ought not have",
    "you'll": "you shall",
    "shouldn't've": "should not have",
    "shouldn't": "should not",
    "we've": "we have",
    "who've": "who have",
    "why've": "why have",
    "needn't've": "need not have",
    "ma'am": "madam",
    "oughtn't": "ought not",
    "mustn't've": "must not have",
    "they'd've": "they would have",
    "isn't": "is not",
    "y'all're": "you all are",
    "so's": "so as",
    "he'd": "he had",
    "doesn't": "does not",
    "he's": "he has",
    "I'm": "I am",
    "mightn't've": "might not have",
    "hadn't": "had not",
    "needn't": "need not",
    "don't": "do not",
    "he'll've": "he shall have",
    "we'll've": "we will have",
    "what'll": "what shall",
    "that's": "that has",
    "it'd": "it had",
    "how's": "how has",
    "you've": "you have",
    "wouldn't": "would not",
    "he'll": "he shall",
    "we'd": "we had",
    "I'll": "I shall",
    "when's": "when has",
    "we'll": "we will",
    "couldn't": "could not",
    "you'll've": "you shall have",
    "will've": "will have",
    "there'd've": "there would have",
    "they'd": "they had",
    "I'd": "I had", "y'all": "you all",
    "won't've": "will not have",
    "aren't": "are not",
    "haven't": "have not",
    "mustn't": "must not",
    "what've": "what have",
    "it's": "it has",
    "she'll": "she shall",
    "wasn't": "was not",
    "they're": "they are",
    "that'd": "that would",
    "how'd'y": "how do you",
    "what's": "what has",
    "there'd": "there had",
    "to've": "to have",
    "I'll've": "I shall have",
    "y'all'd": "you all would",
    "would've": "would have",
    "how'll": "how will",
    "she'd": "she had", "what're": "what are",
    "wouldn't've": "would not have",
    "might've": "might have", "mayn't": "may not", "o'clock": "of the clock",
    "'cause": "because",
    "mightn't": "might not",
    "didn't": "did not",
    "they'll": "they shall",
    "there's": "there has",
    "we'd've": "we would have", "hasn't": "has not",
    "let's": "let us", "she's": "she has",
    "who'll": "who shall",
    "shan't've": "shall not have",
    "won't": "will not",
    "where've": "where have",
    "it'll've": "it shall have", "where's": "where has",
    "you'd've": "you would have",
    "weren't": "were not",
    "who'll've": "who shall have",
    "why's": "why has",
    "how'd": "how did",
    "we're": "we are",
    "she'd've": "she would have",
    "ain't": "am not",
    "y'all'd've": "you all would have",
    "I'd've": "I would have", "they've": "they have",
    "must've": "must have",
    "what'll've": "what shall have", "she'll've": "she shall have",
    "where'd": "where did",
    "should've": "should have",
    "you'd": "you had",
    "can't": "cannot",
    "it'd've": "it would have",
    "so've": "so have", "they'll've": "they shall have"}

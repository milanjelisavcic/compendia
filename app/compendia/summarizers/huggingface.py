from transformers import pipeline


def summarize(text):
    """
    Summarize text using huggingface summarizer
    """
    # # Open and read the article
    # f = open("article.txt", "r", encoding="utf8")
    # to_tokenize = f.read()

    # Initialize the HuggingFace summarization pipeline
    summarizer = pipeline("summarization")
    summarized = summarizer(text, min_length=75, max_length=300)

    return summarized

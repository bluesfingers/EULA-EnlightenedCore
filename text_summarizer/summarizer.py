from transformers import pipeline

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    # Use the summarizer to generate a summary
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']

# Example text to summarize
if __name__ == "__main__":
    text = (
        "OpenAI is an artificial intelligence research lab consisting of "
        "the for-profit OpenAI LP and its parent company, the non-profit "
        "OpenAI Inc. OpenAI conducts AI research with the goal of "
        "promoting and developing friendly AI in a way that benefits humanity as a whole."
    )
    print("Original Text:", text)
    print("Summary:", summarize_text(text))

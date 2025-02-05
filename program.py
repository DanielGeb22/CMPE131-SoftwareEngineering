import pandas as pd
from textblob import TextBlob
import os
import chardet

def analyze_sentiment(text):
    """Analyze sentiment of a given text using TextBlob."""
    analysis = TextBlob(text)
    score = analysis.sentiment.polarity  # Returns a score between -1 (negative) and 1 (positive)

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    """Reads input CSV from a predefined directory, performs sentiment analysis, and saves results."""
    input_dir = r"C:\Users\danie\Documents\College\SJSU\Spring 2025\CMPE 131\ai_based_sentiment_analysis"
    output_dir = r"C:\Users\danie\Documents\College\SJSU\Spring 2025\CMPE 131\ai_based_sentiment_analysis"
    input_csv = os.path.join(input_dir, "test.csv")
    output_csv = os.path.join(output_dir, "output.csv")
    
    try:
        # Ensure directories exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Detect encoding
        with open(input_csv, 'rb') as f:
            result = chardet.detect(f.read())
            encoding = result['encoding']

        # Load dataset
        df = pd.read_csv(input_csv, encoding=encoding)
        
        if 'text' not in df.columns:
            raise ValueError("CSV file must contain a 'text' column")
        
        # Apply sentiment analysis
        df['sentiment_score'] = df['text'].astype(str).apply(analyze_sentiment)
        df['sentiment_label'] = df['sentiment_score'].apply(lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral'))
        
        # Save results
        df.to_csv(output_csv, index=False)
        print(f"Sentiment analysis completed. Results saved to {output_csv}")
    except Exception as e:
        print(f"Error: {e}")

# Prints the sentiment message based on sentiment score
print(analyze_sentiment("Despise"))
print(analyze_sentiment("Lively"))
print(analyze_sentiment("Bland"))

# Calling main() will analyze the sentiments from the given dataset input "test.csv" and output the results in a new dataset
#main()
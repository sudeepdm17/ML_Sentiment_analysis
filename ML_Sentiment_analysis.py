from textblob import TextBlob
import pandas as pd

# Sample tweets (you can add more)
tweets = [
    "I'm enjoying the lockdown in the USA. It gives me time to relax.",
    "The lockdown measures in the USA are too strict. It's frustrating.",
    "Working from home during the lockdown has its challenges.",
    "The lockdown is necessary to control the spread of Covid-19.",
    "I'm feeling anxious during the lockdown in the USA.",
]

# Create a DataFrame to store the tweets
data = {'Tweet': tweets}
df = pd.DataFrame(data)

# Perform sentiment analysis for each tweet
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df['Sentiment'] = df['Tweet'].apply(analyze_sentiment)

# Print the sentiment analysis results
print("Sentiment Analysis Results:")
print(df)
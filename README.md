# Public-Opinion-on-Climate-Change-Initiatives

Understanding public opinion is essential for politicians and business people alike. Regarding climate change, understanding the relative popularity of climate change initiatives could provide insight for policymakers, indicating which policies are more popular and therefore politically feasible to implement. Using social media and natural language processing (NLP) techniques to evaluate this supplements traditional polling and survey methods, and likely captures the opinion of a different portion of the population.
Similarly, understanding popular opinion toward climate change could help businesses discover opportunities. In the context of well-established companies increasingly emphasizing sustainability, understanding which initiatives are popular could help them determine what to prioritize. This project could also provide some initial insight into potential market gaps for social entrepreneurs attempting to build sustainable businesses from the ground up. 
The main questions we are attempting to answer, with the goal of providing the insight described above, are: what are patterns in public perception of climate change policies? How have these perceptions changed over time?

# Sitemap

`Archive`
  - `Paris_v_GND_Try2.ipynb`: Experiment with prophet library
  - `gnd_location.py`: pyspark script to find locations from Twitter locations string
  
`EDA`: Exploratory data analysis
  - `A Starter Look Into Cleaning and Exploratory Data Analysis`: Initial look at recently scraped green new deal data
  - `Carbon Neutral EDA.ipynb`: EDA of recently scraped carbon neutral tweets
  - `Historical Data Set Starter Notebook.ipynb`: First look at subset of historical climate change data
  - `Paris Agreement EDA.ipynb`: EDA of recently scraped Paris Agreement data
  - `Plastic EDA.ipynb`: EDA of recently scraped tweets on plastic
  - `Project EDA and Topic Analysis.ipynb`: Complete EDA for recently scraped Green New Deal and Paris Agreement data
  
`Sentiment Analysis`
  - `Paris_v_GND.ipynb`: Sentiment Analysis, and attempt linear regression for sentiment analysis on hsitorical Twitter data
  - `Time Series Graph Sentiment Analysis.ipynb`: Sentiment over time
  - `Topic Sentiment Analysis, Paris.ipynb`: Sentiment analysis by topic (post-lda), historical data
  - `sentiment_analysis_gnd.ipynb`: Green new deal historical data sentiment analysis
  - `sentiment_analysis_paris.ipynb`: Paris historical data sentiment analysis
  - `time_series_prophet.py`: Script for prophet library
  - `topic_sentiment_analysis_gnd.ipynb`: Sentiment analysis historical green new deal data
  
`TwitterDataAnalysis`: scripts for scraping and processing the data
`Data`: place holder file for Twitter api user info

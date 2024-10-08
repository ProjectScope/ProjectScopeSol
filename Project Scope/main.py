from twitter_api import TwitterAPI
from cmc_api import CoinMarketCapAPI
from ai_analysis import AIAnalysis

# API keys (replace with your actual keys)
TWITTER_API_KEY = 'your_twitter_api_key'
# Replace with your Twitter API key
TWITTER_API_SECRET_KEY = 'your_twitter_api_secret_key'
# Replace with your Twitter API secret key
TWITTER_ACCESS_TOKEN = 'your_access_token'
# Replace with your Twitter access token
TWITTER_ACCESS_TOKEN_SECRET = 'your_access_token_secret'
# Replace with your Twitter access token secret
CMC_API_KEY = 'your_cmc_api_key'
# Replace with your CoinMarketCap API key
OPENAI_API_KEY = 'your_openai_api_key'
# Replace with your OpenAI API key

# Instantiate API handlers
twitter_api = TwitterAPI(
    TWITTER_API_KEY,
    TWITTER_API_SECRET_KEY,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_TOKEN_SECRET)
cmc_api = CoinMarketCapAPI(CMC_API_KEY)
ai_analysis = AIAnalysis(OPENAI_API_KEY)

# User input
project_name = input("Enter the cryptocurrency project name (e.g., Bitcoin): ")
twitter_username = input("Enter the Twitter username (without @): ")

# Fetch data
twitter_data = twitter_api.get_user_data(twitter_username)
cmc_data = cmc_api.get_project_data(project_name)

if cmc_data and twitter_data:
    # Analyze using AI
    analysis_result = ai_analysis.analyze_data(
        project_name,
        twitter_data,
        cmc_data)
    print("AI Analysis Result:\n", analysis_result)
else:
    if not cmc_data:
        print("Project not found in CoinMarketCap.")
    if not twitter_data:
        print("Failed to fetch Twitter data.")

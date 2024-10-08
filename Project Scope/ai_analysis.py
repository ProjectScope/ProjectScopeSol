import openai


class AIAnalysis:
    def __init__(self, api_key):
        # Replace with your OpenAI API key
        openai.api_key = api_key  # OpenAI API Key

    def analyze_data(self, project_name, twitter_data, cmc_data):
        prompt = (
            f"Analyze the following cryptocurrency project based on the provided data:\n\n"
            f"Project Name: {project_name}\n"
            f"Twitter Data: {twitter_data}\n"
            f"CoinMarketCap Data: {cmc_data}\n"
            f"Analyze certain criteria using twitter, cmc, and your existing database including: active social media + community, web presence, founder credibility, security audits, tokenomics and financials"
            f"Generate a sentiment score from 1 to 100."
            f"Use any useful links including social media and official pages"
        )
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message['content']
        except Exception as e:
            print(f"Error during AI analysis: {e}")
            return None

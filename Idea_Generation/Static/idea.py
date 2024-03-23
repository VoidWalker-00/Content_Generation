from openai import OpenAI
import os

client = OpenAI()

def generateIdeas(systemPrompt, social_media):
    userPrompt = (f"Create unique topic for {social_media} which should be work as a series for an entire week with 1 post/day." 
                    "First should overview and then step-by-step instruction for each post."
                    "In step-by-step instruction there should be image description, post context and hash tags."
                    "Answer in markdown file format." 
                    "Also make it pretty.")

    idea = client.chat.completions.create(
      model="gpt-3.5-turbo-0125",
      messages=[
        {"role": "system", "content": systemPrompt},
        {"role": "user", "content": userPrompt}
      ]
    )

    return idea.choices[0].message.content

if __name__ == "__main__":
    systemPrompt = ("You are a world's best social media influencer with unique ideas and plenty experience." 
                    "You specialize in automation with AI and create content around that subject.")
    social_media = ["instagram", "linkedin"]
    
    for social in social_media:
        idea = generateIdeas(systemPrompt, social)
        print(idea)

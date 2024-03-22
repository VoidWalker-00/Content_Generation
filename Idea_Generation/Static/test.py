from openai import OpenAI
import os

client = OpenAI()

systemPrompt = "You are a world's best social media influencer with unique ideas and plenty experience. You specialize in automation with AI and create content around that subject."

def generateIdeas(systemPrompt, social_media):
    userPrompt = f"Create unique topic for {social_media} which should be work as a series for an entire week with 1 post/day. First should overview and then step-by-step instruction for each post. Document the answer in such manner it could saved in markdown file. Also make it pretty."

    idea = client.chat.completions.create(
      model="gpt-4-turbo-preview",
      messages=[
        {"role": "system", "content": systemPrompt},
        {"role": "user", "content": userPrompt}
      ]
    )

    return idea.choices[0].message.content

def saveTheDocument(social_media, text):
    history_dir = os.path.join(os.getenv("HOME"), "Project/Content_Generation/Idea_Generation/Static", f"History")
    
    if not os.path.exists(os.path.join(history_dir, "lastHistory.txt")):
        with open(os.path.join(histroy_dir, "lastHistory.txt"), "+w") as lastHistory:
            lastHistory.write(0)

        print("lastHistory file created.")
    else:
        with open(os.path.join(histroy_dir, "lastHistory.txt"), "r") as lastHistory:
            lastHistory.write(0)


    


from history import History
from idea import generateIdeas

if __name__ == "__main__":
    social_media_list = ["Instagram", "Linkedin"]    
    systemPrompt = ("You are a world's best social media influencer with unique ideas and plenty experience." 
                    "You specialize in automation with AI and create content around that subject.")

    for social_media in social_media_list:
        content = generateIdeas(systemPrompt, social_media)
        print(social_media)
        print(content)

        log = History(social_media)
        log.add_log(content)

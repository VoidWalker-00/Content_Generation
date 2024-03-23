import os
import re
import time
from datetime import datetime

class History():
    def __init__(self, social_media):
        self.social_media = social_media
        self.history = os.path.join(os.getenv("HOME"), "Project/Content_Generation", "History/Static")
        self.history_file = os.path.join(self.history, f"Log-{self.social_media}.txt")
        self.name = "Idea"

    def store_doc(self, content, name):
        with open(os.path.join(self.history, self.social_media, f"{name}.md"), "+w") as doc:
            doc.write(content)
            print("Idea doc file stored.\n")

    def new_file(self, content):
        current_time = datetime.now()
        total_ideas = 1

        self.store_doc(content, f"{self.name}-{total_ideas - 1}")

        content = (
            f"Total Ideas Created: {total_ideas}\n"
            f"==============================\n"
            f"==============================\n"
            f"[{current_time.strftime("%Y-%m-%d %H:%M:%S")}] | {self.name}-{total_ideas - 1}.md Created\n"
        )
        with open(self.history_file, "+w") as history:
            history.write(content)

        print("New Log File Created.\n")

    def get_total_ideas(self):
        with open(self.history_file, "r") as log_file:
            lines = log_file.readlines()

        if lines and lines[0].startswith("Total Ideas Created:"):
            parts = lines[0].split(":")

            if len(parts) > 1 and parts[1].strip().isdigit():
                current_number = int(parts[1].strip())

        return current_number

    def update_total_ideas(self):
        with open(self.history_file, "r") as log_file:
            lines = log_file.readlines()

        new_number = self.get_total_ideas() + 1
        lines[0] = f"Total Ideas Created: {new_number}\n"

        with open(self.history_file, 'w') as log_file:
            log_file.writelines(lines)

        return new_number

    def add_log(self, content):
        current_time = datetime.now()

        with open(self.history_file, "a+") as log_file:
            log_file.seek(0)

            total_ideas = self.update_total_ideas()

            log_file.write(f"[{current_time.strftime("%Y-%m-%d %H:%M:%S")}] | {self.name}-{total_ideas - 1}.md Created\n")

        self.store_doc(content,  f"{self.name}-{total_ideas - 1}")

        print("Log File Updated.\n")

    def clear_file(self):
        open(self.history_file, "w").close()
        print("Log File Cleared.\n")


if __name__ == "__main__":
    history = History("Instagram") 
    history.clear_file()
    history.new_file("Generating Test Content")
    history.add_log("Generating Test Content")

    history = History("Linkedin") 
    history.clear_file()
    history.new_file("Generating Test Content")
    history.add_log("Generating Test Content")




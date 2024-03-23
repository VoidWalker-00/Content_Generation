import os
import re
import time
from datetime import datetime

class History():
    def __init__(self):
        self.history = os.path.join(os.getenv("HOME"), "Project/Content_Generation", "History/Static")
        self.history_file = os.path.join(self.history, "log.txt")

    def new_file(self, name):
        current_time = datetime.now()
        total_files = 1
        content = (
            f"Total Ideas Created: {total_files}\n"
            f"==============================\n"
            f"==============================\n"
            f"[{current_time.strftime("%Y-%m-%d %H:%M:%S")}] | {name}-{total_files}.md Created\n"
        )
        with open(self.history_file, "+w") as history:
            history.write(content)

        print("New Log File Created.\n")

    def update_total_ideas(self):
        with open(self.history_file, "r") as log_file:
            lines = log_file.readlines()

        if lines and lines[0].startswith("Total Ideas Created:"):
            parts = lines[0].split(":")

            if len(parts) > 1 and parts[1].strip().isdigit():
                current_number = int(parts[1].strip())
                new_number = current_number + 1  # Increment the number
                lines[0] = f"Total Ideas Created: {new_number}\n"

        with open(self.history_file, 'w') as log_file:
            log_file.writelines(lines)

        return new_number

    def add_log(self, name):
        current_time = datetime.now()

        with open(self.history_file, "a+") as log_file:
            log_file.seek(0)

            total_files = self.update_total_ideas()

            log_file.write(f"[{current_time.strftime("%Y-%m-%d %H:%M:%S")}] | {name}-{total_files}.md Created\n")

        print("Log File Updated.\n")

    def clear_file(self):
        open(self.history_file, "w").close()
        print("Log File Cleared.\n")


if __name__ == "__main__":
    history = History() 
    # history.clear_file()
    # history.new_file("Test_File")
    history.add_log("Test_File")

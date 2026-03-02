class AIManager:
    def __init__(self):
        self.__token_count = 0 #private variable


    def process_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                self.__token_count += len(line.split())

    def get_report(self):
        return f"Total tokens processed: {self.__token_count}"
    

if __name__ == "__main__":
    manager = AIManager()
    manager.process_file("Self_run/Token tracker/doc_2.txt")
    print(manager.get_report())
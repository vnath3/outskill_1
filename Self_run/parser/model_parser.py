def parse_model_response(file_path):
    try:
        with open(file_path, mode='r') as file:
            # Iterating directly over 'file' is memory efficient
            for line in file:
                # 1. Split by pipe to get segments
                segments = line.split("|")
                
                # Reset variables for each line
                id_val, sent_val, conf_val = None, None, None

                for part in segments:
                    # 2. Extract values based on keywords
                    if "ID:" in part:
                        id_val = part.split(":")[1].strip()
                    elif "Sentiment:" in part:
                        sent_val = part.split(":")[1].strip()
                    elif "Confidence:" in part:
                        conf_val = part.split(":")[1].strip()

                # 3. Final Output with formatting
                if id_val and sent_val and conf_val:
                    confidence_pct = float(conf_val) * 100
                    print(f"ID {id_val} is {sent_val} ({confidence_pct:.1f}% confidence)")

    except FileNotFoundError:
        print("Error: The file was not found.")

if __name__ == "__main__":
    parse_model_response("./Self_run/parser/model_output.txt")
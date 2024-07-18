import os
import pandas as pd
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to read and speak the definition
def read_definition(word, definition):
    print(f"Definition of {word}: {definition}")
    engine.say(f"Definition of {word}: {definition}")
    engine.runAndWait()

# Function to greet the user
def greet_user():
    greeting = "Hello! I am a dictionary assistant powered by Python. " \
               "I can help you find definitions of words. " \
               "Feel free to ask me anything!"
    print(greeting)
    engine.say(greeting)
    engine.runAndWait()

# Function to get the word's definition from the CSV file
def get_definition(word):
    first_letter = word[0].upper()  # Get the first letter and make it uppercase
    directory = "C:\\Users\\adity\\Desktop\\DICTIONARY\\Dictionary in csv"  # Adjusted for Windows file path
    file_path = os.path.join(directory, f"{first_letter}.csv")
    
    if not os.path.exists(file_path):
        print(f"No dictionary file found for words starting with '{first_letter}'.")
        return

    try:
        # Read the CSV file with the correct encoding
        df = pd.read_csv(file_path, encoding='latin1', header=None)  # Read without header
    except UnicodeDecodeError:
        print(f"Failed to read the file {file_path} due to encoding issues.")
        return

    # Search for the word in the DataFrame
    df.columns = ['Text']  # Name the single column
    df['Word'] = df['Text'].apply(lambda x: x.split(' ', 1)[0].lower())  # Extract the word
    df['Definition'] = df['Text'].apply(lambda x: x.split(' ', 1)[1] if len(x.split(' ', 1)) > 1 else '')  # Extract the definition

    row = df[df['Word'] == word.lower()]

    if row.empty:
        print(f"Word '{word}' not found in the dictionary.")
    else:
        definition = row.iloc[0]['Definition']  # Get the definition from the 'Definition' column
        read_definition(word, definition)

# Main function to run the dictionary AI
def main():
    greet_user()
    
    user_name = input("May I know your name? ").strip()
    print(f"Nice to meet you, {user_name}!")
    
    word = input("Now, please enter a word to get its definition: ").strip()
    get_definition(word)

if __name__ == "__main__":
    main()

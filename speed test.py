from sqlite3 import SQLITE_LIMIT_COMPOUND_SELECT
import time

def calculate_typing_speed(start_time, end_time, text):
    elapsed_time = end_time - start_time
    words = text.split()
    num_words = len(words)
    minutes = elapsed_time / 60
    wpm = num_words / minutes
    return wpm

def main():
    print("Welcome to the Typing Speed Calculator!")
    input("Press Enter when you're ready to start typing...")
    
    print("Type the following text as fast as you can:")
    text = "The quick brown fox jumps over the lazy dog"
    print(text)
    
    input("Press Enter to start typing...")
    start_time = time.time()
    
    user_input = input("Type the above text: ")
     
    
    end_time = time.time()
    wpm = calculate_typing_speed(start_time, end_time, user_input)
    print(f"Your typing speed is {wpm:.2f} words per minute (WPM)")

if __name__ == "__main__":
    main()



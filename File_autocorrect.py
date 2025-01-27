import re
import Levenshtein as lev

class FileHandler:
    def __init__(f, file_path):
        f.file_path = file_path
        f.file = None

    def open_file(f, mode='r'):
        try:
            f.file = open(f.file_path, mode)
            print(f"File '{f.file_path}' opened successfully in {mode} mode.")
        except FileNotFoundError:
            print(f"Error: The file '{f.file_path}' was not found.")
        except IOError as e:
            print(f"Error: Unable to open file. {e}")

    def close_file(f):
        if f.file:
            f.file.close()
            print(f"File '{f.file_path}' closed.")
        else:
            print("Error: File is not open.")

    def clean_word(f, word):
        cleaned_word = re.sub(r'[^\w\s]', '', word) 
        if cleaned_word.isdigit() or re.match(r'^\d+(\.\d+)?$', cleaned_word):
            return None  
        
        return cleaned_word.lower()  

    def cheak_file_errors(f, file_to_check):
        try:
            all_words = set()
            check_words = set()
            f.file_path = 'files\\wordList_250120.txt'
            f.open_file('r')
            for line in f.file:
                words_in_line = set(line.strip().split())
                for word in words_in_line:
                    cleaned_word = f.clean_word(word)
                    if cleaned_word:  
                        all_words.add(cleaned_word)
            f.close_file()
            f.file_path = file_to_check
            f.open_file('r')
            for line in f.file:
                words_in_line = set(line.strip().split())
                for word in words_in_line:
                    cleaned_word = f.clean_word(word)
                    if cleaned_word:  
                        check_words.add(cleaned_word)
            f.close_file()
            unique_words = check_words - all_words

            if unique_words:
                print(f"The following words in '{file_to_check}' are not recognized as English words:")
                for word in sorted(unique_words):
                    print(f"- {word}")
            else:
                print(f"All words in '{file_to_check}' are recognized as English words.")

            return unique_words

        except Exception as e:
            print(f"An error occurred: {e}")
        return set() 
    

    def compare_with_dictionary(f, unique_words):
        dictionary_words = set()
        matched_words_dict = {}

        
        f.file_path = 'files\\wordList_250120.txt'
        f.open_file('r')
        for line in f.file:
            words_in_line = set(line.strip().split())
            for word in words_in_line:
                cleaned_word = f.clean_word(word)
                if cleaned_word:
                    dictionary_words.add(cleaned_word)
        f.close_file()

        
        for word in unique_words:
            matched_words = []
            closest_distance = float('inf') 
            potential_matches = []  
            
            for dict_word in dictionary_words:
                distance = lev.distance(word, dict_word)

                if distance <= 1:
                    matched_words.append(dict_word)
                else:
                    if distance < closest_distance:
                        closest_distance = distance
                        potential_matches = [dict_word]
                    elif distance == closest_distance:
                        potential_matches.append(dict_word)
            
            if not matched_words:
                matched_words = potential_matches
            
            matched_words_dict[word] = matched_words
        
        return matched_words_dict


    

File1 = FileHandler("files\\sample_01.txt")
samplePath1 = "files\\sample_01.txt"

unique_words = File1.cheak_file_errors(samplePath1)

matched_words_dict = File1.compare_with_dictionary(unique_words)

print("\nError sample corrections:")
for word in sorted(matched_words_dict.keys()): 
    print(f"'{word}' -> Auto-correct: {matched_words_dict[word]}")
    print() 


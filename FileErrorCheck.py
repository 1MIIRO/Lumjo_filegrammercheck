import re

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

    def AccuracyCheck(f, file_to_check):
        try:
            unique_words = f.cheak_file_errors(file_to_check)
            total_words = 0
            f.open_file('r')
            for line in f.file:
                total_words += len(line.strip().split())
            f.close_file()
            mismatch_count = len(unique_words)
            if total_words > 0:
                mismatch_percentage = (mismatch_count / total_words) * 100
                Accuracy = 100 - mismatch_percentage
            else:
                mismatch_percentage = 0
            print(f"Number of errors: {mismatch_count}")
            print(f"The file's accuracy percentage: {Accuracy:.2f}%")

        except Exception as e:
            print(f"An error occurred: {e}")



File1 = FileHandler("files\\sample_01.txt") 
File2 = FileHandler("files\\sample_02.txt")
File3 = FileHandler("files\\sample_03.txt")
File4 = FileHandler("files\sample_04.txt")
samplePath1 = "files\\sample_01.txt"
samplePath2= "files\\sample_02.txt"
samplePath3 = "files\\sample_03.txt"
samplePath4 = "files\\sample_04.txt"
print("\n")
print("=== File 1:Error check===== ")
File1.cheak_file_errors(samplePath1)
File1.AccuracyCheck(samplePath1)
print("\n")
File1.close_file()
print("\n")
print("=== File 2:Error check===== ")
File1.cheak_file_errors(samplePath2)
File1.AccuracyCheck(samplePath2)
print("\n")
File1.close_file()
print("\n")
print("=== File 3:Error check===== ")
File1.cheak_file_errors(samplePath3)
File1.AccuracyCheck(samplePath3)
print("\n")
File1.close_file()
print("\n")
print("=== File 4:Error check===== ")
File1.cheak_file_errors(samplePath4)
File1.AccuracyCheck(samplePath4)
print("\n")
File1.close_file()




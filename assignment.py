print()
''' 1. Exploring Python's OS Module

Objective:
 The goal of this assignment is to deepen your understanding of the OS module in Python. 
 You will engage in tasks that involve file and directory operations, path manipulations, 
 and practical applications of these operations in real-world scenarios.

Task 1: Directory Inspector:

Problem Statement:
 Create a Python script that lists all files and subdirectories in a given directory. 
 Your script should prompt the user for the directory path and then display the contents.

Code Example:
import os
def list_directory_contents(path):
    # List and print all files and subdirectories in the given path

Expected Outcome:
 The script should correctly list all files and subdirectories in the specified directory. 
 Handle exceptions for invalid paths or inaccessible directories.
'''
import os

def list_directory_contents():
    print("Common Directory Paths are:\n'C:\\WIndows\\System32' for windows users \n'/Users/YourUsername/Documents' on Mac or linux")
    path = input("Please enter the directory path: ")
    
    try:
        if os.path.isdir(path):
            print(f"Listing contents of the directory: {path}")
            contents = os.listdir(path)
            for item in contents:
                print(item)
        else:
            print("The specified path is not a directory or does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

list_directory_contents()
print()
'''
Task 2: File Size Reporter:

Problem Statement:
 Write a Python program that reports the sizes of all files in a specific directory. 
 The program should ask the user for a directory path and then print each file's name and size within that directory.

Expected Outcome:
 Your program should display the name and size (in bytes) of each file in the given directory. 
 Ensure that the program only reports on files, not directories, and handles any errors gracefully.
'''

import os

def report_file_sizes():
    directory = input("Please enter the directory path: ")
    
    try:
        if os.path.isdir(directory):
            print(f"Reporting file sizes in the directory: {directory}")
            for entry in os.listdir(directory):
                entry_path = os.path.join(directory, entry)
                if os.path.isfile(entry_path):
                    size = os.path.getsize(entry_path)
                    print(f"{entry}: {size} bytes")
        else:
            print("The specified path is not a directory or does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

report_file_sizes()
print()

''' 
Task 3: File Extension Counter:

Problem Statement:
 Develop a Python script that counts the number of files of each extension type in a directory. 
 For instance, in a directory with five '.txt' files and three '.py' files, the script should report "TXT: 5" and "PY: 3".

Expected Outcome:
 The script should accurately count and display the number of files for each extension type in the specified directory. 
 Handle different cases of file extensions (e.g., '.TXT' and '.txt' should be considered the same).

'''

import os

def count_file_extensions():
    directory = input("Please enter the directory path: ")
    
    try:
        if os.path.isdir(directory):
            extension_counts = {}
            
            for entry in os.listdir(directory):
                entry_path = os.path.join(directory, entry)
                
                if os.path.isfile(entry_path):
                    _, extension = os.path.splitext(entry)
                    extension = extension.lower()
                    
                    if extension in extension_counts:
                        extension_counts[extension] += 1
                    else:
                        extension_counts[extension] = 1
            
            for ext, count in extension_counts.items():
                print(f"{ext.upper()}: {count}")
        else:
            print("The specified path is not a directory or does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

count_file_extensions()
print()

''' 2. Regex-Powered Text Data Processing

Objective:
 The purpose of this assignment is to harness the power of regular expressions (regex) in Python for advanced text data processing. 
 You will apply regex to extract, manipulate, and analyze data from text files, combining it with efficient file handling techniques.

Task 1: Email Extractor:

 Problem Statement:
 Write a Python script to extract all email addresses from a given text file (contacts.txt). The file contains a mix of text and email addresses.

File Example:

```
Contact List:
John Doe - john.doe@example.com
Jane Smith - jane.smith@gmail.com

For inquiries, please contact info@example.com
```

Code Example:
```python
import re
def extract_emails(filename):
    # Read the file and use regex to find and return all email addresses
```

Expected Outcome:
 The script should output a list of all unique email addresses found in the file. 
 Utilize regex to accurately identify email addresses amidst other text.
'''
import re

def extract_emails(filename):
    email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    
    unique_emails = set()
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                emails = email_pattern.findall(line)
                unique_emails.update(emails)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    
    return list(unique_emails)

emails = extract_emails("contact_list.txt")
print(emails)
print()

''' 3. Advanced Python Data Processing and Analysis Challenge
Objective:
This assignment is aimed at challenging your skills in advanced data processing and analysis using Python. 
It encompasses a broad range of topics, including file handling, regular expressions, data structures, and 
complex problem-solving, at a medium-hard difficulty level.

                             Task 1: Travel Blog Sentiment Analysis:

Problem Statement:
Perform sentiment analysis on a collection of travel blog entries stored in travel_blogs.txt. 
Identify and count the occurrences of positive words (e.g., "amazing", "enjoy", "beautiful") 
and negative words (e.g., "bad", "disappointing", "poor").

- Dataset Example: 

<div class='oc-markdown-custom-container oc-markdown-activatable' contenteditable='false' data-value='```

Travel Blog Entries:
"Our recent trip to the mountains was amazing! The scenery was breathtaking and we enjoyed every moment of it."
"The beach vacation was wonderful. We relaxed by the shore and soaked up the sun."
"The city tour was a bit disappointing. The guide wasn't very knowledgeable, and the attractions were overcrowded."
"Exploring the countryside was a unique experience. The landscapes were stunning, but the accommodations were poor."
"Despite the rain, our visit to the waterfall was memorable. The cascading water was mesmerizing."
"We had high hopes for the safari adventure, but it turned out to be lackluster. The wildlife sightings were scarce."
"The food on our trip was excellent. We sampled delicious local cuisine at every stop."
"The historical tour was enlightening. We learned so much about the culture and heritage of the region."
"Overall, our travel experience was fantastic. We made unforgettable memories and can't wait for our next adventure!"
'>
Travel Blog Entries:
"Our recent trip to the mountains was amazing! The scenery was breathtaking and we enjoyed every moment of it."
"The beach vacation was wonderful. We relaxed by the shore and soaked up the sun."
"The city tour was a bit disappointing. The guide wasn't very knowledgeable, and the attractions were overcrowded."
"Exploring the countryside was a unique experience. The landscapes were stunning, but the accommodations were poor."
"Despite the rain, our visit to the waterfall was memorable. The cascading water was mesmerizing."
"We had high hopes for the safari adventure, but it turned out to be lackluster. The wildlife sightings were scarce."
"The food on our trip was excellent. We sampled delicious local cuisine at every stop."
"The historical tour was enlightening. We learned so much about the culture and heritage of the region."
"Overall, our travel experience was fantastic. We made unforgettable memories and can't wait for our next adventure!"
```
Code Example:
```
Travel Blog Entries:
1. "Our recent trip to the mountains was amazing! The scenery was breathtaking and we enjoyed every moment of it."

2. "The beach vacation was wonderful. We relaxed by the shore and soaked up the sun."

3. "The city tour was a bit disappointing. The guide wasn't very knowledgeable, and the attractions were overcrowded."

4. "Exploring the countryside was a unique experience. The landscapes were stunning, but the accommodations were poor."

5. "Despite the rain, our visit to the waterfall was memorable. The cascading water was mesmerizing."

6. "We had high hopes for the safari adventure, but it turned out to be lackluster. The wildlife sightings were scarce."

7. "The food on our trip was excellent. We sampled delicious local cuisine at every stop."

8. "The historical tour was enlightening. We learned so much about the culture and heritage of the region."

9. "Overall, our travel experience was fantastic. We made unforgettable memories and can't wait for our next adventure!"
```
Expected Outcome:
 A summary report indicating the number of positive and negative words in the travel blogs, demonstrating the ability to process text data and apply basic sentiment analysis.

                                                         Task 2: Historical Weather Data Compiler

Problem Statement:
 Compile and analyze historical weather data from multiple files (weather_2020.txt, weather_2021.txt, etc.). Each file contains daily temperature data. Calculate the average temperature for each year and identify the year with the highest average.

- Dataset Example:
File: weather_2020.txt
python def analyze_blog_sentiments(blog_file): # Implement sentiment analysis logic on the blog file

Code Example:
2020-01-01,5°C 2020-01-15,6°C 2020-02-05,4°C 2020-02-20,7°C 2020-03-10,8°C 2020-03-25,
9°C 2020-04-05,12°C 2020-04-20,14°C 2020-05-05,17°C 2020-05-20,19°C 2020-06-05,22°C 
2020-06-20,25°C 2020-07-05,28°C 2020-07-20,30°C 2020-08-05,32°C 2020-08-20,
31°C 2020-09-05,27°C 2020-09-20,24°C 2020-10-05,19°C 2020-10-20,16°C 2020-11-05,
11°C 2020-11-20,9°C 2020-12-05,6°C 2020-12-20,4°C

Expected Outcome:
 An aggregated view of average temperatures for each year and identification of the year with the highest average temperature, showcasing data aggregation and analysis skills.
'''

# Task 1

def analyze_blog_sentiments(blog_file):
    import re
    
    positive_words = ['amazing', 'enjoy', 'beautiful', 'wonderful', 'excellent', 'memorable', 'fantastic']
    negative_words = ['bad', 'disappointing', 'poor', 'lackluster', 'scarce']
    
    positive_count = 0
    negative_count = 0
    
    word_pattern = re.compile(r'\b\w+\b', re.IGNORECASE)
    
    try:
        with open(blog_file, 'r') as file:
            for line in file:
                words = word_pattern.findall(line)
                for word in words:
                    if word.lower() in positive_words:
                        positive_count += 1
                    elif word.lower() in negative_words:
                        negative_count += 1
    except FileNotFoundError:
        print(f"The file {blog_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return {'positive': positive_count, 'negative': negative_count}

if __name__ == "__main__":
    sentiment_results = analyze_blog_sentiments("travel_blogs.txt")
    print(sentiment_results)
    print()


# Task 2

def analyze_weather_data(files):
    import re
    
    yearly_data = {}
    
    data_pattern = re.compile(r'(\d{4}-\d{2}-\d{2}),(\d+)')
    
    try:
        for file in files:
            print(f"Processing file: {file}")
            year = file.split('_')[1].split('.')[0]
            temperatures = []
            
            with open(file, 'r', encoding='utf-8') as f:
                for line in f:
                    print(f"Reading line: {line.strip()}")
                    match = data_pattern.search(line)
                    if match:
                        temperature = int(match.group(2))
                        print(f"Matched temperature: {temperature}")
                        temperatures.append(temperature)
                    else:
                        print("No match found")
            
            if temperatures:
                average_temp = sum(temperatures) / len(temperatures)
                yearly_data[year] = average_temp
                print(f"Year: {year}, Average Temperature: {average_temp}")
    except FileNotFoundError:
        print(f"The file {file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    if yearly_data:
        highest_avg_year = max(yearly_data, key=yearly_data.get)
        highest_avg_temp = yearly_data[highest_avg_year]
        return {'yearly_averages': yearly_data, 'highest_average': (highest_avg_year, highest_avg_temp)}
    else:
        return {'yearly_averages': {}, 'highest_average': None}

files_list = ['weather_2020.txt', 'weather_2021.txt']  
result = analyze_weather_data(files_list)
print(result)

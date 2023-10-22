import DataScraper
from algorithms import KMPAlgo, NaiveStringMatching, RabinKarpAlgo
import time

# yet to complete dont run this
url = input("Enter the URL you want to scrape: ")
scrapped_data = DataScraper.getWepageData(url)
algorithmselected = input("NaiveStringMatching  KMPAlgorithm  RabinKarbAlgorithm")
pattern = "reviewed"


# run algorithms
if algorithmselected == "NaiveStringMatching":
    start = time.process_time()
    wordCount = {}
    text_data = scrapped_data.split()
    # print(text_data)
    for word in text_data:
        if word in wordCount:
            continue
        else:
            count = NaiveStringMatching.naive_string_matching(scrapped_data, word)
            wordCount[word] = count

    end = time.process_time()
    print("time to run algorithm", (end - start) * 1000000, "ms")
    print(wordCount)

elif algorithmselected == "KMPAlgorithm":
    start = time.process_time()
    wordCount = {}
    text_data = scrapped_data.split()
    # print(text_data)
    for word in text_data:
        if word in wordCount:
            continue
        else:
            count = KMPAlgo.kmp_search(scrapped_data, word)
            wordCount[word] = count
    end = time.process_time()
    print("time to run algorithm", (end - start) * 1000000, "ms")
    print(wordCount)

elif algorithmselected == "RabinKarbAlgorithm":
    start = time.process_time()
    wordCount = {}
    text_data = scrapped_data.split()
    # print(text_data)
    for word in text_data:
        if word in wordCount:
            continue
        else:
            rk_search = RabinKarpAlgo.RabinKarp(scrapped_data, word)

            count = rk_search.search_pattern()
            wordCount[word] = count

    end = time.process_time()
    print("time to run algorithm", (end - start) * 1000000, "ms")
    print(wordCount)

else:
    print("please enter valid algorithm name")

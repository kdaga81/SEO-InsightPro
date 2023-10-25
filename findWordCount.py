import DataScraper
from algorithms import KMPAlgo, NaiveStringMatching, RabinKarpAlgo
import time


def getProcessTimeAndWordCount(scrapped_data, algorithmselected):

    wordCount = {}
    process_time = {}

    # run algorithms
    if "NaiveStringMatching" in algorithmselected:
        start = time.process_time()
        
        text_data = scrapped_data.split()
        # print(text_data)
        for word in text_data:
            if word in wordCount:
                continue
            else:
                count = NaiveStringMatching.naive_string_matching(scrapped_data, word)
                wordCount[word] = count

        end = time.process_time()
        process_time["NaiveStringMatching"] = (end - start)
        print("time to run NaiveStringMatching algorithm", (end - start) , "secs")


    if "KMPAlgorithm" in algorithmselected:
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
        process_time["KMPAlgorithm"] = (end - start) 
        print("time to run KMPAlgorithm algorithm", (end - start),  "secs")
        

    if "RabinKarbAlgorithm" in algorithmselected:
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
        process_time["RabinKarbAlgorithm"] = (end - start)
        print("time to run RabinKarbAlgorithm algorithm", (end - start), "secs")

    return wordCount, process_time

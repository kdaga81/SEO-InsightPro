import DataScraper
from algorithms import KMPAlgo, NaiveStringMatching, RabinKarpAlgo
import time


def getProcessTimeAndWordCount(scrapped_data, algorithmselected):
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
        process_time = (end - start) * 1000000
        print("time to run algorithm", (end - start) * 1000000, "ms")
        print(wordCount)
        return wordCount, process_time

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
        process_time = (end - start) * 1000000
        print("time to run algorithm", (end - start) * 1000000, "ms")
        print(wordCount)
        return wordCount, process_time

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
        process_time = (end - start) * 1000000
        print("time to run algorithm", (end - start) * 1000000, "ms")
        print(wordCount)
        return wordCount, process_time

    else:
        print("please enter valid algorithm name")
        return {}, 0

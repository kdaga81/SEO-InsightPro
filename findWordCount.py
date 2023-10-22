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
    NaiveStringMatching.naive_string_matching(scrapped_data, pattern)
    end = time.process_time()
    print("time to run algorithm", (end - start) * 1000000, "ms")

elif algorithmselected == "KMPAlgorithm":
    start = time.process_time()
    KMPAlgo.kmp_search(scrapped_data, pattern)
    end = time.process_time()
    print("time to run algorithm", (end - start) * 1000000, "ms")

elif algorithmselected == "RabinKarbAlgorithm":
    start = time.process_time()
    rk_search = RabinKarpAlgo.RabinKarp(scrapped_data, pattern)

    rk_search.search_pattern()

    end = time.process_time()
    print("time to run algorithm", (end - start) * 1000000, "ms")

else:
    print("please enter valid algorithm name")

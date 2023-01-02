""" Colombian Scrapper class."""
from selenium import webdriver
import datetime
import time

def disjunction(listoflists):
    """
    This is a method that i implemented for returning the disjunction of a list
    of lists, however, its computational complexity is O(n⁴) and i dont know if
    there is a way to do it better in a better complexity. This method is
    pending to be reviewed by someone who knows all about algorithms because i
    think it can be better.
    """
    print("Disjuntion...")
    disjunction_list = []
    for i in tqdm(listoflists): #n
        x_is_in = True
        for x in i: #n
            x_is_in = True
            for lis in listoflists: ##n
                if(x not in lis): #n
                    #print(f"{x} not in {lis}")
                    x_is_in = False
            if(x_is_in):
                disjunction_list.append(x)
                x_is_in = True
    lista = list(set(disjunction_list))
    print(f"disjunction done")
    return(lista)


class ColombianScrapper:
    def __init__(self,headless: bool , disjunction = False):
        """
        Initialize the methods for the class ColombianScrapper that will be
        the father of the the other scrappers.
        
        headless: specify if the driver is going to run in headless mode

        disjunciton_mode: specify if the results of each query are going to be
        a disjunction or a disjunction, if is a disjunction, all the scrapper
        data will be returned, else only the data that matches all the queries
        will be returned.
        """
        self.start_time = time.time() # is easier to store the time in seconds since epoch
        self.options = webdriver.ChromeOptions()
        self.headless = headless
        self.disjunction = disjunction
        if(self.headless):
            print("starting on headless mode")
            self.options.add_argument("--headless")
        self.options.add_argument("--disable-notifications")
        # Using Chrome driver because i think is faster (feel free to change it)
        self.driver = webdriver.Chrome(options = self.options) 
        # Results to store all the results
        self.results = []
        # Results by query list to store values for them applying intersection
        self.results_by_query = []
        # Queries recived in get_all_results_from_query method in each class
        # that is already implemented
        self.queries = []


class ColombianNewspaperPost:
    def __init__(self, url: str, driver):
        """
        ColombianNewspaperPost is a class from the idea of making a general
        scrapper for a colombian newspaper post, the idea is that every
        newspaper scrapper needs a way of processing a single post.

        url: recives the post url

        driver: recives the current driver that is executing the scrapper, this
        makes everything more simple.

        Some post scrappers needs to quit publicity and a lot of stuff, thats
        why this class is needed.
        """
        self.driver = driver 
        self.url = url

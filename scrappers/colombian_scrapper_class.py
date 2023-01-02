""" Colombian Scrapper class."""
from selenium import webdriver
import datetime
import time



class ColombianScrapper:
    def __init__(self,headless: bool , disjunction_mode: bool):
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
        self.disjunction = self.disjunction
        if(self.headless):
            print("starting on headless mode")
            self.options.add_argument("--headless")
        self.options.add_argument("--disable-notifications")
        # Using Chrome driver because i think is faster (feel free to change it)
        self.driver = webdriver.Chrome(options = self.options) 
        # Results to store all the results
        self.results []
        # Results by query list to store values for them applying intersection
        self.results_by_query = []
        # Queries recived in get_all_results_from_query method in each class
        # that is already implemented
        self.queries = []

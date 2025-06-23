#!/usr/bin/env python
import sys

import warnings

from datetime import datetime

from stock_advisor.crew import StockAdvisor

from dotenv import load_dotenv


load_dotenv()

def run():

    inputs = {

        'sector' : 'Technology'
    }

    try:

        result = StockAdvisor().crew().kickoff(inputs = inputs)

        print("\n\n=== FINAL STOCK RECOMMENDATION === \n\n")

        print(result.raw)

    except Exception as e:

        print(f"Error running the crew: {e}")    


if __name__ == "__main__":

    run()        


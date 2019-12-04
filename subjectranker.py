##############################################
#  Name: Subject line analyzer
#  Author: skyr__
#  Date : 03.12.2013
##############################################
import requests
import argparse
from bs4 import BeautifulSoup
import numpy as np

if __name__ == "__main__":
    
    # We setup the args
    parser = argparse.ArgumentParser()
    parser.add_argument('subjectline', help="Pass the subject line to analyze as an argument")
    parser.add_argument('source', help="Change the source of the checker.")
    args = parser.parse_args()

    if args.source == "1":
        # We setup the API url
        url = 'https://www.subjectline.com/Home/SubmitSubjectLine'
        # Setup the request
        data = requests.post(url, data={'txtSubjectLine': args.subjectline})

        # Soup the response
        soup = BeautifulSoup(data.text, 'html.parser')

        # Get the score from the element
        score = soup.find(id="slScore")['value']

        # Print the result
        print(score)

    elif args.source == "2":

        
        # We setup the API url
        url = 'http://emailsubjectlinegrader.com/home/analyze'
        # Setup the request
        data = requests.get(url, params={'text': args.subjectline}).json()

        print(data['TotalScore'])

    elif args.source == "3":
        url = 'https://subject-line-analyzer-api.automizy.com/analyze-subject-line.php'

        data = requests.get(url, params={'sessionId':'6339125706206075-7682761238966293-1575455173186', 'subjectLine':args.subjectline}).json()

        print(round(data['score']*100,0))

    elif args.source == "mean":
        
        score_list = []

        # We setup the API url
        url = 'http://emailsubjectlinegrader.com/home/analyze'
        # Setup the request
        data = requests.get(url, params={'text': args.subjectline}).json()

        score_list.append(int(data['TotalScore']))

        url = 'https://subject-line-analyzer-api.automizy.com/analyze-subject-line.php'

        data = requests.get(url, params={'sessionId':'6339125706206075-7682761238966293-1575455173186', 'subjectLine':args.subjectline}).json()

        score_list.append(int(round(data['score']*100,0)))

        print(np.mean(score_list))

    else:
        print("Error please check your requests")


    
    

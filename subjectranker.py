##############################################
#  Name: Subject line analyzer
#  Author: skyr__
#  Date : 03.12.2013
##############################################
import requests
import argparse
from bs4 import BeautifulSoup


if __name__ == "__main__":
    
    # We setup the args
    parser = argparse.ArgumentParser()
    parser.add_argument('subjectline', help="Pass the subject line to analyze as an argument")
    args = parser.parse_args()

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

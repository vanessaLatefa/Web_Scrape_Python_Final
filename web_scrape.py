#Importing.. searches for the named module, 
#creates a reference to that module in this namespace
# Since we are importing,
# we can access and make use of their libraries, 
# which are a bunch of code designed by other people.

import requests 
import urllib.request
import os

#Using this becuase I only want 
# to import a specif module.

from bs4 import BeautifulSoup
from urllib.request import urlopen
from termcolor import colored

#BeautifulSoup is a Python library 
#for pulling data out of HTML and XML files

#Setting the url we want to scrape
scrape = 'https://clbokea.github.io/exam/index.html#menu'

#Connecting to the URL 
# #sends a get request to the server
connection = requests.get(scrape)

#Specifying or parsing HTML 
#save it in a Beautifulsoup object
soup = BeautifulSoup(connection.text, "html.parser")
assign_p = ""
assign_title = ""
assignment_url = []


def createTheUrl():
#a method that finds all the link
#and locates the href attributes
#added the href_link, to create a url for each links of the assignment
#added the url to the assignment_url
    for i in range(3,7):
        one_at_a_time = soup.find_all('a')[i]
        href_link = one_at_a_time['href']
        href_url = 'https://clbokea.github.io/exam/' + href_link
        assignment_url.append(href_url)
   
def chooseALink():

    print(colored('    Here are the list of projects for ComputerScience 4th Semester',color='yellow', on_color=None, attrs=['bold']))
    print(colored('            _________________________________', color='cyan'))
    print(colored('            |_________Assignment 1__________|', color='cyan'))
    print(colored('            |_________Assignment 2__________|', color='cyan'))
    print(colored('            |_________Assignment 3__________|', color='cyan'))
    print(colored('            |_________Assignment 4__________|', color='cyan'))
    print()
    print()

#using the input method, when n is entered
#it will then match to the link's index
#handling the error using a print method
#when the enterd value doesnt match, the program asks again.

    n = input(colored('                 Enter a number: ', color='magenta', on_color=None, attrs=['bold']))
    if n == '1':
        assign_link = assignment_url[0]
        scrapeMe(assign_link) 
    elif n == '2':
        assign_link = assignment_url[1]
        scrapeMe2(assign_link)
    elif n == '3':
        assign_link = assignment_url[2]
        scrapeMe2(assign_link)
    elif n == '4':
        assign_link = assignment_url[3]
        scrapeMe(assign_link)
    else:
        print()
        print('     ///  The value entered cannot be found!   \\\\\\')
        chooseALink()
        

def scrapeMe(assignLink):
    #Connecting to the URL and requesting a get
    connection = requests.get(assignLink)
    #parsing HTML and save it in a Beautifulsoup object
    soup = BeautifulSoup(connection.text, "html.parser")
    find_h1 = soup.find('h1')
    #adding the h1 to this variable including a new line to be readable
    assign_title = find_h1.text + '\n'
    add_to_file(assign_title.upper())
    find_all_p = soup.find_all('p')
    
    #if string is found, please pass
    #meaning ignore
    for p in find_all_p:
        if 'NOTE: This is a ' in p.text:
            pass
        elif 'A html page looking like this' in p.text:
            pass
        elif 'Becomes'in p.text:
            pass
        elif 'The links to follow' in p.text:
            pass
        else:
            assign_p = str(p.text) + '\n'
            add_to_file(assign_p)
    
def scrapeMe2(assignLink):
    #Connecting to the URL
    connection = requests.get(assignLink)
    #parsing HTML and save it in a Beautifulsoup object
    soup = BeautifulSoup(connection.text, "html.parser")
    find_h1 = soup.find('h1')
    assign_title = find_h1.text + '\n' #adding the content to this variable including a new line to be readable
    
    add_to_file(assign_title.upper())
    find_all_li = soup.find_all('li')
    find_all_p = soup.find_all('p')
    
    
    
    for li in find_all_li:
        if 'Exam flow' in li.text:
            pass
        elif 'Assignment' in li.text:
            pass
        elif 'Assingment' in li.text:
            pass
        elif 'NOTE' in li.text:
            pass
        else:
            assign_li = str(li.text) + '\n'
            add_to_file(assign_li)

    for p in find_all_p:
        if 'If you like you' in p.text:
            pass
        elif 'Assignment' in p.text:
            pass
        elif 'The rules of the game' in p.text:
            pass
        elif 'NOTE' in p.text:
            pass
        else:
            add_p = str(p.text) + '\n'
            add_to_file(add_p)

def add_to_file(text):
    #please append and write the text to a readme file.
    with open('file.md', 'a+') as f:
        f.write(text)
        
def check_for_md_file():
    #check if the file exists, if yes, remove and create a new one.
    if os.path.exists('file.md'):
        os.remove('file.md')

def printContent():
    with open('file.md', 'r') as f:
            content = f.read()
            print(content)

def main():
    check_for_md_file()
    print()
    print()
    print(colored('             ------------WELCOME------------', color='red', 
    on_color=None, attrs=['bold']))
    print(colored('             --------------TO---------------', color='red', 
    on_color=None, attrs=['bold']))
    print(colored('             ------------PYTHON-------------', color='red', 
    on_color=None, attrs=['bold']))
    print(colored('             ----------WEB SCRAPER----------', color='red', 
    on_color=None, attrs=['bold']))
    print()
    print()
    

    createTheUrl()
    chooseALink()
    print()
    printContent()
    print(colored('         *** CONTENT IS ALSO SAVED IN file.md  ***', color='yellow',
    on_color=None, attrs=['bold']))
    print()
    
  

if __name__ == "__main__":
    main()

(AM I RESPONSIVE IMAGE)

# **Promotional Sales Review System**

## # Table of contents

1. [Link To Live Site](#linktolivesite)


## **LucidChart Diagram**

screenshot of lucid chart showing flow of processes.


## Overview

This is a system designed to review the promotional sales during the month. It is designed to be manager review only and will require a password to be put in correctly in order to activate the system.

This will then return values to the terminal to show key information for the management team to evaluate performance;
- It will start with the stock section, providing useful insites into the items that have been sold.
- It will then move onto the advisor review section and shows key information regarding performances.


## User Stories

The first time you run this code should be at the end of the first day; this will then run the code and complete the first update for the system.

The second and all further runs of the programme will display the same information but will show the managers up to date information regarding performance.

There will be some updates to the spreadsheets that will then allow further analysis to be displayed to the manager;
- As new information is inputted, the figures will be updated to reflect the up to date information.
- This can be updated as many times and will always pull the up-to-date information.

## Initial Set Up Steps

Setting up this project requires a few steps based on the functionality and requirements;
- Google Form,
- Google Sheets,
- Google Cloud Platform,
- Terminal.

### Google Form

The set up for the google form is relatively simple;
- Create a new form,
- Add a title to the document,
- Add the four different questions to the page: Date, Advisor, Item, Value,
- Set the requirements for each Question.
- In the responses page, click the green icon to create a spreadsheet for the responses.
- Once completed, this file needs to be made public so that anyone can access and view this form.

### Google sheet

The google sheet requires you to update the name of the spreadsheet before linking it to the GitPod editor. This must also be shared using the client email that is created as part of the creds.json file;
- In the Google Sheet, top right button that reads 'Share',
- Click on it and add in the email address, making sure that Editor is marked so that we can edit or read from the form.
- Once completed, this file needs to be made public so that anyone can access and view this sheet.

### Google Cloud Platform

This requires the most complex setting up as this creates additional files that must be suitably and correctly added in specific ways.

### Terminal

In order for the terminal to be able to access the information for the functions to run, I have processed installations and imported libraries;
- I have installed gspread for using the google sheet manipulation and google-auth for accessing the correct google spreadsheet. I have also installed pwinput to allow users to input passwords with a mask to protect the user's input characters.
- I have imported the required libraries at the top of my run.py file for gspread, google.oauth.service_account, OrderedDict and pwinput.
- The json file downloaded from the Google Cloud Platform has been added to the file list, but IMMEDIATELY added to gitignore due to the sensitive information contained within the codument, so as not to include in it my GitHub Repository.
- I have defined the scope for the document to be able to access the apis mentioned in the Google cloud platform section in order for me to pull information from a separate service.
- Finally, I have defined my CONSTANT variables in order to make sure they do not change during the manipulation of the database.

#### Features

The features of this app allow the user to maniulate data from a spreadsheet to allow managers to see a simple and analytical view of the inputted data. In order to complete these actions, the following features were implemented;
- A manager's log in is requested; to protect the input, I have added code to mask the input but must still be inputted correctly in order to access the rest of the information.
- There is a main menu which can be returned to from the end of each journey; sales, items and advisor reviews. These is also a 'Quit/Exit' option to terminate the terminal programme.
- These are passed through another validator before running the approriate function of displaying relevant information based on the option chosen
    - The Sales option totals the number of sales, then display total and average sales values.
    - The Item option displays a nice chart of each device that has been sold as part of the promotion and the number of sales for it. It also has a statement that displays the most popular item and the number of sales.
    - The Advisor option completes similar jorney to Item by displaying the advisors in the promotional sale as well as the number of sales made. This also has a statement that displays the summary information for the manager.
- At the end of each option, there is an input required if user would like to return to the main menu or exit the app completely.

## Testing

Code check has been processed on the Python Validator PEP8

[screenshot of pep8 code validator]

### Python

screenshot of validator

## Unfixed Bugs

This app currently has a single bug creates and infinite loop when completing a validation check on the "y or n" choice. In order to break out of the loops and return correct values to exit out of the programme instead of returning to previous functions, the code has been adjusted and mended and something now doesn't complete correctly. IN ORDER TO BREAK OF THIS LOOP YOU MUST PRESS CTRL + C which will terminate all functions of the terminal. I have attempted troubleshoot and had peer review on this code through slack and mentor meeting.

## Fatures to implement

The amount of information could be increased and more complex fucntion created to bring more math; such as pulling the total value sold for each device or the most popular device an particular advisor sells. These were too complex for my current programme and would have caused issues with the size of the terminal being able to hold all the informatin in one screen.

## Deployment

In order to deploy the project and allow other people to run the app and see it working, there are 3 methods to allow you to action this:

#### Forking and Cloning Repositories

Accessing GitHub and navigating to my repositories will allow users to copy my code, either by forking or cloning:
Accesing my repository and clicking on the code button next to Gitpod link will bring up a drop down to create a repository of your own in your own github repo. You can also download a zip file and copy the information into a new file of your own making to continue working on it.

### Local Deployment

this is how it is locally deployed

### Remote Deployment

this is how it is remotely deployed

## Credits

The project was inspired by the Love Sandwiches walkthrough. Thank you to the Code Institute for showing me the processes required to create a project like this.

Thank you to the following people and sites for their advice and contributions to helping me understand and be able to confidently create this project:

- Chris Quinn - Mentor
- Iryna Sanzhara - Slack
- https://pypi.org/project/pwinput/1.0.1/ - document to protect password input from anyone else viewing the input, improving user experience.
- https://thispointer.com/python-4-ways-to-print-items-of-a-dictionary-line-by-line/ - to help me display the information in a dictionary in a more easily read format to improve user experience.
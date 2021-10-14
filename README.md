(AM I RESPONSIVE IMAGE)

# **Promotional Sales Review System**

## # Table of contents

1. [Link To Live Site](#linktolivesite)
2. [LucidChart Diagram](#lucidchartdiagram)
3. [Overview](#overview)
4. [User Stories](#userstories)
5. [Initial Set Up](#initialsetup)
    1. [Google Form](#googleform)
    2. [Google Sheet](#googlesheet)
    3. [Google Cloud Platform](#googlecloudplatform)
    4. [GitHub](#github)
    5. [Terminal - Gitpod](#Terminalgitpod)
6. [Features](#features)
7. [Features to Implement](#featurestoimplement)
8. [Testing](#testing)
9. [Unfixed Bugs](#unfixedbugs)
10. [Deployment](#deployment)
    1. [Forking and Cloning](#forkingandcloning)
    2. [Local Deployment](#localdeployment)
    3. [Remote Deployment](#remotedeployment)
11. [Credits](#credits)

## Link to Live Site

add web address here

## LucidChart Diagram

Here is the diagram I created to map out the flow of the app and how I wanted it to work:

[Image of LucidChart Diagram](/workspace/promo-sales-review/assets/images/lucidchart-flow.png)

## Overview

This is a system designed to review the promotional sales during the month. It is designed to be manager review only and will require a password to be put in correctly to activate the system. Once the password is in, the first step is to retrieve the information from the input spreadsheet.

The system has evolved a couple of times; due to terminal size and dimensions, I have made further adjustments and required a method of shortening what was displayed in the terminal window;
- There is now a menu set up that allows the user to break down the information into choices that can be reviewed as many times and in any order.
- It also gives the user an option to exit the terminal function at any point - either by choosing the exit option or by choosing not to continue with the program after viewing a section.

## User Stories

The first time you run this code should be at the end of the first day; this will then run the code and complete the first update for the system.

The second and all further runs of the program will display the same information but will show the managers up-to-date performance information.

There will be some updates to the spreadsheets that will then allow further analysis to be displayed to the manager;
- As new information is inputted, the figures will be automatically updated to reflect the up-to-date information when the program is initiated.
- This can be updated as many times as needed and will always pull the up-to-date information.

## Initial Set Up Steps

Setting up this project requires a few steps based on the functionality and requirements;
- Google Form,
- Google Sheets,
- Google Cloud Platform,
- GitHub,
- Terminal.

### Google Form

The setup for the google form is relatively simple;
- Create a new form,
- Add a title to the document,
- Add the four different questions to the page: Date, Advisor, Item, Value,
- Set the requirements for each Question.
- On the responses page, click the green icon to create a spreadsheet for the responses.
- Once completed, this file needs to be made public so that anyone can access and view this form.

### Google sheet

The google sheet requires you to update the name of the spreadsheet before linking it to the GitPod editor. This must also be shared using the client email that is created as part of the creds.json file;
- In the Google Sheet, the top right button that reads 'Share',
- Click on it and add in the email address, making sure that Editor is marked so that we can edit or read from the form.
- Once completed, this file needs to be made public so that anyone can access and view this sheet.

### Google Cloud Platform

This requires the most complex setting up as this creates additional files that must be suitably and correctly added in specific ways. The process is listed in steps below to creating API Credentials:
- Create a new project (so that credentials are specific to the project), rename it and open it,
- Choose the APIS and services from the menu and choose a library,
- select the programs that are in use; Google Drive to start with as this is the storage space for the project. You would add google sheets API after completing the credentials part for drive API (you don't need to create the credentials for the sheet as well.)
- Once selected, you will need to enable the app, then create credentials from the option on the right:
    - Select which API to link (the app you selected),
    - Select which data to use (Application)
    - Select 'Not planning to use with compute engines'
    - Create a service name and click 'Create'
    - Make sure you make yourself editor on next section
    - Leave 'grant users access' blank, then select Done.
- You will now see the service account you created on the next page,
- Choose the keys tab and create a new key
- select the JSON file. (at this point you can now add the google sheets API to the service, but don't worry about the credentials again.)
- At this point you can download the credentials JSON file to use in your project file.

### GitHub

This is the hosting site for the project, create a new repository (in this case I used a template from Code Institute). Once it was created, I then used the Gitpod button to open the IDE to create the project.

### Terminal - Gitpod

For the terminal to be able to access the information for the functions to run, I have processed installations and imported libraries;
- I have installed gspread for using the google sheet manipulation and google-auth for accessing the correct google spreadsheet. I have also installed pwinput to allow users to input passwords with a mask to protect the user's input characters.
- I have imported the required libraries at the top of my run.py file for gspread, google.oauth.service_account, OrderedDict and pwinput.
- The JSON file downloaded from the Google Cloud Platform has been added to the file list, but IMMEDIATELY added to the gitignore file due to the sensitive information contained within the document, so as not to include in it my GitHub Repository.
- I have defined the scope for the document to be able to access the APIs mentioned in the Google cloud platform section for me to pull information from a separate service.
- Finally, I have defined my CONSTANT variables to make sure they do not change during the manipulation of the database.

## Features

The features of this app allow the user to manipulate data from a spreadsheet to allow managers to see a simple and analytical view of the inputted data. To complete these actions, the following features were implemented;
- A manager's login is requested; to protect the input, I have added code to mask the input but must still be inputted correctly to access the rest of the information.
- There is the main menu that can be returned to from the end of each journey; sales, items and advisor reviews. There is also a 'Quit/Exit' option to terminate the terminal program.
- These are passed through another validator before running the appropriate function of displaying relevant information based on the option chosen
    - The Sales option totals the number of sales, then displays total and average sales values.
    - The Item option displays a nice chart of each device that has been sold as part of the promotion and the number of sales for it. It also has a statement that displays the most popular item and the number of sales.
    - The Advisor option completes a similar journey to Item by displaying the advisors in the promotional sale as well as the number of sales made. This also has a statement that displays the summary information for the manager.
- At the end of each option, there is an input required if the user would like to return to the main menu or exit the app completely.

## Features to implement

The amount of information could be increased and more complex functions created to bring more math; such as pulling the total value sold for each device or the most popular device a particular advisor sells. These were too complex for my current program and would have caused issues with the size of the terminal being able to hold all the information on one screen.

## Testing

### Python

Code check has been processed on the Python Validator PEP8.

![PEP8 Code Validator](/workspace/promo-sales-review/assets/images/pep8-validator.jpg)

## Unfixed Bugs

This app currently has a single bug that creates an infinite loop when completing a validation check on the "y or n" choice. To break out of the loops and return correct values to exit out of the program instead of returning to previous functions, the code has been adjusted and mended and something now doesn't complete correctly. TO BREAK OF THIS LOOP YOU MUST PRESS CTRL + C which will terminate all functions of the terminal. I have attempted to troubleshoot and had peer review on this code through slack and mentor meetings.

## Deployment

To deploy the project and allow other people to run the app and see it working, there are 3 methods to allow you to action this:

#### Forking and Cloning Repositories

Accessing GitHub and navigating to my repositories will allow users to copy my code, either by forking or cloning:
Accessing my repository and clicking on the code button next to Gitpod link will bring up a drop-down to create a repository of your own in your own GitHub repo. You can also download a zip file and copy the information into a new file of your own making to continue working on it.

### Local Deployment

this is how it is locally deployed

### Remote Deployment

this is how it is remotely deployed

## Credits

The project was inspired by the Love Sandwiches walkthrough. Thank you to the Code Institute for showing me the processes required to create a project like this.

Thank you to the following people and sites for their advice and contributions to helping me understand and be able to confidently create this project:

- Chris Quinn - Mentor
- Iryna Sanzhara - Slack helper regarding my initial issues with validation check issues.
- https://pypi.org/project/pwinput/1.0.1/ - document to protect password input from anyone else viewing the input, improving user experience.
- https://thispointer.com/python-4-ways-to-print-items-of-a-dictionary-line-by-line/ - to help me display the information in a dictionary in a more easily read format to improve user experience.
- Slack - gleaning insights from other people's mentions and questions.
- Slack Overflow - providing some clues and information regarding issues that arose regarding validation of response in terminal inputs.
- GeekforGeeks - information regarding python functions and performances that would improve my app design.
- Code Institute - teaching me about the entire world of programming and introducing me to python and web development.
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
- Add teh four different questions to the page: Date, Advisor, Item, Value,
- Set the requirements for each Question.
- In the responses page, click the green icon to create a spreadsheet for the responses.

### Google sheet

The google sheet requires you to update the name of the spreadsheet before linking it to the GitPod editor.

### Google Cloud Platform

This require the most complex setting up as this creates additional files that must be suitably and correctly added in specific ways

### Terminal

In order for the terminal to be able to access the information for the functions to run, I have processed installations and imported libraries;
- I have installed gspread for using the google sheet manipulation and google-auth for accessing the correct google spreadsheet.
- I have imported the required libraries at the top of my run.py file for both gspread and google.oauth.service_account.
- The json file downloaded from the Google Cloud Platform has been added to the file list, but IMMEDIATELY added to git ignore due to the sensitive information contained within the codument.
- I have defined the scope for the document to be able to access the apis mentioned in the Google cloud platform section in order for me to pull information from a separate service.
- Finally, I have defined my CONSTANT variables in order to make sure they do not change during the manipulation of the database.

#### Features

The features of this app

## Testing

Code check has been processed on the Python Validator PEP8

[screenshot of pep8 code validator]

### Python

screenshot of validator

## Unfixed Bugs

Anything this app does that shouldn't or doesn't do that should?

## Fatures to implement


## Deployment

In order to deploy the project and allow other people to run the app and see it working, there are 3 methods to allow you to action this:

#### Forking and Cloning Repositories

Accessing GitHub and navigating to my repositories will allow users to copy my code, either by forking or cloning:
Accesing my repository and clicking on the code button next to Gitpod link will bring up a drop down to create a repository of your own in your own github repo. You can also download a zip file and copy the information into a new file of your own making to continue working on it.

### Local Deployment

this is how it is locally deployed

### Remote Deployment

thisis how it is remotely deployed

## Credits

Any credits for code or help that you have received.

Chris Quinn - Mentor
Iryna Sanzhara - Slack


# Flexicon - The flexible lexicon

README file for Data Centric Development Milestone Project

-----


[Flexicon App](https://flexicon-words.herokuapp.com/) </br>
[Flexicon GitHub Repo](https://github.com/sheldon18/flexicon)
</br></br></br>

<p align="center"><img src="https://user-images.githubusercontent.com/44424348/78756100-55ec6100-79ce-11ea-9969-cd07127840bc.JPG" /></p>


## About this website

This is a dictionary website for literally anyone to add new words and phrases that may be self-made-up or discovered elsewhere.
It is similar to urban dictionary, however with Flexicon, users can edit the existing words, definitions, pronunciations, etc., if they are aware of more suitable corresponding particulars.


## UX Features

- Simple and easy-to-use website to add new words or edit existing words
- Handy navigation bar to perform CRUD functions.
- Pop-out accordion for distinct appearance of the word being viewed.
- Responsive design for any device/layout.
- Every added, edited word is updated in the MongoDB Collections
- Parts of speech can also be added and edited
- Delete functionality removed in latest deploys to avoid users being able to delete words without administrator’s permission.
- EmailAPI added to the Delete buttons to enable user to request word deletion from administrator.
- Appealing and distinct yet soft and playful colour scheme used as this website is intended for humorous users.

## Wireframes


<p align="center"><img src="https://user-images.githubusercontent.com/44424348/78755946-1887d380-79ce-11ea-8df7-9addb9928adc.png" /></p>






## Technologies and External APIs

- For wireframes, I used the __Balsamiq Wireframes__ tool (as per pictures above).
- __HTML, CSS, JavaScript, Python, Flask, PyMongo, MongoDB Atlas__ technologies used.
- __CDNJS cloudfare__ script tag for executing jQuery.
- __Google Fonts__ API for website’s fonts.
- __Materialize__ and __Material Icons__ used for various elements such as accordion, navbar, forms, forms' icons, etc.
- Used GitHub issues section to generate links to add wireframe images to README.




## Process of creation

1. Wireframes created using Balsamiq Wireframes and updated with progress.

2. Database clusters and collections created in MongoDB.

3. Created AWS C9 project to code this app.

4. Installed Flask

5. App.py created to run the back-end of this website.

6. Heroku app created.

7. Variables created in app.py and added to Heroku before initial commit.

8. Deployed to Heroku using GitHub connection in Heroku so that all GitHub pushes are deployed to Heroku automatically.

9. Template inheritance added.

10. Materialize and material icons and Google Fonts API tags added

11. Static css added

12. CRUD functionality of the app added with corresponding templates. 
__Note:__ Delete functionality was removed to avoid users from deleting words. Delete button has been wired up to EmailAPI so that the user can send me an email to request deletion of a word with their reason for deletion. 
Ideally I would have liked to apply same functionality to all Delete buttons, however I have kept the Delete button functionality on the Parts of Speech page to demonstrate and satisfy project requirements. 


#### Testing & Code Validation

- __W3C Markup Validation Service__ used to validate HTML code by direct input.
- __W3C CSS Validation Service__ used to validate CSS code by direct input.
- __Chrome dev tools__ and __Mozilla inspect element tool__ used for testing HTML and CSS.
- Tested app.py with app.route 'Flask Test'
- All Python code conforms to PEP8 style guide
- Browser __console log__ used for layout, responsiveness and user actions.



#### User Testing

- if user opens app, they will reach the home page with all the added words
- if user clicks on Flexicon logo, they will reach the home page
- if user clicks on Words in the navbar, they will be directed to the home page
- if user click on Add Word button or New Word in navbar, they are directed to Add a new word page
- if user fills in all information and clicks on Submit Your Word, they will be directed to home page where their newly created word will appear. This will also be added to the MongoDB.
- if user fails to enter any fields in the form, form will no submit and they will be alerted to fill in required fields.
- if user clicks on Edit Button under each word, they will reach the edit page of that specific word.
- if user click on Submit Edit button, they are directed back to the homepage where their edited word will show will rest of the words.
- user can perform similar functions on parts of speech page
- if user clicks on Delete button under each word, their email app of their device will open, will the recipient as my email address and the Subject as: Flexicon - Delete Request - <word_name>
- tested all of the above on iPad and iPhone screens.

## Deployment

This project was developed using the AWS Cloud9, and deployed to Heroku via GitHub.

To deploy this page to Heroku, the following was done:
1. Created repo in __GitHub__
2. Pushed to GitHub from AWS C9
3. Created [Flexicon App](http://flexicon-words.herokuapp.com/) in __ Heroku__
4. Required Config Vars added
    - IP variable
    - PORT variable
    - MONGO_DBNAME Variable
    - MONGO_URI variable
5. App connected to GitHub Repo in Heroku deploy settings.
6. Deploy Branch set to __Master__
7. Enabled Automatic deploys so that all GitHub pushes are auto-deployed to Heroku

### Credits & Acknowledgements

- Stackoverflow
- W3schools
- Code Institute Tutorials
- This README file layout was based on my previous README files
- README image uploads were done with assistance from stackoverflow.
- Tutor Support assistance was used for select js validation.
- Besides materialize inputs, all other written code has been self-written.


#### Media

- Apple devices mockup [image](https://user-images.githubusercontent.com/44424348/78756100-55ec6100-79ce-11ea-9969-cd07127840bc.JPG) created using Multi Device Website Mockup Generator. 


#### Disclaimer

The content of this app is for educational and milestone project purposes only.

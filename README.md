# Bucketlist

## Deployed Site
![](assets/screenshots/website.gif)
[Live website](https://kimkesdev.github.io/YogaCity/.)

## Table of Contents
* [UX](#UX)
  * User Goals
  * User Stories
  * Strategy
  * Scope
  * Structure
  * Skeleton
  * Surface
  * Mockups
  * Database Schema
* Features
  * .
  * .
* Technologies
  * Languages
* Credits
  * Content
  * Media
  * Acknowledgements

## #UX

### User Goals

### User Stories
* A new user:
* A login user:


### Strategy

### Scope
A Landing Page that is easy to navigate.
A footer and navigation bar that change depending on whether the user is logged in or not.
A register and login form for users to either create a new account or to log in.
A My Account Page for users to view/edit/delete their posts, and an option to delete their account.
A Sign Out button that is easy to find on every page (preferably in the navigation bar).
An About page for both users and new visitors to see what the website does and how to use the website.
A Posts page where users can see all the posts on the website.
A way to filter posts so users can see the plants available in their area.

### Structure
Color Scheme

### Skeleton

### Surface

### Mockups
The following wireframes were created using Balsamiq to design the website layout options.
Homepage
Register page
Login page
Add intention page

### Database Schema

## Features
The webpage consists of the following features:

__The navigation bar__

__Footer__

__Registration page__
The form is set to give feedback if username is too short. There is also error checking against confirmation password mismatch and some basic password criteria. Passwords are hashed using bcrypt and then saved to the database, hashed passwords are compared on login attempt. Once registered the user ill be redirected to their profile page. There is also a link to go to the sign in page here.

__Login page__
The login page is simple, users can enter their username and password. This is authenticated in python and feedback is given if the credentials are incorrect. For security all passwords are hashed and the hashed versions are compared. Successfully signing in to the site will direct the user to their profile page. There is also a link here to register a new user.

__Profile page__
The profile page is a users space to 
This is also where you will delete your profile.

__Intentions Page__
CRUD - Read (view) all intentions
This page shows all the posts made on the website.

__Add Intention__
CRUD - Add a New Intention.
A simple form in the same style as all other forms on the website. When a user is logged in they can use this form to add a new intention. The following details need to be filled in on this form:
<ul>
  <li>
</ul>
When the Submit button is pressed the post is sent to the Mongo database and will show up on the main intentions page.

__Edit Intention__
CRUD - Update and Delete a Post
When the submit button is pressed the updated information gets sent to the database for that post.

### Code structure

### Features Left to Implement

## Technologies

### Languages
Python3 - Used for backend data manipulation <br>
PyMongo - Used to communicate with the mongoDB database <br>
[HTML5](https://en.wikipedia.org/wiki/HTML5) - Used as the main language for the templates <br>
[CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Used for styling the webpage <br>
[JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Used for some front end functionality

### Libraries/Frameworks/Tools
[Github](https://github.com/) - Used for version control <br>
Flask 1.0.2 - Used as the main framework for my application <br>
[Pixabay](https://pixabay.com/) - Free online images. Used for some images on website <br>
[Fontawesome](https://fontawesome.com/) - Used for some icons on the website <br>
[Materialize](https://materializecss.com/) - Used as the main frontend framework <br>
[Heroku](https://heroku.com/) - Used to host the website <br>
[GitHub](https://github.com/) Used to store my project source code <br>
[W3C](https://validator.w3.org/) Markup - Used this to check my HTML for errors and typos <br>
[W3C CSS](https://jigsaw.w3.org/css-validator/) - Used this to check the validity of my CSS

### Databases
[MongoDB](https://www.mongodb.com/)- Used as the main database technology

## Credits

### Content
The content is made up and written by me.

### Media
The photos used in this website were obtained from Pixabay.

### Acknowledgements
<ul>
  <li>Bootstrap4 Docs
  <li>Fontawesome Icons
  <li>Flask Docs
  <li>Mongo Docs
  <li>Slack
  <li>Google
  <li>YouTube
</ul>

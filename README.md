# Bucketlist

## Deployed Site
![](assets/screenshots/website.gif)
[Live website](https://bucketlist-2020.herokuapp.com/.)

## Table of Contents
* <a href="#user-content-ux" id="ux">UX</a>
  * <a href="#user-content-user-goals" id="user-goals">User Goals</a>
  * <a href="#user-content-user-stories" id="user-stories">User Stories</a>
  * <a href="#user-content-strategy" id="strategy">Strategy</a>
  * <a href="#user-content-scope" id="scope">Scope</a>
  * <a href="#user-content-structure" id="structure">Structure</a>
  * <a href="#user-content-skeleton" id="skeleton">Skeleton</a>
  * <a href="#user-content-surface" id="surface">Surface</a>
  * <a href="#user-content-mockups" id="mockups">Mockups</a>
  * <a href="#user-content-database-schema" id="database-schema">Database-Schema</a>
* <a href="#user-content-features" id="features">Features</a>
  * .
  * .
* <a href="#user-content-technologies" id="technologies">Technologies</a>
  * <a href="#user-content-languages" id="languages">Languages</a>
* <a href="#user-content-credits" id="credits">Credits</a>
  * <a href="#user-content-content" id="content">Content</a>
  * <a href="#user-content-media" id="media">Media</a>
  * <a href="#user-content-acknowledgements" id="acknowledgements">Acknowledgements</a>

## UX 

### User Goals

### User Stories
* A new user:
* A login user:


### Strategy

### Scope
* A Landing Page that is easy to navigate.
* A footer and navigation bar that change depending on whether the user is logged in or not.
* A register and login form for users to either create a new account or to log in.
* A My Account Page for users to view/edit/delete their posts, and an option to delete their account.
* A Sign Out button that is easy to find on every page (preferably in the navigation bar).
* A Posts page where users can see all the posts on the website.

### Structure
Color Scheme

### Skeleton

### Surface

### Mockups
The following wireframes were created using Balsamiq to design the website layout options.
![Homepage](.../img/homepage.jpg)


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

When the Submit button is pressed the post is sent to the Mongo database and will show up on the main intentions page.

__Edit Intention__
CRUD - Update and Delete a Post
When the submit button is pressed the updated information gets sent to the database for that post.

### Code structure

### Features Left to Implement

## Technologies

### Languages
* Python3 - Used for backend data manipulation 
* PyMongo - Used to communicate with the mongoDB database 
* [HTML5](https://en.wikipedia.org/wiki/HTML5) - Used as the main language for the templates 
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Used for styling the webpage
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Used for some front end functionality

### Libraries/Frameworks/Tools
* [Github](https://github.com/) - Used for version control 
* Flask 1.0.2 - Used as the main framework for my application 
* [Pixabay](https://pixabay.com/) - Free online images. Used for some images on website 
* [Fontawesome](https://fontawesome.com/) - Used for some icons on the website 
* [Materialize](https://materializecss.com/) - Used as the main frontend framework 
* [Heroku](https://heroku.com/) - Used to host the website 
* [GitHub](https://github.com/) Used to store my project source code 
* [W3C](https://validator.w3.org/) Markup - Used this to check my HTML for errors and typos
* [W3C CSS](https://jigsaw.w3.org/css-validator/) - Used this to check the validity of my CSS

### Databases
* [MongoDB](https://www.mongodb.com/)- Used as the main database technology

## Credits

### Content
The content is made up and written by me.

### Media
The photos used in this website were obtained from [Pixabay](https://pixabay.com/).

### Acknowledgements
* [Code Institute course](https://codeinstitute.net/)
* [YouTube](https://www.youtube.com/)

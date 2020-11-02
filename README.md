# Bucketlist

## Deployed Site

## Table of Contents
<ul>
  <ol>UX
    <li>User Goals
    <li>User Stories
    <li>Strategy
    <li>Scope
    <li>Structure
    <li>Skeleton
    <li>Surface
    <li>Mockups
    <li>Database Schema
  <ol>Features
    <li>
    <li>
  <ol>Technologies
    <li>Languages
  <ol>Credits
    <li>Content
    <li>Media
    <li>Acknowledgements
</ul>

## UX

### User Goals

### User Stories
<ul>
  <li>A new user:
  <li>A login user:
  <li>
  <li>
  <li>
  <li>
  <li>
  <li>
</ul>

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

<strong>The navigation bar</strong>

Footer
Registration page

The form is set to give feedback if username is too short. There is also error checking against confirmation password mismatch and some basic password criteria. Passwords are hashed using bcrypt and then saved to the database, hashed passwords are compared on login attempt. Once registered the user ill be redirected to their profile page. There is also a link to go to the sign in page here.

Login page
The login page is simple, users can enter their username and password. This is authenticated in python and feedback is given if the credentials are incorrect. For security all passwords are hashed and the hashed versions are compared. Successfully signing in to the site will direct the user to their profile page. There is also a link here to register a new user.

Profile page
The profile page is a users space to 
This is also where you will delete your profile.

Intantions Page
CRUD - Read (view) all intentions
This page shows all the posts made on the website.

Add Intention
CRUD - Add a New Intention.
A simple form in the same style as all other forms on the website. When a user is logged in they can use this form to add a new intention. The following details need to be filled in on this form:
<ul>
  <li>
</ul>
When the Submit button is pressed the post is sent to the Mongo database and will show up on the main intentions page.

Edit Intention
CRUD - Update and Delete a Post
When the submit button is pressed the updated information gets sent to the database for that post.

Code structure

Features Left to Implement

## Technologies

### Languages
<ul>
  <li>Python 3 - Used for backend data manipulation
  <li>PyMongo - Used to communicate with the mongoDB database
  <li>HTML5 - Used as the main language for the templates
  <li>CCS3 - Used for styling the webpage
  <li>JavaScript - Used for some front end functionality
</ul>

### Libraries/Frameworks/Tools
<ul>
  <li>Git - Used for version control
  <li>Flask 1.0.2 - Used as the main framework for my application
  <li>Pixabay - Free online images. Used for some images on website.
  <li>Fontawesom - Used for some icons on the website
  <li>Materialize - Used as the main frontend framework
  <li>Heroku - Used to host the website
  <li>GitHub Used to store my project source code
  <li>W3C Markup - Used this to check my HTML for errors and typos.
  <li>W3C CSS - Used this to check the validity of my CSS.
</ul>

### Databases
<ul>
  <li>MongoDB - Used as the main database technology
</ul>

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

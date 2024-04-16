# SFBnB 

Airbnb-like Web Application

## Description

This is a university project for a web application built with Python, Flask, and SQLite3. The main goal was to create an Airbnb-like experience, focusing on meeting specific assessment requirements rather than implementing user authentication and login features.

## The current project now does the following: 

- Allows anyone to **leave a review** - which is entered into the database and displayed in the html table below after submitted.
- Allows anyone to **upvote or downvote** the recent reveiws, which are counted and displayed next to the rating in negative or positive amounts of up/downvotes.
- Allows anyone to **delete reviews**

- A **simple registration** enables users to register a profile,and login. The way the database pulls the correct users is by **saving a cookie as the user ID** during registration or login. When the profile page is rendered, the username corresponding with the respective ID stored in the cookie is displayed in the html. Cookies were chosen as I found it easy to access them on client & server.

## Technologies Used

For this project I chose to work with language Python and use the Flask framework. As I had knowledge of this from the first Foundation Semester I participated in with Adam Roe, in 2019. I found it easier to recall this knowledge instead of using Javascript and the Express framework, as presecribed in the class. 
For my database I chose to use SQLite3 as I had also used it during my first attempt at SE19 & SE01 in 2019. 

## Project Requirements 

- **HTML Pages**: The project includes at least 3 HTML pages that are linked to each other.
- **CSS Styling**: All pages are styled using CSS rules.
- **Responsive Design**: Pages are responsive and use media queries with at least 2 breakpoints.
- **Routes**: There are at least 3 different routes in the application.
- **Dynamic Route**: The application includes at least one dynamic route that allows users to access different pages with different URLs, all handled by a single route function in the backend.
- **Database Connection**: There is a working database connection with at least one data model.
- **Templating Language**: A templating language is used to render the database entries within the HTML.
- **CRUD Operations**: CRUD operations are implemented.
- **Deployment**: The application is deployed using Render.
- **Error-Free**: The application works without errors.
- **Code Quality**: The code is clean and follows best practices.

## Deployment

[Link to Deployed Website](https://web-basics-hand-in-04.onrender.com) 

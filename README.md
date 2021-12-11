# Team 2 -Easy Ride



* This is a group submission for final project. We have used Angular as front end framework and Django as backend framework.



* Date Created: 8th November 2021



* Last Modification Date: 10 Dec 2021



## Getting started



* Make sure you have installed Django in the system.You can check the version using the command "python -m django --version". you can install it from Here, then run npm install to resolve all dependencies (might take a minute).



* Run ng serve for a dev server. Navigate to http://localhost:4200/. The app will automatically reload if you change any of the source files.



## Building the project



* To run the project, use "python manage.py runserver". After that the project will build and start.



## Functionality overview



* The given website is a carpooling website build for working professional in Halifax who wants to commute to their work. The car owner can be anyone who wants to share ride expenses to the working professionals. The live Demo of our website is at: http://easy-ride-share.herokuapp.com/main/home-page.



## Repository Url:



* Frontend URL: https://github.com/mh342039/easy-ride



* Backend URL: https://github.com/akshay-garg-dal/Easy-Ride---Carpooling-




## Link to Jira:



* Added with this email (ms450806@dal.ca): https://easy-ride.atlassian.net/jira/software/projects/ER/boards/1/backlog





## Demo Video Link:



* https://www.youtube.com/watch?v=YwYRfGlg5Nw





## General functionality:



* We have following features in our web application:



* Login/Sign-up



* Update Profile



* Ride search on the basis of the start and destination location along with Date and time of the Departure. And number of passenger booking



* User can also publish ride



* User can modify publish ride



* User can Delete publish ride



* User can see all past rides in Myride



* If while searching user does not mention the ride search details then all the ride in the system will be available to the user



## The general page breakdown looks like this:



## Home page (URL: /main/Homepage)



* Contains search ride menu



* Contains FAQS, Contact Us, Terms & Conditions



* Login/Signup button on the top right corner



## Login /Sign up/ Logout pages (URL: /main/Homepage)



* Uses JWT (store the token in local Storage)



* Authentication can be easily switched to session/cookie based



* After sign-in session is created and the session is maintained until user clicks on logout



## Search-Result page (URL: /main/search-result)



* Filtered results are shown on the basis of the source and destination of the ride along with date and time



* If user has not mentioned any specified information then all the rides in the application will be shown



## Publish a Ride (URL: /main/publish-ride)



* Ride publisher needs to give information about ride title, Leaving from, Destination, Time, and price



* Reset button is also available to reset the content field



## My Ride (URL: /main/my-rides)



* Fetched all the information from the Database about the past rides the given user has published or taken



* User has a option to delete and update the ride details.



## Profile (URL: /main/profile)



* Fetched all the information from the Database and populates fields such as Firstname, Lastname, EmailAddress, phone.



* User can just view the details, Update the details by changing any of the mentioned details or user can delete the account as well.



* User has a option to delete and update the ride details.



# Authors:



* Mohammed Hamza Jasnak 
* mh342039@dal.ca  



* Grant Chesney 
* Gr953532@dal.ca 



* Preethi Jeeva 
* pr316875@dal.ca  



* Neelay Jayantbharti Goswami 
* nl339853@dal.ca 



* Akshay Garg 
* ak561005@dal.ca 



* Dharaben Thakorbhai Gohil 
* dh447205@dal.ca  

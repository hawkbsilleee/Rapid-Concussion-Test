# rapid-concussion-test
Flask application hosting a prototype rapid concussion test using varying sine wave patterns. 

There are two testing modes, thickness test and contrast test, which display sine patterns that vary in thickness or contrast over time. The user should focus on the center target which flashes with random numbers. As soon as the user sees the sinusoidal wave pattern they should click on the quadrant where they see it. 

<img width="1440" alt="Screen Shot 2024-11-22 at 11 51 40 AM" src="https://github.com/user-attachments/assets/4bf2f022-74e7-40a9-9835-85f795d674bb">

<img width="1439" alt="Screen Shot 2024-11-22 at 11 52 49 AM" src="https://github.com/user-attachments/assets/59470e5f-1565-4c4d-91bb-629ea36d4dc0">

<img width="1440" alt="Screen Shot 2024-11-22 at 11 52 31 AM" src="https://github.com/user-attachments/assets/e1fd7291-bab9-4bb3-b10b-dee8db45b8b8">


A version of this application is hosted via server at this url: https://rippler.pythonanywhere.com/index.html. (UPDATE: This site no longer works).  

## Run app
To run the flask app locally run the following command in terminal `python3 app.py`. This will run the backend python file which runs the website. In terminal you will see that flask provides you with the url to access the site (which can be done through a webrowser). To navigate to the home page of the app you must add "/index.html" to the end of the url that flask provide. Together it should be something like this "http://127.0.0.1:5000/index.html". 

### Login Info
User: padula1,
Password: 0604 

## File Structure 
### app.py
The main python backend running the flask application. Contains routes for each page, chooses the quadrant in which the ripple animation is run, and tracks the elasped time of the test.

### utils.py
Handles user authentification.

### requirements.txt
Use this file to see which external modules and versions this project is using. 

### static/css/style.css
Contains the css styling for all html pages. Also uses a css animation function to drive the sine wave annimation (iterfacing w/ the anim#.html files). 

### static/imgs
Where logos or any images are stored. 

### static/js/main.js
This is the only javascript used on this site, providing the random number functionality of the central target. This file generates a random number and sends it to one of the anim#.html files. 

### templates/index.html 
Home page

### templates/anim#.html
Four different html files that are practicly the same. Span classes are called by the css file to create circles for the annimation. 
The location of the "covers" change depending on each animation file for each quadrant. 

### templates/results#.html 
Four different html files that are practicly the same. The python file will render one of the results files based on which quadrant was presented. 







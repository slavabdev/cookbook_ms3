<h1 align="center">Easy Peasy recipes website</h1>

<div align="center">

[View the project here.]( https://cook-book-vb.herokuapp.com/)
</div>

<h2 align="center"><a href="https://ibb.co/M5Rf9WT"><img src="https://i.ibb.co/LhCrvbw/food-screenshot.png" alt="food-screenshot" border="0"></a><h2 align="center">

### **Legend**:
This is a website of **Easy Peasy recipes**  – for people who like to cook, eat and share their recipes with the public and supposed to be clear and user-friendly as well as responsive for different types of devices.

### Core audience of the website (CA):
-  People who love to cook and always looking for new recipes online;
-  People who like to share their recipes with friends and public;


### Website business goals
* Build an 'Easy Peasy' brand awareness among the CA representatives;
* Attract audience to the 'Easy Peasy' social media pages using the website;
* Build a community around 'Easy Peasy' brand;
* To attract advertisers on the website (food and kitchen equipment producers and others).
## UX
### User stories:
- As a **new visitor**, I want to understand what this website about and what its purpose. 
- As a **new visitor**, I want to easily navigate the site to get a content what I need;
- As a **new visitor**, I want to see a website, which works properly on my device;
- As a **new visitor**, I want to see a fully-filled website with up-to-date information;
- As a **new visitor** I want to have an ability browse all the recipes published on the site;
- As a **new visitor** I want to be able to filter recipes by categories and search them using keywords;
- As a **new visitor**, I want to see a modern website with a pleasant colour palette.

- As an **interested visitor** I want to easily create an account on the site;
- As an **interested visitor** I want to have an ability to add/edit/delete my recipes on/from the website;
- As an **interested visitor** I want to easily navigate through recipes I posted;
- As an **interested visitor** I want to get more information about the 'Easy Peasy' company and check their social media pages
- As an **interested visitor**, I want to see the most popular recipes on the website.

### Design
- Color Scheme:
One of the main task was to make website pleasing to the eye. By this reason the accent were made on the following colors: 
    - mustard [#ffd977](#);
    - milky(`#fafafa`);
    - dark grey (#212121). 
- Typorgaphy:
  - There are three fonts used in the website Montserrat,Roboto and Train One – convenient and frequently used in web design. 
    - The Train One were chosen for the navigation items.
    - The Montserrat font (with Sans Serif in case of fallback) is predominately used for all the headings and subheadings on the website. 
    - The Roboto font (with Sans Serif in case of fallback) used text and the main text of the sections. 
### Wireframe
  - [View the website wireframe.](https://drive.google.com/drive/folders/1lv4rL3surdlCxzjNL3ihrcwngYiybCT3?usp=sharing)
### Database structure
•	The database **cook_book** consists of two collections: 'recipes' and 'users'.
- Recipe Structure
    1.	_id - ObjectId - (created by mongoDB)
    2.	category - str
    3.	recipe_title - str
    4.	cook_time- str
    5.	description - str
    6.	ingredients - str
    7.	method - str
    8.	image_url - str
    9.	count - int
    10.	author - str
- Users
    1.	_id - ObjectId - (created by mongoDB)
    2.	username - str
    3.	password - str - (password hash created and provided by werkzeug.security)

## Features
- **Website summary**
  - Website consist of 5 pages, which available for all users: [Home](http://cook-book-vb.herokuapp.com/home), [Recipes](http://cook-book-vb.herokuapp.com/recipes), [Register](http://cook-book-vb.herokuapp.com/register), [Login](http://cook-book-vb.herokuapp.com/login) and Recipe (link can change depending on recipe).  
  - And 3 pages, which available only for registered users Profile, Add recipe and Edit recipe.
    - 404 page display if requested page doesn’t exist.
    - For user’s comfortable navigation, every section inside the pages has a large and perceptible heading.
### The website features are:
- **Navigation bar**
  - The website use customized Materialize navigation bar. It is a navbar with a logo placing on the top-left and menu items on the top-right. When browsing the website from mobile devices, menu item list becoming a burger-button with a half-screen right-side list. 
  - For user’s convenient navigation, navigation bar has a fixed position. 
- **Footer**
  - The website use customized Materialize Footer as well. The footer is divided on 2 blocks. First one includes short description of EasyPeasy website and social media icons with *hover effect* and active links to the social media pages. At the current moment, social media links lead to the home page of the particular social media websites. 
  -  Second block has a dynamic copyright caption. Which updates the year, based on the current date.
- **HOME PAGE**
    - Besides navigation bar and footer **Home page** consists of **3 sections**: 
    1. Materialize Carousel. There are 2 slides in carousel. Every slide includes heading, short description and call to action button for convenient navigation between sections and pages. 
       
    2. Categories
        - The Categories section is made with Materialize grid system to be concisely and responsive depending on a screen size.  There are a three categories of recipes that user can find or upload on the website. Every category has a call to action button, which lead to the Recipes page and filter all recipes by chosen category. 
        - Below the categories user can find call to action button, which redirect the user to recipes page (with all recipe list).
    3. Popular recipes.
        - A 'Popular recipes' section is made with Materialize grid system to be concisely and responsive depending on a screen size.  The section includes 3 cards of the recipes with the highest recipe page views (Recipes arranged from higher to lesser views quantity).
        - Every recipe has a responsive image, title, cook time, description (reveals when clicking the arrow button) and a button, which leads to the recipe page. All recipes information is pulled from the database.  
- **RECIPES**
    - Recipes page can be displayed in 2 ways: 
    - **All recipes** (default option). User can see all the recipes published on the website (retrieve from database and renders on page).
    - **By categories** (when user was redirected to recipes page by choosing a particular category on a Home page). In this case only recipes from the corresponding categories render to the page.
    - The title of the page will be changed as well according the above mentioned.  
    1. **Search**  
        - The search takes a text input, it retrieves all recipes from the database which have the inputted reference in either the recipe name or description, otherwise it returns the information that nothing found.
    2. **Recipe**
        - A recipes section is made with Materialize grid system to be concisely and responsive depending on a screen size.  Every recipe has an image, title, cook time, description (reveals when clicking the arrow button) and a button, which leads to the particular recipe page. All recipes data is pulled from the database.  
- **AUTHENTIFICATION**
    - The site uses authentication. Only users that have registered/signed up to the site can conduct the following actions:
        - Have an access to the personal account page (profile), where they can see the list of recipes added to the site by them.
        - Add recipes to the site / Edit & Delete recipes added by themselves.

- **Profile page**
    - This page renders all the recipes made by particular user from database and display them on the Profile page.
    This page includes following actions:
        - Page get the user name from database (users collection) and display it on the top of the page (with greetings).
        - For the users convenience after greeting text call to action button located. This button redirects to 'Add recipe' page.
        - Below the 'Add recipe' button user recipes cards located. This section is made with Materialize grid system to be concisely and responsive depending on a screen size. Every card display recipe image, the title and cooking time. These data retrieved from database. 
            - There are 3 buttons on the bottom of every card: View recipe, edit and delete. 
                1. View recipe button link to the particular recipe page;
                2.	Edit recipe button redirect to the ‘edit-edit’ recipe page;
                3.	Delete button allows to delete the recipe from database.
- **Recipe page**
    - This page renders the information on particular recipe  taken from the database.
    - All recipe details, including image, are pulled from the database and rendered in the separate parts of the page. Sections separates by headings and border lines. 
- **New Recipe Page**
    - The add recipe section is a form which should be fully filled to add recipe to the database and display on the website. In this developer to a Materialized form and customized it. 
        - The categories drop-down select box include 3 categories: Dessert, Main and Appetizer. User can choose the one which correspond to the dish he wants to upload.
        - Other steps include text input fields (except cootime, which is a number) which must be filled by user. 
        - The final step is adding an image. This step can be completed by adding a url of a desirable image, which corresponds to the particular dish. If link is 'broken', 'plug-image' will be appeared.
    - Upon submitting the form, data is passed into the 'recipes' database, hosted with MongoDB.
- **Edit Recipe Page**
    - The edit recipe page renders the same form as the 'new recipe' page. The only difference that the form will have been already filled with data from database, which corresponds to the particular recipe.
    - Users can 'edit' a recipe which was added to the site by them.
    - Users can then edit all the data which they want and submit changes to the database by clicking 'Submit Changes'.
### Things to implement in future
- Add ability (for registered users) to rate recipes, and add them to the favorites.
- Add an ability to add the comments at the recipes page.
- Add an option to add ingredients and methods by separate lines and upload images (more than one) from the device.
## Technologies used
- **Languages Used:**
  - [HTML5](https://en.wikipedia.org/wiki/HTML5)
  - [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
  - [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    - [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)) 
    - [Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine))
- **Frameworks, Libraries & Programs Used:**
1.	[Materialize 1.0.0](https://materializecss.com/)
     - Materialized was used to assist with the responsiveness and styling of the website.
2.  [Google Fonts](https://fonts.google.com/):
    - Google fonts were used to import fonts into the style.css file which are used on the website.
3.	[Font Awesome](https://fontawesome.com/): 
     - Font Awesome was used to add icons to locations page and footer of the website.
4.	[jQuery](https://jquery.com/):
    - Used throughout the site to target and manipulate HTML elements    
5.	[Git](https://git-scm.com/):
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
6.	[GitHub](https://github.com/):
    - GitHub is used to store the projects code after being pushed from Git. 
7.	[Figma](https://www.figma.com//):
    - Figma was used to create the wireframe.
8.	[GitPod](https://gitpod.io/):
    - GitPod was used as an IDE to develop a project. A project was built on a gitpod template of the Code institute.
9. [Heroku](https://www.heroku.com/)
    - Heroku was used a hosting for the project deployment.
10. [MongoDB](https://cloud.mongodb.com/) 
    - used to host the project data
## Testing
All-testing has been documented [Testing.md](https://github.com/slavabdev/cookbook_ms3/blob/master/Testing.md)
## Deployment
This project was developed using the GitPod, committed to Git and pushed to [GitHub repository](https://github.com/slavabdev/cookbook_ms3/).
- The following GIT commands were used throughout deployment:
```console
    - git status ------ used to check the status of files and any changes made / untracked.
    - git add ------ to stage files ready to commit.
    - git commit -m " " ------ to commit the files.
    - git push ------ to push the files to the master branch of the GitHub repo.
```
### Hosting on Heroku
- This [site](http://cook-book-vb.herokuapp.com/) is hosted using Heroku, deployed directly from the master branch via GitHub.
- The following steps were taken to complete the hosting process.
    1. Set debug=False in the server.py file.
    2. Created a requirements.txt file from the terminal, using pip3 freeze --local > requirements.txt, to allow Heroku to detect this project as a python app and any required package dependencies.
    3. Created a Procfile using echo web: python server.py > Procfile from the Gitpod terminal so Heroku would be informed on which file runs the app and how to run this project.
    4.	Created a new Heroku app, cook-book-vb and set its region to Europe.
    5.	Automatic deployment was set up on Heroku - On the app dashboard, in the deploy menu. Connect to GitHub section. The GitHub repository was searched for and connected to the app.
    6.	In the settings tab on the app dashboard, 'Reveal Config Vars' was used to tell Heroku which variableS are required to run the app. The following config vars were added:
        - IP
        - PORT
        - SECRET_KEY
        - MONGO_URI
        - MONGO_DBNAME
    7. In GitPod, a check was completed to ensure the master branch was up to date and all commits had been pushed to GitHub, ready for Heroku to deploy.
    8.	Clicked the Enable Automatic Deploys button located in the Deploy section of Heroku to allow for automatic deploys.
    9.	Clicked the Deploy Branch button located in the Deploy section of Heroku to finally deploy this project.
    10.	Clicked the View button to launch this project's app.
- The deployed site on Heroku will update automatically upon new commits to the master branch in the [GitHub Repository](https://github.com/slavabdev/cookbook_ms3/).

### Forking the GitHub Repository
A forking the GitHub Repository is used for copying of the original depository to  GitHub account. It allows viewing or making changes in the project without affecting the original repository. It can be done using the following steps: 
1.	Log in to GitHub and go to the GitHub Repository.
2.	At the top-right of the page, just below the GitHub navigation bar, the "Fork" Button is located.
3.	Click the “Fork” button and get a copy of the original repository to a GitHub account. 
### Run project locally
1.	Log in to GitHub and locate the GitHub Repository.
2.	Click a “Code” dropdown button, which located just under the “Settings”.
3.	To clone the repository using HTTPS, copy the link with clone URL.
4.	Open Git Bash in your local IDE.
5.	Change the current working directory to the location where you want the cloned directory to be made.
6.	Type git clone, and then paste the URL you copied before.
```console
git clone https://github.com/SLAVABDEV/REPOSITORY
```
7.	Press Enter. Your local clone will be created.
```console
$ git clone https://github.com/slavabdev/cookbook_ms3
> Cloning into `Spoon-Knife`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
### Content
- All content was written by the developer.
### Media
- All images were taken from [unplush](https://unsplash.com).
    - https://unsplash.com/photos/KPDbRyFOTnE?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
    - https://unsplash.com/photos/lK1Q5RyD6tc?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
    - https://unsplash.com/photos/fdlZBWIP0aM?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
    - https://unsplash.com/photos/awj7sRviVXo?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
    - https://unsplash.com/images/food?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  
### Acknowledgements
- Friends and family for helpful feedback.
- My Mentor Oluwafemi Medale for support and useful feedback.
- Code Institute for teaching me how to make coding magic.

# Testing
The W3C Markup Validator and W3C CSS Validator Services were used in the project to ensure there were no syntax errors.
* [W3C Markup Validator](https://validator.w3.org/nu/)
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
   - One mistake in Materialize URI https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css detected
* [JSHint](https://jshint.com/)
* [PEP8](http://pep8online.com/) 

### Manual testing of all elements and their functionality.

- **NAVIGATION BAR**:
    - Hover over the logo and navbar items and verify that the colour is changed.
    - Click on the logo to make sure that it links to the homepage.
    - Click all the navbar items to verify that they work and lead the user to correct pages.
    - Change the screen size from desktop to tablet and from tablet to mobile to make sure that the navigation bar switches from the inline menu to burger dropdown menu. Check all menu items to verify that they are clickable, on the correct place  works well.

- **FOOTER**:
    - Hover over each social media icon and make sure that colour change expected.
    - Click on each icon to confirm that the link opens in a separate tab.
    - Play with the window width to verify that the footer is responsive and looks good for different screen sizes
    - Confirm that footer code is the same on all HTML pages.
- **HOME PAGE**
    - Open the page in different browsers and scroll it down to make sure that everything displays correctly. 
    - Carousel
        - Click on the dots to verify that the carousel works correctly and all slides are displayed accurately.
        - Hover over the buttons to make sure that they change the colour.
        - Click the buttons to verify that they link with the correct sections/pages.
        - Expand and reduce a screen size to verify that slider looks good on different screen widths. 
- Categories section
    - Expand and reduce a screen size to verify that this section looks good on different screen widths.
    - Confirm that all images and text are display properly.
    - Click the buttons to verify that they link to the Recipes page, which opens using correct filtering.
- Popular recipes
    - Confirm that every card gets the correct content from the database. 
    - Expand and reduce a screen size to verify that section looks good on different screen widths. 
    - Click the arrow-up button to confirm that it reveals a correct recipe description. 
    -Click the arrow-down button to confirm that it hides recipe description. 
    - Click the buttons to verify that they link with the correct recipe pages.

- **RECIPES PAGE**
    - Confirm that all uploaded recipes are visible.
    - Expand and reduce a screen size to verify that the page and all the components looks good on a different screen widths. 
- Search
    - Confirm that page title display the correct value ('category name' if came by the category link from the fome page; or 'All recipes') 
    - Print the text that is exactly in some of recipes and check if search will find it.
    - Print the text that is not in recipes and check if search will return 'Nothing found' message.
- Recipes
    - Hover over the buttons to verify that they change its colour;
    - Click the arrow-up button to confirm that it reveals a correct recipe description. 
    -Click the arrow-down button to confirm that it hides recipe description. 
    - Click the buttons to verify that they link with the correct recipe pages.

- **AUTHENTIFICATION**
    - Confirm that all content is visible
    - Expand and reduce a screen size to verify that the page and all the components looks good on a different screen widths. 
    - Confirm that un-registered/unauthorised user can't see the 'Profile', 'Logout' and 'Add recipe' items on the navbar and don't have an access to this pages.
    - Confirm that registered/authorised user can't see the 'Register' and 'Login' items on the navbar.
- Register 
    - Confirm that it is unable to register without filling the whole registration form.
    - Confirm that it is unable to register with the existing users username (and corresponding flash message appears)
    - Confirm that after registration user get a flash message and redirected to the all recipes page.
- Login
    - Verify that it is unable to login without filling the whole  form.
    - Confirm that it is unable to login with the adding incorrect username/password (and corresponding flash message appears).
    - Confirm that after log in user get a corresponding flash message and redirected to the all recipes page.
- Logout    
    - Confirm that after clicking a 'logout' in the navigation section user will be popped out of the session, get a corresponding flash message and redirected to the 'login' page.
- **PROFILE**
    - Confirm that all content is visible
    - Expand and reduce a screen size to verify that the page and all the components looks good on a different screen widths.
    - Confirm that if user haven't uploaded recipes yet, they will see a corresponding message. 
    - Verify that username, taken from the database (users collection) display correctly.
    - Make sure that 'Add recipe' button redirect to corresponding page. 
- Recipes
    - Make sure that only users recipes display on their profile page
    - Confirm that every recipe card display properly and get the correct content from database.
    - Confirm that every recipe has a 'VIEW RECIPE', 'EDIT' and 'DELETE' buttons
    - Make sure that 'VIEW RECIPE' and 'EDIT' buttons link to the correct pages.
- **NEW RECIPE**
    - Confirm that all content is visible
    - Expand and reduce a screen size to verify that the page and all the components looks good on a different screen widths.
    - Confirm that it is unable to submit the form without filling the whole form.
    - Verify all validation is not present throughout the form as specified below:
        - Title - text (Minimum 5 characters) 
        - Description - text (Minimum 30 characters) 
        - Cook_time - is an integer  
        - Ingredients - text (Minimum 5 characters) 
        - Method - text (Minimum 5 characters)   
        - image_URL - text (Minimum 5 characters)  
    - Verify that on clicking 'Add recipe' button, recipe will be posted to database and the user gets a corresponding flash message.
- **EDIT RECIPE**
    - Confirm that all content is visible
    - Expand and reduce a screen size to verify that the page and all the components looks good on a different screen widths.
    - Confirm that it is unable to submit the form without filling the whole form.
    - Verify all validation is in place as specified for the 'New Recipe' page
    - Verify all fields are automatically filled in from the database, with corresponding recipe information.
    - Verify any changes are submitted to the database when the 'Submit Changes' button is clicked.
- **DELETE RECIPE**
    - The recipe can be deleted from website and database directly from the 'Profile' page by clicking 'Delete' button.
    - Verify that by clicking the 'delete' button user will get 'pop-up window' to ensure that the user wants to delete a recipe.
    - Make sure that after confirmation recipe will be deleted from the website and database.
- **RECIPE**
    - Confirm that all content is visible
    - Expand and reduce a screen size to verify that the page and all the components looks good on a different screen widths.
    - Verify all recipe info is rendered from the database correctly and in full.
    - Verify backup placeholder image renders if recipe IMG/URL path is broken (error).
    - Verify that backup placeholder image will be displayed correctly on the all pages, where the particular recipe appear
    - Make sure that every visit on the recipe page is counting.



- ## [Manual testing results](https://drive.google.com/drive/folders/1PxYaCnti41b-D8P_lKoXvAM7GNKRpJ8Y?usp=sharing)

## **Testing User Stories from User Experience (UX) Section**
- As a **new visitor**, I want to understand what this website about and what its purpose. 
    - Upon entering the site, the user sees the company logo on the navigation bar and a slider with themed images and сall to action content. When scrolling down the home page, the user can easily understand what the website purpose.
- As a **new visitor**, I want to easily navigate the site to get a content what I need;
    - The website has a clear and understandable, responsive and fixed navigation bar, which allow to user navigate the pages and sections easily.
    - User can navigate the website using navigation bar as well as buttons located on pages. 
- As a **new visitor**, I want to see a website, which works properly on my device;
    - Website is made fully responsive, so it’s convenient to browse on a desktop, laptop, tablet and mobile devices. 
    - Website works stably with different browsers as well.
- As a **new visitor** I want to have an ability browse all the recipes published on the site;
    - There are few options how user can browse the recipes:
        - They can check All recipes on the website by clicking a corresponded link on the navigation bar, or the button on the Home Page (below category section)
        - They can check recipes by chosing a specific category from the category list on the Home page.
- As a **new visitor** I want to be able to filter recipes by categories and search them using keywords;
    -  For users convenience they can filter recipes by category by clicking a particular button on the home page (category section).
    -  Users can search the recipes by title or  ingredients through all the recipe page.
- As a **new visitor**, I want to see a modern website with a pleasant colour palette.
    - The website (including the buttons, forms and content) is made in one style and using pleasant colour palette.

- As an **interested visitor** I want to easily create an account on the site;
    - User can easily access to the registration page by clicking a corresponding link on the navigation bar or by clicking call to action butoon on the slider. Registration process is quick and doesn't require a multiple actions.
- As an **interested visitor** I want to have an ability to add/edit/delete my recipes on/from the website;
    - Every registered user have an ability to upload, edit and delete their own recipes. For users convenience, all these actions can be held from the Profile page. 
- As an **interested visitor** I want to easily navigate through recipes I posted;
    - All recipes posted by user will appear on the users profile page.
- As an **interested visitor** I want to get more information about the 'Easy Peasy' company and check their social media pages
    - All links to the Easy Peasy social media pages are located in the footer of every page of the website.
- As an **interested visitor**, I want to see the most popular recipes on the website.
    - Top 3 recipes are located on the bottom part of the home page and have a corresponding title.

### Further testing
- The website was tested on the following browsers:
    * Google Chrome;
    * Opera;
    * Mozilla Firefox; 
    * Microsoft Edge; 
    * Safari.
- To be sure that website is responsive, it was viewed on such devices as desktops, laptops, tablet (Samsung galaxy tab A), and mobile (Iphone 6, IPhone X, IPhone XS Max, IPhone11 PRO MAX, Samsung Galaxy S10) .
- All buttons, forms and links have been tested several times to make sure they work correctly.
- Friends and family members reviewed the website from their devices to make sure that website is displaying well and all functions are working properly. 
### Known Bugs
- On the Iphone X (Safari) Materialize select button has 2 dropdown arrows - custom (by Materialize) and default. Sometimes Materialize dropdown menu doesn't respond properly on touch. It can confuse the user.


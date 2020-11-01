# Frankie's Kitchen Testing

All code used for Frankie's Kitchen was extensively tested through manual process during every stage of development to ensure that it works as intended and any bugs found were fixed. The responsive design of the website was tested on various devices and browsers.

During the coding process I found a bug where GitHub auto-formatting would not work as intended so I had to format the code manually in many places.

## Table of Contents

1. [**Code Validation**](#code-validation)

2. [**Testing Against User Stories**](#testing-against-user-stories)

3. [**Manual Testing**](#manual-testing)
    - [**Responsive Design Testing**](#responsive-design-testing)
        - [**Overview**](#overview)
            - [**Navbar**](#navbar)
            - [**Landing Page**](#landing-page)
            - [**Search Results Page**](#search-results-page)
            - [**Recipe Page**](#recipe-page)
            - [**Add Recipe Page**](#add-recipe-page)
            - [**Manage Recipe Page**](#manage-recipe-page)
            - [**404 Page**](#404-page)
            - [**500 Page**](#500-page)

    - [**Functionality Testing**](#functionality-testing)

        - [**Base Template**](#base-template)
            - [**Breakdown of Jinja Functionality in Base Template**](#breakdown-of-jinja-functionality-in-base-template)
            - [**Breakdown of CSS Functionality in Base Template**](#breakdown-of-css-functionality-in-base-template)
            - [**Base Template - Breakdown of Views Used**](#base-template---breakdown-of-views-used)

        - [**Landing Page Template**](#landing-page-template)
            - [**Breakdown of jQuery Functionality in Landing Page Template**](#breakdown-of-jquery-functionality-in-landing-page-template)
            - [**Landing Page Template - Breakdown of Views Used**](#landing-page---breakdown-of-views-used)

        

        - [**Search Page Template**](#search-page-template)
            - [**Breakdown of Jinja Functionality in Search Page Template**](#breakdown-of-jinja-functionality-in-search-page-template)
            - [**Search Page Template - Breakdown of Views Used**](#search-page---breakdown-of-views-used)

        - [**Recipe Page Template**](#recipe-page-template)
            - [**Breakdown of Jinja Functionality in Recipe Page Template**](#breakdown-of-jinja-functionality-in-recipe-page-template)
            - [**Breakdown of jQuery Functionality in Recipe Page Template**](#breakdown-of-jquery-functionality-in-recipe-page-template)
            - [**Recipe Page Template - Breakdown of Views Used**](#recipe-page---breakdown-of-views-used)

        - [**Add Recipe Page Template**](#add-recipe-page-template)
            - [**Breakdown of Jinja Functionality in Add Recipe Page Template**](#breakdown-of-jinja-functionality-in-add-recipe-page-template)
            - [**Breakdown of jQuery Functionality in Add Recipe Page Template**](#breakdown-of-jquery-functionality-in-add-recipe-page-template)
            - [**Add Recipe Page Template - Breakdown of Views Used**](#add-recipe-page---breakdown-of-views-used)

        - [**Manage Recipe Page Template**](#manage-recipe-page-template)
            - [**Breakdown of Jinja Functionality in Manage Recipe Page Template**](#breakdown-of-jinja-functionality-in-manage-recipe-page-template)
            - [**Breakdown of jQuery Functionality in Manage Recipe Page Template**](#breakdown-of-jquery-functionality-in-manage-recipe-page-template)
            - [**Manage Recipe Page Template - Breakdown of Views Used**](#manage-recipe-page---breakdown-of-views-used)

        - [**404 Page Template**](#404-page-template)

        - [**500 Page Template**](#500-page-template)

        - [**Functions**](#functions)
            - [**Image Upload**](#image-upload)
            - [**Recipe Steps**](#recipe-steps)
            - [**Recipe Ingredients**](#recipe-ingredients)

    - [**pylint**](#pylint)
    - [**Lighthouse Chrome developer tools**](#Lighthouse-Chrome-developer-tools)

## Code Validation

All code written has been thoroughly validated and passed through the following online validators:

- HTML - All code was run through the [W3C HTML Validator](https://validator.w3.org/) to ensure it was valid code and no errors were made. I used the [Web Developer](https://chrispederick.com/work/web-developer/) plugin for the chrome browser to pass the local HTML into the W3C validator on every page of the website.

- CSS - All styling was run through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to ensure it was valid and no errors were made.

- jQuery - All my script was run through the [JSHint](https://jshint.com/) validator and no errors were found.

- Python - All code was run through [PEP8](http://pep8online.com/).All code is PEP8 compliant.

## Testing Against User Stories

The below goes through of of the user stores listed in the UX section of the [README.md](https://github.com/Dhracko/frankies_kitchen/blob/master/README.md).

**As a user, I want:**

1. The website will provide a visually appealing manner.

    - The landing page of the website uses soft colours that compliment each other to make the user easy to read and navigate.

    - There are various pictures of food such as the search banner and the recipe images that are uploaded by users to help reinforce to the user that the site is about food and sharing recipes.

    - The user is not presented to a lot of text but instead is is behind the images of the cards so when the user hovers the mouse over the card flips and reveal the short description, the time to cook it and the portions that serves.

    - The interactivity of the landing page helps the user understand immediately what they can interact with - such as expanding navbar buttons, images that flip over as the cursor scrolls over it, and buttons/links that change colour on hover.

2. Be able to navigate myself around the site with ease and with as little guidance as necessary.

    - This has been achieved by clearly labeling all buttons and links that a user can interact with in addition to this, when a user hovers over a link or button it will either increase in size on mouse hover or it will change colour.

    - When recipes are displayed, for instance in a search result or on the landing page, the entire image and text area are links.

    - When the user is on certain pages such as the landing page or add recipe page then the corresponding link in the navbar is assigned the active class to make it a different colour and stand out to the user.

3. The users can locate a recipe by searching from a word in the name and get all the result.

    - This has been achieved by showing the recipes with the containing word within the name, the user is able to search for recipes using the search bar functionality.

    - A feature that will be implemented at a later date will allow a user to search for all recipes by ingredients.

4. This is a website where the user can store and easyly access cooking recipes. The recipes will have fields such as description, ingredients, preparation method, cooking time and portions.
    
    - This was achieved by allowing the user to create a new recipe with the different fields.

    - It was also allowing the users to put a link of the recipe for other so see.

    - If the user didn't have or want to upload an image then the server would asign a generic image.

    - A future feature will be to allow the user to upload the images straigh to the server.

5. The user can edit recipes, change any of the fields or even delete the recipe.

    - On the recipe page, the user is able to delete the recipe by pressing on the "Delete" button. If the user clicks it then a modal is launched to ask the user if they are sure they want to delete the recipe? This has been added to ensure recipes are not accidentally deleted.

    - On the recipe page, the user is able to edit the recipe by clicking on the "Edit" button. Upon on clicking on the button the recipe fields become available for the users to change any field. The user is able to delete ingredients or step method.
    The user is able to add any ingredient or step methods.
    
## Manual Testing

I have detailed the manual testing undertaken during the development stage to ensure that the design is responsive and free of bugs.

### Responsive Design Testing

During every stage of development, I used a variety of tools to test out the layout of the website to ensure that it remained responsive at various screen sizes, that the website retained the correct look, and all elements were displayed correctly and readable by the user.

For testing the various media screen sizes, I used the built-in options that were available through the Chrome browser as well using the [Responsive Test Tool Website](http://responsivetesttool.com/) as this gave access to a wider range of screen and device sizes.

All tests were performed on the following browsers:

- Google Chrome
- Opera
- Microsoft Edge
- Mozilla Firefox
- Safari

All testing was performed at the following screen sizes:

- Mobile Phones/ Small Devices (Portrait and Landscape) - All available through Chrome and Firefox Dev Tools.
  - Additional Emulated Devices - Nexus 7, iPod Touch, Galaxy Note 3, Nexus 6P, LG G5
  - Physical Devices - iPhone X and Samsung S9

- Tablet Devices (Portrait and Landscape) - All available through Chrome and Firefox Dev Tools.
  - Additional Emulated Devices - Samsung Galaxy Tab 2, iPad Pro 9.7, iPad Pro 9.7, iPad mini, HTC Nexus 9
  - Physical Devices - iPad Air

- Laptop/Desktop Devices (Portrait and Landscape).
  - Emulated Screen Sizes - 1024 x 600, 1280 x 800, 1366 x 768, 1440 x 900, 1680 x 1050, 1920 x 1080
  - Physical Devices - 18" Laptop, 22" Monitor, 14" laptop


#### Overview

This website was intended to be responsive across all media devices such as mobile phones, tablets and desktops/laptops as the primary purpose of the website is to enable users to view and create recipes that others can see and users will want to be able to take their chosen media device with them to their kitchen.

To ensure the website and content remains responsive, I tested the layout at every stage of development on the various screen sizes and devices listed in the previous section. If the content did not display as intended, I corrected the styling of the elements and added Media Queries so that the design will adjust to device being viewed.

The overall site was designed using the Bootstrap Framework to make use of their flex layout. In addition to this I used relative measurements in my styling where possible, rather than absolute measurements to allow the elements to adapt to screen size changes before a new media query would need to be introduced.

##### Navbar

- I tested to ensure that the Navbar is correctly displayed at all times and the buttons within it responded and acted as intended.

##### Landing Page

- I tested that all writing, buttons and images on the landing page remained readable by the user and it adapted accordingly to the device it was being viewed on.

- Where the responsiveness of the website began to degrade, I created a media query to deal with any issues.

- In order to ensure that the site retained cross-browser responsiveness, I used the online CSS [Autoprefixer](https://autoprefixer.github.io/).

  - **Bug Identified** - Overlay Bar transition 

    - There was not small devices compativility on the transition of the pull-out bar

  - **Fix Applied**:

    - In order to correct this issue, I added   -webkit-transition: 0.5s; -o-transition: 0.5s;  transition: 0.5s; to the ovelay.

- In the search bar.

    - **Bug Identified** - Inline flex for small screen.
    - **Fix Applied** - I added 2 new lines in css :
        -   display: -webkit-inline-box and  display: -ms-inline-flexbox

##### Search Results Page

- I tested to ensure that the results shown in the search results page are displayed correctly to the user and that they kept a consistent flow between different media devices.

- No issues were discovered.

##### Recipe Page

- I tested to ensure that the results shown in the search results page are displayed correctly to the user and that they kept a consistent flow between different media devices.

- No issues were discovered.

##### Add Recipe Page

- I tested to ensure that the form content displayed and adjusted appropriately to the user and the media screen size they were viewing the page on.

- I tested to ensure that all validation messages remained clear to the user at all times.

- I test to ensure the buttons used within the page were clear to the user and that it conveyed its purpose.

- No issues were discovered.

##### Manage Recipe Page

- I tested to ensure that the form content displayed and adjusted appropriately to the user and the media screen size they were viewing the page on.

- I tested to ensure that all validation messages remained clear to the user at all times.

- I test to ensure the buttons used within the page were clear to the user and that it conveyed its purpose.

- I tested to ensure that the modal used for confirming the deletion of the recipe displayed correctly to the user and appeared correctly on all media screen sizes.

- No issues were discovered.


##### 404 Page

- I tested to ensure that the text content and image displayed and adjusted appropriately to the user and the media screen size they were viewing the page on.

##### 500 Page

- I was not able to test this page.

### Functionality Testing

At all instances within the below testing summaries, I ensured that the correct information was displayed within the jinja ``{% block TAG_NAME %}`` tags.

#### Base Template

I performed various tests to ensure that the conditional statements used within the base template are working as intended.

I manually tested every link works as intended and directs the user to the relevant page.

##### Breakdown of Jinja Functionality in Base Template

- Navbar Options:

  - Within the base template, there are two conditional statements used to show a user various option:

    - A user should be able to see the options for ``Home`` and ``Add Recipe``.

      - I tested that this conditional statement works as intended by verifying that the options shown are working as intended and the link takes you to the pages.

      - No issues were found with this functionality.

##### Breakdown of CSS Functionality in Base Template

- Flip card functionality:

  - I verified that the CSS functionality of ``flip-card-inner`` to the cards when the mouse hovers over it and shows the descriptiton and flip it back to the image once the mouse leaves.

  - No issues were discovered with this functionality.

##### Base Template - Breakdown of Views Used

**Associated View - Route: ``/search`` Function: ``get_search()``**

Breakdown of ``get_search()`` functionality:

- This takes the input from the search form and then redirects the user to the search results page view by passing in the forms input value as a variable argument:

    ```Python
    search_term=request.form.get("search_field")
    ```

- No issues were discovered with the functionality of this view

#### Landing Page Template

I performed various tests to ensure that the conditional statements used within the ``initial.html`` template are working as intended and that all associated ``views`` and ``jQuery`` functionalities work.

I manually tested every link works as intended and directs the user to the relevant page.

##### Breakdown of jQuery Functionality in Landing Page Template

- I resize the screen to different devices using the chrome developers’ tool and verify the burger icon will show up and the nav icons will be hiden.

- I verify that on click the burger icon on the top left coner and ``50%``  wide and screen height tall would how up and the links within will work and take you to the relevant page.

- No issues were discovered with this functionality.

##### Landing Page - Breakdown of Views Used

**Associated View - Route: ``/`` Function: ``get_recipes()``**

Breakdown of ``get_recipes()`` functionality:

    - I verified that all the recipes within the database are shown and all the details and images are being display within the recipe cards.

    - No issues were discovered with this functionality.

**Search Bar Functionality**

  - I manually tested that the search bar functionality works as intended.

    - I input different values where i knew the search will produce positive results.

    - I input values where I knew there will be no results and it will display a ``Sorry, no results were found`` message.

    - **Bug Identified** - Error 404 page.
        When the field is empty It can cause a 404-error message.
    - **Fix Applied** -
        Added a "**required**" in the input form.

**Associated View - Route: ``/search`` Function: ``get_search()``**

- Breakdown of ``get_search()`` functionality:

  - This takes the input from the search form and then redirects the user to the search results page view by passing in the forms input value as a variable argument:

    ```Python
    search_term=request.form.get("search_field")
    ```

- No issues were discovered with the functionality of this view


#### Recipe Page Template

I verified that the recipe page displays the correct recipe information as expected and that all buttons work as intended.

I manually tested every link works as intended and directs the user to the relevant page.

##### Breakdown of Jinja Functionality in Recipe Page Template

- Recipe Information:

  - I verified that the information is correctly inputted into the recipe document, including the number of steps and ingredients, as per the recipe document in the database.

    - No issues were discovered.

##### Breakdown of jQuery Functionality in Recipe Page Template

 
- I resize the screen to different devices using the chrome developers’ tool and verify the burger icon will show up and the nav icons will be hiden.

- I verify that on click the burger icon on the top left coner and ``50%``  wide and screen height tall would how up and the links within will work and take you to the relevant page.

- No issues were discovered with this functionality.

##### Recipe Page - Breakdown of Views Used

**Associated View - Route: ``/recipe/<recipe_id>`` Function: ``get_recipe(recipe_id)``**

Breakdown of ``get_recipe(recipe_id)`` functionality:

This view generates the recipe page for the intended recipe.

- It runs a query on the database to find the queried recipe based on its ``recipe_id`` and then returns the found recipe which is based into the recipe template.

  - No issues were discovered with this query functionality and the correct information was returned.

#### Add Recipe Page Template

I verified that the add recipe page displays as expected and that all buttons work as intended.

##### Breakdown of Jinja Functionality in Add Recipe Page Template

No additional Jinja statements were used within the creation of this page outside of the required block tags.

I verified that all HTML input elements with required tags and patterns worked as intended.

I added at the ``endblock`` another block so it complies with best practices on where the scipts goes:
```Jinja
{% block script %}
<script src="{{ url_for('static', filename='js/add-recipe.js')}}"></script>
{% endblock %}
```

##### Breakdown of jQuery Functionality in Add Recipe Page Template

- Remaining Character Length - Recipe Name & Recipe Description

  - I verified that the function that updates the HTML text for both the Recipe Name & Recipe Description remaining characters works as intended and that the remaining characters are displayed to the user.

  - I verified that when the max character count is reached that the HTML text turns red for that field.

- Adding / Removing Input Fields for Steps and Ingredient:

  - I verified that when a user presses the "+" or "-" under the relevant ingredient or step input that it adds or removes a field input.
  
    - When an input was added, I made sure that the input element was correct and had the necessary attributes.

    - When an input was removed, I made sure that it was the last child input that was removed.
 

##### Add Recipe Page - Breakdown of Views Used

**Associated View - Route: ``/create_recipe`` Function: ``add_recipe()``**

Breakdown of ``add_recipe()`` functionality:

- Inserting Form Information into the Database:

  - When the form information has been validated and submitted to the backend, the fields from the form are assigned to variables which can be used to create a new document that is inserted into the database.

    - Two helper functions are used for the steps and ingredient fields as these can be dynamic according to what the user has inputted.

      - The helper functions are [**Recipe Steps**](#recipe-steps) and [**Recipe Ingredients**](#recipe-ingredients).

    - The link requests an external image which is store as a ``string``. If the user doesn't input any link when a generic image will be assigned by using:
    ```Python
    if image == "":
            image = "static/images/generic_logo.png"
    ```

    - I verified that all the information submitted from the form correctly gets uploaded to the database and no errors were found.

#### Manage Recipe Page Template

I verified that the manage recipe page displays as expected and that all buttons work as intended.

##### Breakdown of Jinja Functionality in Manage Recipe Page Template

- I verified that the current recipe information was correctly populated within the form, so the user was able to see their previous information and update it where required.

- I verified that all the validation elements within the form worked as expected.

##### Breakdown of jQuery Functionality in Manage Recipe Page Template

- Remaining Character Length - Recipe Name & Recipe Description

  - I verified that the function that updates the HTML text for both the Recipe Name & Recipe Description remaining characters works as intended and that the remaining characters are displayed to the user.

  - I verified that when the max character count is reached that the HTML text turns red for that field.

- Adding / Removing Input Fields for Steps and Ingredient:

  - I verified that when a user presses the "+" or "-" under the relevant ingredient or step input that it adds or removes a field input.
  
    - When an input was added, I made sure that the input element was correct and had the necessary attributes.

    - When an input was removed, I made sure that it was the last child input that was removed.
  

##### Manage Recipe Page - Breakdown of Views Used

**Associated View - Route: ``/edit_/<recipe_id>`` Function: ``edit_recipe(recipe_id)``**

Breakdown of ``edit_recipe(recipe_id)`` functionality:

- Querying Recipe Details

  - A Query is run to obtain the details of the recipe that has been sent along to the route and this information is assigned to a variable ``recipe_id`` which is then passed to the passed into the template ``edit_recipe.html`` to show the recipe information for the user.

**Associated View - Route: ``/update/<recipe_id>`` Function: ``update_recipe(recipe_id)``**

Breakdown of ``update_recipe(recipe_id)`` functionality:

- Inserting Form Information into the Database:

  - When the form information has been validated and submitted to the backend, the fields from the form are assigned to variables which can be used to update the document into the database.

    - Two helper functions are used for the steps and ingredient fields as these can be dynamic according to what the user has inputted.

      - The helper functions are [**Recipe Steps**](#recipe-steps) and [**Recipe Ingredients**](#recipe-ingredients).

    - The link requests an external image which is store as a ``string``. If the user doesn't input any link when a generic image will be assigned by using:
    ```Python
    if image == "":
            image = "static/images/generic_logo.png"
    ```

    - I verified that all the information submitted from the form correctly gets uploaded to the database and no errors were found.

**Associated View - Route: ``/delete/<recipe_id>`` Function: ``delete_recipe(recipe_id)``**

Breakdown of ``delete_recipe(recipe_id)`` functionality:

- Querying Recipe Details

  - A Query is run to obtain the details of the recipe unique id which is then used to delete the recipe.
    
    - I verified that this functionality works as intended, the recipe is removed from the database.
  

#### 404 Page Template

I verified that the custom 404 page correctly generates and is displayed to the user when they access a view that does not exist. I test by removing the ``required`` vaule in the search bar.


##### Recipe Steps

The ``recipe_steps()`` function takes one argument:

- req - This is request.form.

This function is then assigned to the relevant variable ``steps_list`` the value of the list.

The function then iterates over the request.form, looks for the key ``step`` then appends the value to the ``steps_list`` variable.

I have verified that this function correctly and assigns all the steps to the right variable creating an array which is then used by the relevant view.

##### Recipe Ingredients

The ``recipe_ingredients()`` function takes one argument:

- req - This is request.form.

This function is then assigned to the relevant variable ``ingredients_list`` the value of the list.

The function then iterates over the request.form, looks for the key ``ingredients`` then appends the value to the ``ingredients_list`` variable.

I have verified that this function correctly and assigns all the ingredients to the right variable creating an array which is then used by the relevant view.

##### pylint

I use this tool at the CLI to verify and make the code compliant.

##### Lighthouse Chrome developer tools

I use this function to generate a report on the test on the different pages.

[Screenshot](https://raw.githubusercontent.com/Dhracko/frankies_kitchen/master/static/image/Screenshot_lighthouse.png)

[Screenshot](https://raw.githubusercontent.com/Dhracko/frankies_kitchen/master/static/image/Screenshot_mobile.png)


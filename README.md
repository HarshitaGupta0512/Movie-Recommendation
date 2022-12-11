

**Overview:**

Recommender systems aim to predict users' interests and recommend product items that quite likely are interesting for them. They are among the most powerful machine learning systems. Recommendation systems play a vital role in the industry, according to a fact NETFLIX increases its economy by 70% using the recommendation system built. When the movies are displayed as per the user’s taste the person feel known on the website and is not lost in the cluster.

Recommender systems function with two kinds of information:

-   *Characteristic information*. This is information about items (keywords, categories, etc.) and users (preferences, profiles, etc.).
-   *User-item interactions.* This is information such as ratings, number of purchases, likes, etc.

Based on this, we can distinguish between three algorithms used in recommender systems:

-   *Content-based* systems, which use characteristic information.
-   *Collaborative filtering* systems, which are based on user-item interactions.
-   *Hybrid systems*, which combine both types of information

**Movie Box** is one such recommendation system built aims to provide the recommendations to user using the characteristics of the movie he /she searches or clicks or give the rating.


> ```
> LOGIN THROUGH **EMAIL AND PASSWORD**:
> Username:harshita
> Email:harshita@gmail.com
> password:harshita
> ```

<!--  Video Link: https://drive.google.com/file/d/1rBTYlnOfKFmisIjy8UsqPYyQxGSQ96Ay/view?usp=sharing -->

**Algorithms used in my project**

*Content Based Recommendation System is used in the project focussing on two main algorithms: Count Vectorization and Cosine Similarity.* The details of the movies (title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB, <https://www.themoviedb.org/documentation/api>.


INTERFACES:

![WhatsApp Image 2022-05-28 at 5 22 17 PM](https://user-images.githubusercontent.com/98079342/170842246-5937a908-702c-476e-ab2b-9bb13bb14a4b.jpeg)

Clean User Interface with a simple Intuitive UI directing the new user to signup and old user to login using the signup and login buttons respectively. Get Started will redirect to signup page.

![WhatsApp Image 2022-05-28 at 5 26 36 PM](https://user-images.githubusercontent.com/98079342/170842386-e0bc8394-41ab-41d1-91ee-ef6a9657ab03.jpeg)
![WhatsApp Image 2022-05-28 at 5 27 26 PM](https://user-images.githubusercontent.com/98079342/170842392-704e9d7e-ca96-40e9-9b9e-05e8d22bbb7f.jpeg)

Authentication built using firebase database

![WhatsApp Image 2022-05-28 at 5 28 24 PM](https://user-images.githubusercontent.com/98079342/170842407-2032916b-4c67-40bb-ae7e-3f18b5e06662.jpeg)

**HOME PAGE**

After user is logged in Home Page appears which shows some of the trending hits of the database which have been calculated using 2 factors- past user ratings of the dataset along with number of users who rated a movie (WEIGHTED MEAN AVERAGE)

![WhatsApp Image 2022-05-28 at 5 38 26 PM](https://user-images.githubusercontent.com/98079342/170843308-a7028deb-bb8d-4700-9488-e298c6c0cf4f.jpeg)

**CATEGORIES PAGE**

Categories showing genre of movie. User can click any genre to get the respective popular movies of that genre from the dataset

![WhatsApp Image 2022-05-28 at 5 41 07 PM](https://user-images.githubusercontent.com/98079342/170843309-0611f8c3-2fd0-4630-9919-94d7914e1e1c.jpeg)

Example:   
This page shows popular Romantic Hits when user clicks Romantic card on categories page.

![WhatsApp Image 2022-05-28 at 5 46 34 PM (1)](https://user-images.githubusercontent.com/98079342/170843314-791a5d1b-7c6c-423e-86e4-162d67db0eba.jpeg)

**MOVIE PAGE**

This Page shows information about the movie user search/clicks that is fetched from IMDB and TMDB along with some recommended movies which are based upon the machine learning algorithms related to movie shown above.

 ![WhatsApp Image 2022-05-28 at 5 53 02 PM](https://user-images.githubusercontent.com/98079342/170843687-2e58f975-5529-4486-9308-a7bf2e4d7432.jpeg)
 
 **Rate (GENRE) Page**

Rate (GENRE) will take you to the above page where you can rate genres from 1 to 5 based upon your interest, finally a list will be shown to you based on your choices filled.

![WhatsApp Image 2022-05-28 at 5 53 36 PM](https://user-images.githubusercontent.com/98079342/170843694-c7d2017c-6a91-4592-82c3-e778731793dd.jpeg)

The List of Recommended Movies

**FEATURES:**

![WhatsApp Image 2022-05-28 at 6 13 12 PM](https://user-images.githubusercontent.com/98079342/170843708-b1b71ff0-8f95-4181-a617-a1b78d37d920.jpeg)

**Click me will redirect user to page where   
it will show information about the user0  
 along with its recommended movies.**

![WhatsApp Image 2022-05-28 at 6 04 00 PM (1)](https://user-images.githubusercontent.com/98079342/170843767-149121e6-9922-42e1-ac0c-9b239a73313f.jpeg)

**Top Button redirects to top of the page**


![WhatsApp Image 2022-05-28 at 6 00 21 PM](https://user-images.githubusercontent.com/98079342/170843772-634a765c-2a07-4959-87ee-6a96c529786f.jpeg)

**Auto Complete Search Box**

![WhatsApp Image 2022-05-28 at 6 01 54 PM](https://user-images.githubusercontent.com/98079342/170843777-7604bc0e-7c7f-4e13-aab7-7b5b23dea7cc.jpeg)

**Shortcut to access the search box without clicking-CTRL+B**

![WhatsApp Image 2022-05-28 at 6 10 17 PM](https://user-images.githubusercontent.com/98079342/170843782-fa7ee572-82e7-4253-8b8d-42739c9dd7b7.jpeg)


**User can click the button to watch movie’s trailer if available on YouTube.**

![WhatsApp Image 2022-05-28 at 6 04 26 PM](https://user-images.githubusercontent.com/98079342/170843786-7100219f-5f42-46a5-b70c-36267f1c42ab.jpeg)
![WhatsApp Image 2022-05-28 at 6 04 59 PM](https://user-images.githubusercontent.com/98079342/170843789-7f9da027-cefb-4316-8fc3-157fd4b5ec64.jpeg)


**Light/Dark mode**

**TECHNOLOGIES USED**

**LANGUAGES** - HTML, CSS, JS, BOOTSTRAP, PYTHON, JQUERY

**FRAMEWORK** - FLASK

**VERSION CONTROL** - GIT

**HOSTING –** HEROKU

| **SPRINT (WEEK DISTRIBUTION)** | **FEATURES IMPLEMENTED AND WORK DONE**                                                                                                                                                                                                                                                                                                                     |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WEEK 1 (4 MAY-10 MAY)**      | Explored the 3 interesting challenges given to us and decided upon to go with algorithms challenge. Started Building Machine Learning Model by learning about the different techniques like content based, collaborative, svd algorithms etc sticking to count vectorizer, cosine similarity and framed the rough idea of the functional prototype design. |
| **WEEK 2 (11MAY-17 MAY)**      | Built a simple UI based website with minimal features like search bar, adding authentication using firebase integrating the ML model by flask framework.                                                                                                                                                                                                   |
| **WEEK 3 (18TH MAY-24MAY)**    | Worked on rest of the features like light/dark mode, incorporating trailer of movies, implementing shortcuts for easy access building form to take user input for recommendations and removed bugs of integration along with changes in the UI.                                                                                                            |
| **WEEK 4 (25MAY-29MAY)**       | Manually tested the features, removed bugs and hosted the webapp on Heroku.                                                                                                                                                                                                                                                                                |

**INSTALLATION COMMAND**

1-Clone or download this repository to your local machine

2-Install all the libraries mentioned in the [requirements.txt](https://github.com/kishan0725/Movie-Recommendation-System-with-Sentiment-Analysis/blob/master/requirements.txt) file with the command pip install -r requirements.txt

3-Open the terminal/command prompt from project directory and run the file main.py by executing the command python main.py.

4-Go to the browser and type http://127.0.0.1:5000/ in the address bar

**LEARNING OUTCOMES**

1- Understood the process of taking an idea to a finished project under a timeline.

2- Explored the domain of Machine Learning and various algorithms, methods and fundamental topics.

3- Got to know how big and interesting the world of recommendation systems is as well as importance of data set in a machine learning project.

4- Worked with frontend languages and technologies and built something that’s interactive, learnt use of HTML, CSS, Bootstrap and JavaScript.

5- Learnt Python to built the models inside Jupiter Notebook and got familiar with the environment.

6- Understood use of JQuery and Flask framework and the hard job of integrating the model with the webapp.

7- Touched on the topic of good UI/UX practices and added features such as auto completion on search etc.

8- Worked with Git Version Control and used hosting services.

**FUTURE SCOPE**

1)Adding Favourites button where user can click on it and the respected movie will get added to the Favourites.

2)Making the website Dynamic-Adding the new movies releasing every time.

3) Using the Hybrid Approach for recommendations.

4) Providing the feature for the user to know which movie is available on which platform like prime, Netflix etc and writing Reviews.

**THANKYOU**

**BY-HARSHITA GUPTA**

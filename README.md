**Microsoft Engage Mentorship program'22 project**

**Overview:**

Recommender systems aim to predict users' interests and recommend product items that quite likely are interesting for them. They are among the most powerful machine learning systems. Recommendation systems play a vital role in the industry, according to a fact NETFLIX increases its economy by 70% using the recommendation system built. When the movies are displayed as per the user’s taste the person feel known on the website and is not lost in the cluster.

Recommender systems function with two kinds of information:

-   *Characteristic information*. This is information about items (keywords, categories, etc.) and users (preferences, profiles, etc.).
-   *User-item interactions.* This is information such as ratings, number of purchases, likes, etc.

Based on this, we can distinguish between three algorithms used in recommender systems:

-   *Content-based* systems, which use characteristic information.
-   *Collaborative filtering* systems, which are based on user-item interactions.
-   *Hybrid systems*, which combine both types of information

**Movie Box** is one such recommendation system built in the 4 weeks mentorship journey aiming to provide the recommendations to user using the characteristics of the movie he /she searches or clicks or give the rating

**Algorithms used in my project**

*Content Based Recommendation System is used in the project focussing on two main algorithms: Count Vectorization and Cosine Similarity.* The details of the movies (title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB, <https://www.themoviedb.org/documentation/api>.

**![](media/0814e2a59fe2c6cd4675c55a796704f7.jpeg)INTERFACES:**

Clean User Interface with a simple Intuitive UI directing the new user to signup and old user to login using the signup and login buttons respectively. Get Started will redirect to signup page.

![](media/90748a7963152cde2afcacc90d03f4ce.jpeg)![](media/63f0021fcc1801e673c8ce71064b26a8.jpeg)

Authentication built using firebase database

**![](media/53c2cba2dedee35f9819e003480748cb.jpeg)**

**HOME PAGE**

After user is logged in Home Page appears which shows some of the trending hits of the database which have been calculated using 2 factors- past user ratings of the dataset along with number of users who rated a movie (WEIGHTED MEAN AVERAGE)

**![](media/b86b6e68602c084a4a106739ee22d709.jpeg)CATEGORIES PAGE**

Categories showing genre of movie. User can click any genre to get the respective popular movies of that genre from the dataset

![](media/c11f25ade9f7892b068f6a8526a6f2fd.jpeg)

Example:   
This page shows popular Romantic Hits when user clicks Romantic card on categories page.

![](media/a0a2e6279b3576fd90d55098c1afde56.jpeg)

**MOVIE PAGE**

This Page shows information about the movie user search/clicks that is fetched from IMDB and TMDB along with some recommended movies which are based upon the machine learning algorithms related to movie shown above.

**Rate (GENRE) ![](media/56dfeeb6a61c938a660ac2ee275a21f4.jpeg)PAGE**

Rate (GENRE) will take you to the above page where you can rate genres from 1 to 5 based upon your interest, finally a list will be shown to you based on your choices filled.

![](media/ad00da85fcbc662b0d9d682e53952200.jpeg)

The List of Recommended Movies

![](media/4a208114d404e29bba505a65d345a747.jpeg)![](media/682a14158b82eb35e42b03c1fcd74469.jpeg)**FEATURES:**

Click me will redirect user to page where   
it will show information about the user0  
 along with its recommended movies.

Auto Complete Search Box

![](media/b196d064900fbd8810406099cb787deb.jpeg)

![](media/5a7d5610fa50a6d334abe25f285f495d.jpeg)Shortcut to access the search box without clicking-CTRL+B

![](media/8ab797dad31870e57580838fa5f95c32.jpeg)

User can click the button to watch movie’s trailer if available on YouTube.

![](media/23e1741adc64583aa32d96b89e212d0b.jpeg) ![](media/c2721a7a5601610732ab6e41b99c10c1.jpeg)

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

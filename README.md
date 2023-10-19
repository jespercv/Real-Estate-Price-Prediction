## Real Estate Property Prediction

Real estate is a term that refers to the physical land, structures, and resources attached to it. According to a 2022 survey, about 60%  of households in the Philippines occupied housing units and lots they owned. On the other hand, 9.5 percent of Filipino families were renting a house or room, including a lot. And there are about 4.5 million homeless people in the Philippines of a population of about 106 million, 

I became interested in this data science project since many Filipinos suffer from homelessness, rental neglect, and other issues. As an engineer and data scientist/analyst, I was motivated to perform this type of research to learn about the situation of my fellow Filipinos who are suffering from inflation and, perhaps, what I can do in the future as a data scientist/analyst to make a difference in this uncertain world.


**Step by Step**
1. We will initially perform an exploratory data analysis on the Kaggle.com dataset.
2. To guarantee that the dataset is ready for modeling, we will also employ Data Cleaning, Outlier identification, and Feature Engineering.
3. Creating the model. But first, let's identify the problem, which is regression where we will forecast the price, thus we will use random forest regressor and gridsearchcv for hyperparameter tweaking to see if there is a better model for the dataset.
4. The next step would be to create a python flask server that serves http requests using the stored model. The third component is a website developed in html, CSS, and javascript that allows users to enter information such as home square footage, bedrooms, and so on, and then calls a Python Flask server to receive the anticipated price.
[![Python Application Test with Github Actions](https://github.com/lilah-duboff/lilah_duboff_miniproj9/actions/workflows/main.yml/badge.svg)](https://github.com/lilah-duboff/lilah_duboff_miniproj9/actions/workflows/main.yml)

![alt text](tests_passed.png)

# Mini-Project 9: Cloud-Hosted Notebook Data Manipulation
---
##### The purpose of this project is to build a cloud-hosted notebook using Google Colab, generate a simple data exploration and analysis using a dataset, and return a project in a GitHub repo that contains a CI/CD pipeline and functioning tests. In this project, we will be exploring and analyzing a free Kaggle dataset the contains information about the average hourly wages for different levels of education, over a span of 50 years (1973-2022). The data is then further broken down by sex and race, allowing for demographics comparison of average pay by education level. The analyses provided compare the average hourly wage based on education level, for 2022 and 1973 (the limits of the dataset), and continue to show the differences in average hourly wages between all men and women who have earned a bachelors or advanced degree.
---
### Requirements
- [x] Set up a cloud-hosted Jupyter Notebook (e.g., Google Colab)
- [x] Perform data manipulation tasks on a sample dataset
- [x] Setup and configuration (20 points)
- [x] Data manipulation tasks (20 points)
- [x] CI/CD pipeline (10 points)
- [x] Link to the cloud-hosted notebook
- [x] Document or video demonstrating the tasks performed

---
### File Structure
- Project Folder
    - .devcontainer
        - devcontainer.json
        - Dockerfile
    - .github
        - main.yml
    - data
        - wages_by_education.csv
    - python files
        - outputs
            - wages_men.jpg
            - wages_women.jpg
        - tests
            - test_lib.py
            - test_main.py
        - lib.py
        - main.py
    - Makefile
    - Mini9_Data_Analysis.ipynb (linked to Google Colab)
    - README.md
    - requirements.txt
---
### Data Cleaning and Exploration
##### To begin, we imported our dependencies, and used pandas to load the url into a dataframe. We ensured that it succeeded by running a few assert statements. Next, we checked to see our column names, and if there were any null or missing numbers in the data. By running data.head() and data.tail(), we were able to see the first and last five rows of the dataframe. We confirmed that the first year was 1973, and the last (most recent year) was 2022. We also created a list of our column titles, and saw that the dataframe contained information about: wages by education level, wages by education level and sex, and wages by education level, sex, and race. Finally, we checked to see if there were any null or missing values in the data. 

##### We established that there were no missing values in this dataset, and continued to the data exploration and analysis. The purpose of the data exploration was to generate summary statistics, including the mean, standard deviation, count, and IQR of some sample columns.
---
### Data Analysis
##### During the data analysis section, we created a number of plots in the cloud notebook, that provided information about the differences in hourly wages by year, by gender, by education level, and by race. The full analysis can be read in the Mini9_Data_Analysis notebook, but below I will show some sample plots and the results found. 

#### Average Hourly Wage for Men, by Education Level
![alt text](python_files/outputs/wages_men.png)
##### This plot depicts the average hourly wages separated by education level for men in the US. Men who hold advanced degrees earn the highest hourly wage among all education levels, and men who did not complete high school earn the least hourly wage. In around 1980, pay began to steadily increase over time for people who held either a bachelors or a masters degree, while the average pay for those with some college experience or less remained around the same amount.


#### Average Hourly Wage for Women, by Education Level
![alt text](python_files/outputs/wages_women.png)
##### This plot depicts the average hourly wages separated by education level for women in the US. Similar to the men's plot, women who hold advanced degrees earn the highest hourly wage among all education levels, and women who did not complete high school earn the least hourly wage. Compared to the mens' plot however, the range of specific pay values appears to be less for women - men who hold advanced degrees earned over $60/hr in 2022, while women with equivalent degrees earned just over $45/hr.

---
### Conclusions about the Analysis and Recommendations
##### Based on these sample plots, we are able to see how much of a difference there is in average hourly wages between men and women who hold equivalent degrees, over a span of 50 years. This data shows us that the wage gap problem is not new, and in fact has continued to worsen over the past 50 years. This analysis can help influence further research on the wage gap, and hopefully inform policies aimed at reducing the gap. 
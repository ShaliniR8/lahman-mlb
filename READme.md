# MLB
- *baseballdatabank_2022.zip* is the original dataset we worked from. 
- *EDA notebooks* folder contains notebooks that show the steps of our EDA. 
- *combined_features.ipynb* is a notebook going through some basic EDA, the feature generation process, cleaning and preprocessing steps, and XGboost regression model along with it's results. 
- *b_features.csv*, *p_features.csv*, and *t_features.csv* are respectively the preprocessed and engineered batting features, pitching features, and team features we generated from combined_features.ipynb. We combined these into a single file *features.csv*
- *features.csv* and *targets.csv* contain the preprocessed data we trained our models with. 
- *Models.ipynb* contains the rest of our models. 



The problem that we plan to explore involves predicting win likelihood in baseball. To do so, we plan to use data from the Lahman dataset which provides data on player and team performance since the 1800s. This problem is fairly broad and can therefore be approached from a few different angles. For instance, we could attempt to predict which of two teams is likely to win in any given matchup. In another case, we could extrapolate team data in an effort to predict the chances each team has of securing a spot in the playoffs. Going further, we could attempt to predict the winner of the World Series outright. This problem has the potential to make a substantial impact within the domain of baseball. In particular, this could result in a better understanding of which elements of a team (e.g. pitching, outfield, offense, etc.) contribute more to win likelihood, which could provide valuable insight for franchise owners trying to build winning teams with limited resources. This analysis will likely require a breakdown between team and player performance, as well as a granular understanding of the impact of defense, offense, and pitching.


Features: 

- Pitcher age, batter age
- Rolling winning percentage
- Median OPS, Median ERA
- Pythagorean Win Percentage ( exp = 1.83, 2.85 )
- Caught Stealing Percentage
- Batting Average ( BA )

### EDA

![](https://github.com/ShaliniR8/lahman-mlb/blob/main/images/fig1.jpg?raw=true)
![](https://github.com/ShaliniR8/lahman-mlb/blob/main/images/fig2.jpg?raw=true)
![](https://github.com/ShaliniR8/lahman-mlb/blob/main/images/fig3.jpg?raw=true)
![](https://github.com/ShaliniR8/lahman-mlb/blob/main/images/fig4.jpg?raw=true)
![](https://github.com/ShaliniR8/lahman-mlb/blob/main/images/fig5.jpg?raw=true)

-- Constructed Features 
![](https://github.com/ShaliniR8/lahman-mlb/blob/main/images/fig6.png?raw=true)

### XGBoostRegressor Test result visualizations and shap plots

![](https://github.com/ShaliniR8/lahman-mlb/blob/main/images/fig7.png?raw=true)
![](https://github.com/ShaliniR8/lahman-mlb/blob/main/images/fig8.png?raw=true)
![](https://github.com/ShaliniR8/lahman-mlb/blob/main/images/fig9.png?raw=true)
![](https://github.com/ShaliniR8/lahman-mlb/blob/main/images/fig10.png?raw=true)
![](https://github.com/ShaliniR8/lahman-mlb/blob/main/images/fig11.png?raw=true)
![](https://github.com/ShaliniR8/lahman-mlb/blob/main/images/fig12.png?raw=true)

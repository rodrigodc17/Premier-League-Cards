#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from pandas import DataFrame, Series


# In[2]:


# Quick Look into our Data Frame
data = pd.read_csv('C:/Users/rodri/Downloads/events_premier-league_2022-23.csv')
data.tail(10)


# In[3]:


data.info()


# In[4]:


# function to identify yellow cards number
def is_card(x):
    if x == "Yellow card":
        return 1
data['is_yellow_card'] = data['event_type'].apply(is_card)    
data.head(10)


# In[5]:


cards_analysis = DataFrame(data.groupby('team').is_yellow_card.count())
cards_analysis.head()
cards_analysis.sort_values('is_yellow_card',ascending=False)


# We can see that Man Utd has the largest amount of Yellow Cards in the league

# In[6]:


import matplotlib.pyplot as plt
time_sheet = DataFrame(data.groupby('event_time').is_yellow_card.count())
time_sheet.plot()
plt.xlabel('Match Time')
plt.ylabel('Card Numbers')


# Cards distribution per time -> one can observe that there is a high concentration of cards in the final moments of a match

# In[7]:


# total yellow cards numbers in the season
time_sheet.sum()


# In[8]:


player_analysis = DataFrame(data.groupby('action_player_1').is_yellow_card.sum())
player_analysis.sort_values('is_yellow_card',ascending=False)


# 7 is the number of max yellow cards a player has in the season yet

# In[9]:


player_analysis[player_analysis.is_yellow_card == player_analysis.is_yellow_card.max()]


# These are the players with the most yellow cards in the league

# In[10]:


player_analysis[player_analysis.is_yellow_card == player_analysis.is_yellow_card.min()]


# As you can see, several players did not even receive a yellow card!

# In[11]:


len(player_analysis[player_analysis.is_yellow_card == player_analysis.is_yellow_card.min()])


# 165, to be more exact

# Let's see if is there some relation between the team playing home or away and it's yellow cards numbers

# In[12]:


teams_analysis = data[['team','event_team','event_time','event_type']]
teams_analysis.head(5)


# In[13]:


# Let's create a aux column to identify yellow cards in home teams
def yellow_for_home(x):
    if x == "Yellow card":
        return 1
    else:
        return 0
teams_analysis['is_yellow_card'] = teams_analysis['event_type'].apply(yellow_for_home)
teams_analysis.head(3)


# In[14]:


# Now let's check cards according to where the event team was playing
cards_per_team = DataFrame(teams_analysis.groupby('event_team').is_yellow_card.sum())
cards_per_team
cards_per_team.plot.pie(y='is_yellow_card', figsize=(5, 5))


# Apparently, visiting teams have a higher tendency to receive yellow cards

# In[15]:


teams_analysis.groupby('event_team').is_yellow_card.mean()


# In[16]:


home_teams = teams_analysis.loc[teams_analysis['event_team']=='home' ]
home_teams.head()
#home_teams.groupby('event_time').is_yellow_card.sum()


# In[17]:


DataFrame(home_teams.groupby('event_time').is_yellow_card.count()).sort_values('is_yellow_card',ascending = False)


# In[18]:


home_teams.hist(column='event_time',bins=70)


# Data shows that most of the cards for home teams occurs after 80 minutes of the match

# In[19]:


# Now let's repeat the analysis for away playing teams


# In[20]:


away_teams = teams_analysis.loc[teams_analysis['event_team']=='away']
away_teams.tail(5)


# In[21]:


del away_teams['event_type']


# In[29]:


away_teams.hist(column='event_time',bins=50,alpha=0.5,color='indianred')
home_teams.hist(column='event_time',bins=50,alpha=0.5)


# In[80]:


import seaborn as sns


# In[ ]:





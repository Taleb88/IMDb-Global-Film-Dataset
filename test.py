import pandas as pd


# 2/23/2025 - TESTING IN PROGRESS
# creating charts via matplotlib
import matplotlib.pyplot as plt

fav_tv_shows_df = pd.read_csv('fav_tv_shows.csv')

for year in fav_tv_shows_df['startYear'].values:
    try:
        color = 'red'
        x = fav_tv_shows_df['primaryTitle']
        y = fav_tv_shows_df.loc[fav_tv_shows_df['startYear'] == year]
        plt.barh(x, y, color=color)
        plt.title(f'Favorit ')
        plt.yticks(fontsize=8)
        plt.xlabel('primaryTitle')
        plt.ylabel('startYear')
        plt.show()   
    except Exception as e:
        print(f'cannot create charts due to wrong year(s) - e - {type(e)}')

# ratings_df = pd.read_table('title.ratings.tsv')
# title_basics_df = pd.read_table('title.basics.tsv')
# title_crew_df = pd.read_table('title.crew.tsv')

# ratings_df.to_csv('ratings.csv', index=False)
# title_basics_df.to_csv('title_basics.csv', index=False)
# title_crew_df.to_csv('title_crew.csv', index=False)

# print('\nratings_df:',ratings_df,'\n')
# print('title_basics_df:',title_basics_df,'\n')
# print('title_crew_df:',title_crew_df,'\n')

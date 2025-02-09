import pandas as pd

gfg_df = pd.read_csv('csv/GfG.csv', low_memory=False)

my_list = list(gfg_df.columns)
index = 0

for col_name in my_list:
    print(index, col_name)
    index +=1
# displaying unique values per column
print('\ntconst:\n',gfg_df['tconst'].unique(),'\n')
print('titleType:\n',gfg_df['titleType'].unique(),'\n')
print('primaryTitle:\n',gfg_df['primaryTitle'].unique(),'\n')
print('originalTitle:\n',gfg_df['originalTitle'].unique(),'\n')
print('isAdult:\n',gfg_df['isAdult'].unique(),'\n')
print('startYear:\n',gfg_df['startYear'].unique(),'\n')
print('endYear:\n',gfg_df['endYear'].unique(),'\n')
print('runtimeMinutes:\n',gfg_df['runtimeMinutes'].unique(),'\n')
print('genres:\n',gfg_df['genres'].unique(),'\n')

gfg_df['isAdult'] = gfg_df['isAdult'].replace("\\N",0).astype(int)

gfg_df.to_csv('GfG.csv', index=False)

def isAdult(x):
    try:
        if x == 0:
            return 'No'
        else:
            return 'Yes'
    except Exception as e:
        return f'cannot update values: {type(e)}'

gfg_df['isAdult'] = gfg_df.apply(lambda x: isAdult(x.iloc[4]), axis='columns')
gfg_df.to_csv('GfG.csv', index=False)
print('\nisAdult:',gfg_df['isAdult'].unique(),'\n')

gfg_df['startYear'] = gfg_df['startYear'].replace("\\N",0000).astype(int)
gfg_df.to_csv('GfG.csv', index=False)
gfg_df['endYear'] = gfg_df['endYear'].replace("\\N",0000).astype(int)
gfg_df.to_csv('GfG.csv', index=False)

print('\nstartYear:',gfg_df['startYear'].unique(),'\n')
print('\nendYear:',gfg_df['endYear'].unique(),'\n')

runtime_minutes_errors = ['\\N','Reality-TV','Talk-Show','Documentary','Family,Game-Show','Animation,Comedy,Family',
         'News,Talk-Show','Comedy,News,Talk-Show','Documentary,Reality-TV','Adult','Comedy,Drama,Fantasy',
         'Fantasy,Horror,Mystery','Action,Fantasy,Horror','Action,Horror,Mystery','Comedy,Drama,Horror',
         'Action,Adventure,Drama','Music','Drama,Fantasy,Horror','Game-Show,Reality-TV']

def runtimeMinutes(x):
    try:
        if x in runtime_minutes_errors:
            return '0'
        else:
            return f'{x}'
    except Exception as e:
        return f'error - cannot make proposed changes {type(e)}'
    
gfg_df['runtimeMinutes'] = gfg_df.apply(lambda x: runtimeMinutes(x.iloc[7]), axis='columns')
gfg_df.to_csv('GfG.csv', index=False)
gfg_df['runtimeMinutes'] = gfg_df['runtimeMinutes'].astype(int)
gfg_df.to_csv('GfG.csv', index=False)
print('runtimeMinutes updated:\n',gfg_df['runtimeMinutes'].unique(),'\n')
print('runTimeMinutes updated accordingly:\n',gfg_df)

gfg_df['genres'] = gfg_df['genres'].replace("\\N","TBD")
gfg_df.to_csv('GfG.csv', index=False)
print('genres updated:\n',gfg_df['genres'].unique(),'\n')

gfg_short_df = gfg_df.loc[gfg_df['titleType'] == 'short']
gfg_short_df.to_csv('gfg_short.csv', index=False)
print('short:\n',gfg_short_df,'\n')

gfg_movie_df = gfg_df.loc[gfg_df['titleType'] == 'movie']
gfg_movie_df.to_csv('gfg_movie.csv', index=False)
print('movie:\n',gfg_movie_df,'\n')

gfg_tv_short_df = gfg_df.loc[gfg_df['titleType'] == 'tvShort']
gfg_tv_short_df.to_csv('gfg_tv_short.csv', index=False)
print('tv_short:\n',gfg_tv_short_df,'\n')

gfg_tv_movie_df = gfg_df.loc[gfg_df['titleType'] == 'tvMovie']
gfg_tv_movie_df.to_csv('gfg_tv_movie.csv', index=False)
print('tv_movie\n',gfg_tv_movie_df,'\n')

gfg_tv_episode_df = gfg_df.loc[gfg_df['titleType'] == 'tvEpisode']
gfg_tv_episode_df.to_csv('gfg_tv_episode.csv', index=False)
print('tv_episode:\n',gfg_tv_episode_df,'\n')

gfg_tv_series_df = gfg_df.loc[gfg_df['titleType'] == 'tvSeries']
gfg_tv_series_df.to_csv('gfg_tv_series.csv', index=False)
print('tv_series:\n',gfg_tv_series_df,'\n')

gfg_tv_miniseries_df = gfg_df.loc[gfg_df['titleType'] == 'tvMiniSeries']
gfg_tv_miniseries_df.to_csv('gfg_tv_miniseries.csv', index=False)
print('tv_miniseries:\n',gfg_tv_miniseries_df,'\n')

gfg_tv_special_df = gfg_df.loc[gfg_df['titleType'] == 'tvSpecial']
gfg_tv_special_df.to_csv('gfg_tv_special.csv', index=False)
print('tv_special:\n',gfg_tv_special_df,'\n')

gfg_video_df = gfg_df.loc[gfg_df['titleType'] == 'video']
gfg_video_df.to_csv('gfg_video.csv', index=False)
print('video:\n',gfg_video_df,'\n')

gfg_videogame_df = gfg_df.loc[gfg_df['titleType'] == 'videoGame']
gfg_videogame_df.to_csv('gfg_videogame.csv', index=False)
print('videogame:\n',gfg_videogame_df,'\n')

gfg_tv_pilot_df = gfg_df.loc[gfg_df['titleType'] == 'tvPilot']
gfg_tv_pilot_df.to_csv('gfg_tv_pilot.csv', index=False)
print('tv_pilot:\n',gfg_tv_pilot_df,'\n')
#converted ratings_df into csv
ratings_df = pd.read_table('title.ratings.tsv', sep='\t', low_memory=False)
ratings_df.to_csv('ratings.csv', index=False)
print('ratings_df:\n',ratings_df,'\n')
# merging gfg_df and ratings_df into one df
gfg_ratings_merged_df = pd.merge(gfg_df, ratings_df, on='tconst')
gfg_ratings_merged_df = gfg_ratings_merged_df.sort_values(by='averageRating', ascending=False)
gfg_ratings_merged_df.to_csv('gfg_ratings_merged.csv', index=False)
print('gfg_ratings_merged_df:\n',gfg_ratings_merged_df.head(50),'\n')
# top 50 tv series; min of 50,000 votes
top_50_tv_series_df = \
    gfg_ratings_merged_df.loc[(gfg_ratings_merged_df['titleType'] == 'tvSeries') 
                              & (gfg_ratings_merged_df['numVotes'].astype(int) >= 100000)]
top_50_tv_series_df = top_50_tv_series_df.head(50)
top_50_tv_series_df.to_csv('top_50_tv_series.csv', index=False)
print('top_50_tv_series:\n',top_50_tv_series_df,'\n')

# creating charts via matplotlib
import matplotlib.pyplot as plt

color = 'blue'
x = top_50_tv_series_df['primaryTitle'].astype(str)
y = top_50_tv_series_df['averageRating']
plt.barh(x, y, color=color)
plt.title('Top 50 TV Series')
plt.yticks(fontsize=8)
plt.xlabel('Rating')
plt.show()

'''def movie_1980s(df):
    try:
        return df[(df['titleType'] == 'movie') &\
                  (df['startYear'] >= 1980) &\
                  (df['startYear'] <= 1989)]
    except Exception as e:
        return(f'cannot filter out rows not meeting criteria {type(e)}')

print('movies from the 1980s:\n',movie_1980s(gfg_df),'\n')'''

#===============================================================================================#
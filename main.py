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

# VALUE CORRECTIONS - MISCELLANEOUS
gfg_ratings_merged_df.loc[gfg_ratings_merged_df['primaryTitle'] == 'My Wife and Kids', 'startYear'] = 2001
gfg_ratings_merged_df.loc[gfg_ratings_merged_df['primaryTitle'] == 'New york Undercover', 'endYear'] = 1998
gfg_ratings_merged_df.loc[gfg_ratings_merged_df['primaryTitle'] == 'Saved by the Bell', 'endYear'] = 1993
gfg_ratings_merged_df.to_csv('gfg_ratings_merged.csv', index=False)

# top 50 tv series; min of 50,000 votes
top_50_tv_series_df = \
    gfg_ratings_merged_df.loc[(gfg_ratings_merged_df['titleType'] == 'tvSeries') 
                              & (gfg_ratings_merged_df['numVotes'].astype(int) >= 100000)]
top_50_tv_series_df = top_50_tv_series_df.head(50)
top_50_tv_series_df.to_csv('top_50_tv_series.csv', index=False)
print('top_50_tv_series:\n',top_50_tv_series_df,'\n')

# my favorite tv shows
def fav_tv_shows(df):
    try:
        return df[(df['titleType'] == 'tvSeries') &
            ((df['primaryTitle'] == 'New York Undercover') | 
            (df['primaryTitle'] == 'Martin') | 
            (df['primaryTitle'] == 'Living Single') | 
            (df['primaryTitle'] == "Hangin' with Mr. Cooper") | 
            (df['primaryTitle'] == 'In the Heat of the Night') | 
            (df['primaryTitle'] == 'The Simpsons') | 
            (df['primaryTitle'] == 'Roc') | 
            (df['primaryTitle'] == 'Boy Meets World') | 
            (df['primaryTitle'] == 'My Wife and Kids') | 
            (df['primaryTitle'] == 'Law & Order') |
            (df['primaryTitle'] == 'The Fresh Prince of Bel-Air') |
            (df['primaryTitle'] == 'Beverly Hills, 90210') |
            (df['primaryTitle'] == 'Married... with Children') |
            (df['primaryTitle'] == 'Malcolm & Eddie') |
            (df['primaryTitle'] == 'The Steve Harvey Show') |
            (df['primaryTitle'] == 'The Cosby Show') |
            (df['primaryTitle'] == 'The Ren & Stimpy Show') |
            (df['primaryTitle'] == '2 Stupid Dogs') |
            (df['primaryTitle'] == 'Eek! The Cat') |
            (df['primaryTitle'] == 'SpongeBob SquarePants') |
            (df['primaryTitle'] == 'Futurama') |
            (df['primaryTitle'] == 'King of the Hill') |
            (df['primaryTitle'] == 'Sister, Sister') |
            (df['primaryTitle'] == 'Boy Meets World') |
            (df['primaryTitle'] == 'Darkwing Duck') |
            (df['primaryTitle'] == 'Double Dragon') |
            (df['primaryTitle'] == 'King of the Hill') |
            (df['primaryTitle'] == 'My Brother and Me') |
            (df['primaryTitle'] == 'In the House') |
            (df['primaryTitle'] == 'The Adventures of Jimmy Neutron, Boy Genius') |
            (df['primaryTitle'] == 'Camp Candy') |
            (df['primaryTitle'] == 'Mighty Morphin Power Rangers') |
            (df['primaryTitle'] == 'The Fairly OddParents') |
            (df['primaryTitle'] == 'Fargo') |
            (df['primaryTitle'] == 'Nickelodeon Arcade') |
            (df['primaryTitle'] == 'Yes, Dear') |
            (df['primaryTitle'] == 'Desperate Housewives') |
            (df['primaryTitle'] == 'A Different World') |
            (df['primaryTitle'] == 'Banshee') |
            (df['primaryTitle'] == 'The King of Queens') |
            (df['primaryTitle'] == 'Martial Law') |
            (df['primaryTitle'] == 'Vanishing Son') |
            (df['primaryTitle'] == 'Police Academy: The Series') |
            (df['primaryTitle'] == 'Xena: Warrior Princess') |
            (df['primaryTitle'] == 'Doogie Howser, M.D.') |
            (df['primaryTitle'] == 'Mr. Belvedere') |
            (df['primaryTitle'] == 'Walker, Texas Ranger') |
            (df['primaryTitle'] == '7th Heaven') |
            (df['primaryTitle'] == 'Buffy the Vampire Slayer') |
            (df['primaryTitle'] == "That '70s Show") |
            (df['primaryTitle'] == 'Law & Order: Criminal Intent') |
            (df['primaryTitle'] == 'Nash Bridges') |
            (df['primaryTitle'] == 'The Wayans Bros.') |
            (df['primaryTitle'] == 'The Drew Carey Show') |
            (df['primaryTitle'] == 'The Jamie Foxx Show') |
            (df['primaryTitle'] == 'Tiny Toon Adventures') |
            (df['primaryTitle'] == 'Cobra Kai') |
            ((df['primaryTitle'] == 'Ducktales') & (df['startYear'] == 1987)) |             
            ((df['primaryTitle'] == 'The Pretender') & (df['startYear'] == 1996)) | 
            ((df['primaryTitle'] == 'Full House') & (df['startYear'] == 1987)) | 
            ((df['primaryTitle'] == 'Animaniacs') & (df['startYear'] == 1993)) | 
            ((df['primaryTitle'] == 'Amen') & (df['startYear'] == 1986)) | 
            ((df['primaryTitle'] == 'Legends of the Hidden Temple') & (df['startYear'] == 1993)) | 
            ((df['primaryTitle'] == 'Doug') & (df['startYear'] == 1991)) | 
            ((df['primaryTitle'] == 'The Wire') & (df['startYear'] == 2002)) |            
            ((df['primaryTitle'] == 'Rugrats') & (df['startYear'] == 1991)) |
            ((df['primaryTitle'] == 'Beavis and Butt-Head') & (df['startYear'] == 1993)) |
            ((df['primaryTitle'] == 'Charmed') & (df['startYear'] == 1998)) | 
            ((df['primaryTitle'] == 'Matlock') & (df['startYear'] == 1986)) | 
            ((df['primaryTitle'] == 'In Living Color') & (df['startYear'] == 1990)) | 
            ((df['primaryTitle'] == 'Saved by the Bell') & (df['startYear'] == 1989)))]
    except Exception as e:
        return print(f'cannot filter accordingly - {type(e)}')

fav_tv_shows_df = fav_tv_shows(gfg_ratings_merged_df.sort_values(by='primaryTitle', ascending=True))
fav_tv_shows_df.to_csv('fav_tv_shows.csv', index=False)
print('fav_tv_shows_df:\n',fav_tv_shows_df.to_string())

# creating charts via matplotlib
import matplotlib.pyplot as plt
# top 50 tv series
color = 'blue'
x = top_50_tv_series_df['primaryTitle'].astype(str)
y = top_50_tv_series_df['averageRating']
plt.barh(x, y, color=color)
plt.title('Top 50 TV Series')
plt.yticks(fontsize=8)
plt.xlabel('Rating')
plt.show()
# fav tv shows
x = fav_tv_shows_df['primaryTitle']
y = fav_tv_shows_df['runtimeMinutes']
plt.barh(x, y, color=color)
plt.title("Taleb's Favorite TV Shows - Runtime Minutes")
plt.yticks(fontsize=8)
plt.xlabel('Primary Title')
plt.ylabel('Runtime Minutes')
plt.show() 

import time

start_time = time.time()
print('\ntime of program execution -',(time.time() - start_time))


#===============================================================================================#
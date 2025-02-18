import pandas as pd

gfg_ratings_merged_df = pd.read_csv('gfg_ratings_merged.csv')
fav_tv_shows_df = pd.read_csv('fav_tv_shows.csv')
gfg_movie_df = pd.read_csv('gfg_movie.csv')
gfg_short_df = pd.read_csv('gfg_short.csv')
gfg_tv_episode_df = pd.read_csv('gfg_tv_episode.csv')
gfg_tv_miniseries_df = pd.read_csv('gfg_tv_miniseries.csv')
gfg_tv_movie_df = pd.read_csv('gfg_tv_movie.csv')
gfg_tv_pilot_df = pd.read_csv('gfg_tv_pilot.csv')
gfg_tv_series_df = pd.read_csv('gfg_tv_series.csv')
gfg_tv_short_df = pd.read_csv('gfg_tv_short.csv')
gfg_tv_special_df = pd.read_csv('gfg_tv_special.csv')
gfg_video_df = pd.read_csv('gfg_video.csv')
gfg_videogame_df = pd.read_csv('gfg_videogame.csv')

array = ['gfg_ratings_merged_df']

# gfg_movie_df
while True:
    df_answer = input('\ntype in name of dataframe:\n')
    # print(f"{gfg_movie_df.loc[(gfg_movie_df['primaryTitle'].str.contains(answer, na=False))]}")
    
    for x in array:
        if df_answer == f'{x}':
            primary_title_answer = input('\nenter primaryTitle value\n:')
            print(f"{gfg_movie_df.loc[(gfg_movie_df['primaryTitle'].str.contains(primary_title_answer, na=False))]}")
            
            

    if df_answer == 'exit query':
        break
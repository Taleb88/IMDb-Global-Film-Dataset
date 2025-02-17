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

# gfg_movie_df
gfg_movie_df = gfg_movie_df.loc[gfg_movie_df['primaryTitle'].str.contains('Hearts', na=False)]

print(gfg_movie_df)
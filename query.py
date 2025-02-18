import pandas as pd

dataframes = ['gfg_ratings_merged','fav_tv_shows','gfg_movie','gfg_short','gfg_tv_episode','gfg_tv_miniseries',
         'gfg_tv_movie','gfg_tv_series','gfg_tv_short','gfg_tv_special','gfg_video','gfg_videogame']
while True:
    df_answer = input('\ntype in name of dataframe:\n')

    for df_name in dataframes:
        if df_answer in df_name:
            df = pd.read_csv(f'{df_name}.csv')
            primary_title_answer = input('primary title:\n')
            print(f"{df[(df['primaryTitle'].str.contains(primary_title_answer, na=False))]}") 

    if df_answer == 'exit query':
        break
                     
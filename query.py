import pandas as pd

dataframes = ['gfg_ratings_merged','fav_tv_shows','gfg_movie','gfg_short','gfg_tv_episode','gfg_tv_miniseries',
         'gfg_tv_movie','gfg_tv_series','gfg_tv_short','gfg_tv_special','gfg_video','gfg_videogame']
# capture primary title value only
while True:
    try: 
        df_answer = input('\ntype in name of dataframe:\n')

        if df_answer == 'exit query':
            break

        if df_answer not in dataframes:
            print('dataframe not found. please try again.')

        for df_name in dataframes:
            if df_answer == 'exit query':
                break
            if df_answer in df_name:
                df = pd.read_csv(f'{df_name}.csv')
                primary_title_values = list(df['primaryTitle'].values)
                primary_title_answer = input('primary title:\n')
                if (primary_title_answer in primary_title_values):
                    print(f"{df[(df['primaryTitle'].str.contains(primary_title_answer, na=False))]}")                                  
    except Exception as e:
        print(f'error - dataframe does not exist - {type(e)}')
        continue
# capture primary title + start year values
while True:
    try: 
        df_answer = input('\ntype in name of dataframe:\n')
        
        if df_answer == 'exit query':
            break

        if df_answer not in dataframes:
            print('dataframe not found. please try again.')
        
        for df_name in dataframes:
            if df_answer == 'exit query':
                break            
            if df_answer in df_name:
                df = pd.read_csv(f'{df_name}.csv')
                primary_title_values = list(df['primaryTitle'].values)
                start_year_values = list(df['startYear'].values)
                primary_title_answer = input('primary title:\n')
                start_year_answer = int(input('start year:\n'))
                if (primary_title_answer in primary_title_values) and (start_year_answer in start_year_values):
                    print(f"{df[(df['primaryTitle'].str.contains(primary_title_answer, na=False)) & (df['startYear'] == start_year_answer)]}")    
    except Exception as e:
        print(f'error - dataframe does not exist - {type(e)}')
        continue                    
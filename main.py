import pandas as pd

gfg_df = pd.read_csv('csv/GfG.csv', low_memory=False)

my_list = list(gfg_df.columns)
index = 0

for col_name in my_list:
    print(index, col_name)
    index +=1

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

#additional cleanup conducted - filter all movies/tv shows with startYear = 0 and make corrections per title
start_year_value_zero_title_type_short_df = gfg_df.loc[(gfg_df['startYear'] == 0) & (gfg_df['titleType'] == 'short')]
print('\n',start_year_value_zero_title_type_short_df.sort_values(by=['primaryTitle'], ascending=True),'\n')




'''def movie_1980s(df):
    try:
        return df[(df['titleType'] == 'movie') &\
                  (df['startYear'] >= 1980) &\
                  (df['startYear'] <= 1989)]
    except Exception as e:
        return(f'cannot filter out rows not meeting criteria {type(e)}')

print('movies from the 1980s:\n',movie_1980s(gfg_df),'\n')'''

#===============================================================================================#
import pandas as pd

gfg_df = pd.read_csv('GfG.csv', low_memory=False)

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
print('runtimeMinutes:\n',gfg_df['runtimeMinutes'].unique(),'\n')
print('genres:\n',gfg_df['genres'].unique(),'\n')

#gfg_df['isAdult'] = gfg_df['isAdult'].astype(str)
gfg_df['isAdult'] = gfg_df['isAdult'].replace("\\N",'No')
#gfg_df['isAdult'] = gfg_df['isAdult'].replace("0",'No')

gfg_df['startYear'] = gfg_df['startYear'].replace("\\N",0000).astype(int)

print('\nisAdult:',gfg_df['isAdult'].unique(),'\n')
print('\nstartYear:',gfg_df['startYear'].unique(),'\n')

def movie_1980s(df):
    try:
        return df[(df['titleType'] == 'movie') &\
                  (df['startYear'] >= 1980) &\
                  (df['startYear'] <= 1989)]
    except Exception as e:
        return(f'cannot filter out rows not meeting criteria {type(e)}')

print('movies from the 1980s:\n',movie_1980s(gfg_df),'\n')
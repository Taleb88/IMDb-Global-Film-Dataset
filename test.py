import pandas as pd

ratings_df = pd.read_table('title.ratings.tsv')
title_basics_df = pd.read_table('title.basics.tsv')
title_crew_df = pd.read_table('title.crew.tsv')

ratings_df.to_csv('ratings.csv', index=False)
title_basics_df.to_csv('title_basics.csv', index=False)
title_crew_df.to_csv('title_crew.csv', index=False)

print('\nratings_df:',ratings_df,'\n')
print('title_basics_df:',title_basics_df,'\n')
print('title_crew_df:',title_crew_df,'\n')

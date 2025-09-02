import pandas as pd

df=pd.read_csv('movies_collaborative.csv')
df.head()

user_movie_matrix = df.pivot_table(index='userId', columns='movieId', values='rating')

user_movie_matrix.fillna(0,inplace=True)

user_movie_matrix

from sklearn.neighbors import NearestNeighbors

model=NearestNeighbors(metric='cosine')
model.fit(user_movie_matrix)

ti=0
dis,idx=model.kneighbors([user_movie_matrix.iloc[ti]],n_neighbors=5)

idx

si=idx[0][1]
si

movie_by_similar_user=user_movie_matrix.iloc[si]

movie_by_similar_user

movie_by_target_user=user_movie_matrix.iloc[ti]

movie_by_target_user

user_movie_matrix.columns

recamond_movie={}
for m,t,s in zip (user_movie_matrix.columns,movie_by_target_user,movie_by_similar_user):
    if t==0 and s!=0:
        recamond_movie[m]=s

recamond_movie

final_movie_tob_recom=[]
for k,v in recamond_movie.items():
    if v>=5:
        final_movie_tob_recom.append(k)

final_movie_tob_recom

result=df[df.movieId.isin(final_movie_tob_recom)].title.unique()
result

for i in result:
    print(i)

df[df.movieId.isin(final_movie_tob_recom)].title.value_counts().head(10)




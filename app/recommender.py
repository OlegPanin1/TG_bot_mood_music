import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Загружаем треки
df = pd.read_csv("app/data/top_100k_tracks.csv")

# Подбираем числовые признаки (можно расширить)
features = df[['valence', 'energy', 'tempo']]

# Строим модель KNN (можно заранее сохранить и подгружать)
knn = NearestNeighbors(n_neighbors=5, algorithm='auto')
knn.fit(features)

# Главная функция
def get_recommendations(valence, energy, tempo):
    query = [[valence, energy, tempo]]
    distances, indices = knn.kneighbors(query)
    recommendations = df.iloc[indices[0]][['track_name', 'artist', 'genre', 'tempo']]
    return recommendations.to_dict(orient='records')

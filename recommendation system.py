import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix

# Step 1: Load the Data
# Example data where rows are users and columns are items (movies, books, products for users)
# we can replace this with your actual data
data = {
    'user_id': [1, 2, 3, 4, 5],
    'item_1': [5, 4, 0, 0, 1],
    'item_2': [4, 0, 0, 2, 2],
    'item_3': [0, 0, 4, 5, 3],
    'item_4': [0, 3, 3, 0, 5],
    'item_5': [1, 0, 0, 0, 4]
}

# Convert data into a DataFrame
df = pd.DataFrame(data)

# Step 2: Prepare the data for the model (create a sparse matrix)
user_item_matrix = df.set_index('user_id').values
sparse_matrix = csr_matrix(user_item_matrix)

# Step 3: Create the recommendation model using Nearest Neighbors
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(sparse_matrix)

# Step 4: Create a function to recommend items to a user
def recommend_items(user_id, num_recommendations=2):
    user_index = user_id - 1  # adjust for 0-indexed matrix
    
    # Step 5: Find similar users based on the user's item ratings
    distances, indices = model.kneighbors(sparse_matrix[user_index], n_neighbors=num_recommendations+1)
    
    # Step 6: Recommend items from similar users that the current user has not rated
    similar_user_indices = indices.flatten()[1:]  # exclude the user itself
    recommended_items = []
    
    for similar_user_index in similar_user_indices:
        similar_user_ratings = user_item_matrix[similar_user_index]
        for item_idx, rating in enumerate(similar_user_ratings):
            if user_item_matrix[user_index][item_idx] == 0 and rating > 0:  # item not rated by current user
                recommended_items.append(f'item_{item_idx + 1}')
    
    return list(set(recommended_items))  # return unique items

# Step 7: Get recommendations for a specific user
user_id = 1  # You can change this to test different users
recommendations = recommend_items(user_id, num_recommendations=2)
print(f"Recommended items for User {user_id}: {recommendations}")

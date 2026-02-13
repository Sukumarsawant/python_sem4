def jaccard_similarity (set1, set2):
    a = len(set1.union(set2))
    b = len(set1.intersection(set2))
    if b==0 : return 0.0
    return a/b #float

### Calculate Jaccard Similarity between two sets

# Formula: |A ∩ B| / |A ∪ B|
# Return Jaccard Similarity

def find_most_similar_user(users, target_user):
    most_sim ="pre"
    max_sim = 0.0 
    for user_id,products in users.items() :
        if user_id != target_user : 
            temp =jaccard_similarity(products,users[target_user])
            if(max_sim>temp) :
                continue
            else : 
               max_sim = temp
               most_sim = user_id
    return most_sim, max_sim
    


## Find the user most similar to the target user

# Get product set of target_user
# Loop through users and calculate similarity
# Return most similar user and similarity score
pass
def recommend_products(users, target_user, similar_user) : 
    target_products = users[target_user]
    similar_user_products = users[similar_user]

    ans = similar_user_products.difference(target_products)
    return  ans


### Recommend products not yet seen by target user

# Get product sets of target and similar users
# Find recommended products using set difference
pass
if __name__ == "__main__":
    users = {
    "U1": {"P101", "P102", "P103"},
     "U2": {"P102", "P103", "P104", "P105"},
    "U3": {"P106", "P107"},
    "U4": {"P101", "P103", "P104"}
     }
    target_user = "U1"
    most_similar_user, max_value = find_most_similar_user(users,target_user)
    final_products = recommend_products(users,target_user,most_similar_user)
    print(f"Similarity score for {target_user} : ",max_value)
    if max_value!=0.0 :
        print(f"recommendations for {most_similar_user} : " , final_products)
    else : print(f"No Recommendations ")
# Find most similar user
# Recommend products
# Display similarity scores and recommendations
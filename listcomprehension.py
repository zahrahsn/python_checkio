
def get_mae(leaf_size):
    return 5*leaf_size
if __name__=="__main__":
    candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
scores = {leaf_size: get_mae(leaf_size) for leaf_size in candidate_max_leaf_nodes}
best_tree_size = min(scores, key=scores.get)
print(scores)
print(best_tree_size)


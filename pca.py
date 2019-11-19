import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

diffs = pd.read_pickle("./models/diffs.pkl")

norm1 = np.sqrt(np.sum(diffs * diffs, axis=0))
#plt.hist(norm1, normed=True, bins=30)
#norm2 = norm(diffs)
diffs = StandardScaler().fit_transform(diffs)
#pca = PCA(n_components=2)
pca = PCA(0.8).fit(diffs)
#principalComponents = pca.fit_transform(diffs)
#principalDf = pd.DataFrame(data = principalComponents
#             , columns = ['principal component 1', 'principal component 2'])
print(pca.n_components_)
print(pca.explained_variance_ratio_)
#make a histogram of differences sizes
#filter differences by size

# TODO only use top used entities and also similarity
# TODO entities in either side visualization
# TODO Cosine similarity
# TODO dist of distances among most used entities
# TODO projection of other words to this direction and look at those which are more aligned to this direction
# TODO take all pairs of entities and look at their distances all the terms vs most popular ones
# do the same thing with patrick's data

print("finish")
# Standardize the measure mean = 0 variance = 1

# check pca.explained ratio and try to keep it above 95%
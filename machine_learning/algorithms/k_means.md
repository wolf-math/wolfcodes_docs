---
title: K-Means Clustering
sidebar_position: 10
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is k-means clustering?

**K-means** is an **unsupervised** learning algorithm that groups data points into $K$ clusters based on similarity. Unlike the other algorithms in this section, it doesn't need labels. You give it raw data and the number of groups you want, and it finds the groups for you.

Each cluster is represented by its **centroid**: the average position of all the points in that cluster.

## Why this matters

Most real-world data has no labels. K-means lets you find structure in it anyway: customer segments, groups of similar documents, or clusters of sensor readings. It's simple, fast, and usually the first clustering algorithm to try.

## How k-means works

1. **Choose $K$**: Decide how many clusters you want.
2. **Place the centroids**: Start with $K$ centroids at initial positions (scikit-learn uses a smart random start called *k-means++*).
3. **Assign points**: Assign every data point to its nearest centroid.
4. **Move the centroids**: Move each centroid to the average position of the points assigned to it.
5. **Repeat**: Go back to step 3 until the assignments stop changing (the algorithm has **converged**).

Behind the scenes, k-means is minimizing the **inertia**: the total squared distance from each point to its cluster's centroid. Lower inertia means tighter clusters.

## Example: segmenting customers

Imagine a store that wants to group its customers into personas for marketing, based on two features:

1. Annual income
2. Spending score (how much they spend relative to other customers)

### Import the packages

```python
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
```

### Create the data

`make_blobs` generates points around a few hidden centers. In a real project you wouldn't know how many groups there are; that's what we'll try to discover.

```python
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.9, random_state=42)

# Like KNN, k-means relies on distances, so scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

Notice we throw away the labels (`_`). K-means never sees them.

### Choose K with the elbow method

How many clusters should you ask for? The **elbow method** runs k-means for a range of $K$ values and plots the inertia. Inertia always decreases as $K$ grows, but at some point the improvement suddenly levels off. That bend, the "elbow," is a good choice for $K$.

```python
inertias = []
k_values = range(1, 10)

for k in k_values:
    kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

plt.plot(k_values, inertias, marker='o')
plt.xlabel('Number of clusters (K)')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()
```

For this data, the elbow appears at $K = 4$.

### Fit the final model

```python
kmeans = KMeans(n_clusters=4, n_init=10, random_state=42)
labels = kmeans.fit_predict(X_scaled)  # Cluster number (0-3) for each customer

print(labels[:10])
print("Centroids:\n", kmeans.cluster_centers_)
```

`n_init=10` runs the algorithm 10 times from different starting centroids and keeps the best result. K-means can get stuck in a poor solution depending on where it starts, so multiple runs make it more reliable.

### Plot the clusters

```python
plt.figure(figsize=(9, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap='viridis', s=40, edgecolor='k')
plt.scatter(
    kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
    c='red', marker='X', s=250, label='Centroids',
)
plt.title('Customer Segments Found by K-Means')
plt.xlabel('Annual income (scaled)')
plt.ylabel('Spending score (scaled)')
plt.legend()
plt.show()
```

### Use the model on new data

Once fitted, the model can assign new customers to the nearest existing segment. Scale them with the same fitted scaler first, because the model learned its centroids in scaled units:

```python
new_customers = [[-2.5, 9.0], [4.5, 2.0]]  # Raw feature values
new_scaled = scaler.transform(new_customers)
print(kmeans.predict(new_scaled))
```

## Limitations

- **You must choose $K$**: The algorithm can't tell you how many clusters exist. Use the elbow method or domain knowledge.
- **It assumes round, similar-sized clusters**: K-means struggles with elongated, irregular, or very unevenly sized groups.
- **It's sensitive to scale and outliers**: Always scale your features, and consider removing extreme outliers, which can drag centroids away from the real groups.
- **Cluster numbers have no meaning**: "Cluster 2" is just a label. It's up to you to inspect each cluster and give it a meaningful name, like "bargain hunters."

## Common mistakes

### Clustering unscaled data

```python
# Wrong: income (tens of thousands) drowns out age (tens)
KMeans(n_clusters=4).fit(X)

# Correct
KMeans(n_clusters=4).fit(StandardScaler().fit_transform(X))
```

### Forcing a K the data doesn't support

K-means always returns exactly $K$ clusters, even if the data has no real groups. Check the elbow plot, and look at the clusters to see whether they make sense.

### Using it on oddly shaped clusters

K-means assumes round, similar-sized groups. For long, curved, or very uneven clusters, try a density-based algorithm like DBSCAN.

## Summary

- K-means groups unlabeled data into $K$ clusters, each represented by a centroid.
- It repeats two steps until stable: assign points to the nearest centroid, then move each centroid to the middle of its points.
- Scale your features, and use the elbow method to choose $K$.
- It works best for compact, roughly round clusters.

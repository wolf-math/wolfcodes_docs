---
title: Feature Engineering
sidebar_position: 5
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is feature engineering?

**Feature engineering** is the work of cleaning, transforming, and creating the input columns (**features**) that a model learns from. It's often the most important phase of the machine learning pipeline. Advanced algorithms are powerful, but the quality of your features sets the ceiling on how well any model can perform.

As the saying goes: **"Garbage in, garbage out."**

## Why this matters

Good features can make a simple model outperform a complex model with bad features. It's like giving a detective the right clues: with them, the mystery gets solved quickly. Without them, the model simply can't see the patterns hidden in the data.

This is also where data scientists spend most of their time. Feature engineering has three parts:

1. **Data cleaning**: Fixing missing values and outliers so the data is consistent and reliable.
2. **Feature transformation**: Scaling, reshaping, and encoding features into a form algorithms can learn from.
3. **Feature creation**: Building new features from the ones you have, so patterns become easier for the model to see.

## Data cleaning

Before modeling, make sure your data is clean, consistent, and reliable.

### Handling missing data

You can either **drop** rows or columns with missing values, or **impute** them (fill them in). Common imputation strategies include:

- Mean, median, or mode substitution
- A constant value (for example, `0` or `"Unknown"`)
- Predictive approaches like KNN imputation

Here's a small dataset with missing values to practice on:

```python
import numpy as np
import pandas as pd

data = {
    'Age': [25, np.nan, 35, 45, 22, 38],
    'Salary': [50000, 60000, np.nan, 80000, 45000, np.nan],
    'Department': ['HR', 'IT', 'HR', np.nan, 'Finance', 'IT'],
}

df = pd.DataFrame(data)
print('Original dataset:')
print(df)
```

#### Univariate imputation with `SimpleImputer`

`SimpleImputer` fills in each column independently using a simple statistic. It's fast and makes a great baseline.

- **Numeric features**: mean, median, or a constant value.
- **Categorical features**: most frequent value (mode) or a constant string like `"Missing"`.

```python
from sklearn.impute import SimpleImputer

numeric_cols = ['Age', 'Salary']
categorical_cols = ['Department']

# Numeric columns: fill with the median
num_imputer = SimpleImputer(strategy='median')
df_numeric = pd.DataFrame(
    num_imputer.fit_transform(df[numeric_cols]), columns=numeric_cols
)

# Categorical columns: fill with the most frequent value
cat_imputer = SimpleImputer(strategy='most_frequent')
df_categorical = pd.DataFrame(
    cat_imputer.fit_transform(df[categorical_cols]), columns=categorical_cols
)

df_simple_imputed = pd.concat([df_numeric, df_categorical], axis=1)
print(df_simple_imputed)
```

#### Local structure imputation with `KNNImputer`

`KNNImputer` uses the [k-nearest neighbors](../algorithms/knn.md) idea. Instead of looking at one column in isolation, it finds the $k$ most similar rows and fills the gap with the average of their values.

- **Best for**: Data where similar rows tend to have similar values (customer records, medical records).
- **Note**: It requires numeric data, so encode categorical columns first.

```python
from sklearn.impute import KNNImputer

# Convert the categorical column into numeric dummy columns first
df_encoded = pd.get_dummies(df, columns=['Department'], dtype=float)

knn_imputer = KNNImputer(n_neighbors=2)
df_knn_imputed = pd.DataFrame(
    knn_imputer.fit_transform(df_encoded), columns=df_encoded.columns
)

print(df_knn_imputed)
```

#### Multivariate imputation (MICE) with `IterativeImputer`

**MICE** (Multivariate Imputation by Chained Equations), available in scikit-learn as `IterativeImputer`, models each column with missing values as a function of the other columns. It treats the missing values as a prediction target, fills them in, and repeats in rounds until the values settle.

- **Best for**: Complex datasets where features are related to each other in intricate ways.
- **Note**: `IterativeImputer` is experimental in scikit-learn, so you must enable it explicitly before importing it.

```python
# IterativeImputer is experimental, so enable it first
from sklearn.experimental import enable_iterative_imputer  # noqa: F401
from sklearn.impute import IterativeImputer

# Uses BayesianRidge regression by default
mice_imputer = IterativeImputer(max_iter=10, random_state=42)
df_mice_imputed = pd.DataFrame(
    mice_imputer.fit_transform(df_encoded), columns=df_encoded.columns
)

print(df_mice_imputed)
```

### Handling outliers

**Outliers** are extreme values that don't fit the rest of the data. They can heavily skew distance-based algorithms (like [SVMs](../algorithms/support_vector_machines.md) and KNN) and linear models. Use statistical bounds to find them, then decide whether to remove, clip, or transform them based on what makes sense for your domain.

Here's a dataset with some deliberate outliers:

```python
import numpy as np
import pandas as pd

np.random.seed(42)
normal_data = np.random.normal(loc=50, scale=10, size=95)
outliers = np.array([105, -15, 120, 5, 135])

df = pd.DataFrame({'income_proxy': np.concatenate([normal_data, outliers])})
```

#### The z-score method

A **z-score** measures how many standard deviations a value is from the mean:

$$
Z = \frac{x - \mu}{\sigma}
$$

- $x$ is the value, $\mu$ is the mean, and $\sigma$ is the standard deviation.
- **Best for**: Data that's roughly normally distributed.
- **Common threshold**: An absolute z-score above 3 (or 2.5 for stricter filtering) is flagged as an outlier.

```python
from scipy import stats

z_scores = np.abs(stats.zscore(df['income_proxy']))
threshold = 3

df_filtered_z = df[z_scores < threshold]
print(f"Original rows: {len(df)}, after z-score filter: {len(df_filtered_z)}")
```

#### The interquartile range (IQR) method

The **IQR** method uses percentiles instead of the mean and standard deviation. That makes it robust for skewed data, where the outliers themselves would drag the mean around.

$$
\text{IQR} = Q_3 - Q_1
$$

$$
\text{Lower bound} = Q_1 - 1.5 \times \text{IQR}
\qquad
\text{Upper bound} = Q_3 + 1.5 \times \text{IQR}
$$

- $Q_1$ is the 25th percentile and $Q_3$ is the 75th percentile.
- **Best for**: Skewed data or distributions with heavy tails.

```python
Q1 = df['income_proxy'].quantile(0.25)
Q3 = df['income_proxy'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df_filtered_iqr = df[
    (df['income_proxy'] >= lower_bound) & (df['income_proxy'] <= upper_bound)
]
print(f"Original rows: {len(df)}, after IQR filter: {len(df_filtered_iqr)}")
```

#### Removing vs. clipping

Dropping rows throws away training data, which hurts most when outliers are scattered across many different columns. Two alternatives keep every row:

- **Clipping (winsorization)**: Cap extreme values at the lower and upper bounds instead of deleting them.
- **Transformation**: Apply a log or power transform to compress the scale (covered below).

```python
df['income_clipped'] = df['income_proxy'].clip(lower=lower_bound, upper=upper_bound)

print('Max before clipping:', df['income_proxy'].max())
print('Max after clipping:', df['income_clipped'].max())
```

## Feature transformation

Raw features often don't match what a model expects in terms of scale, distribution, or data type. Transformations reshape them into something the algorithm can learn from more effectively.

Here's a sample dataset with a mix of feature types:

```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, PowerTransformer, StandardScaler

np.random.seed(42)

df = pd.DataFrame(
    {
        'income': np.random.exponential(scale=30000, size=100) + 20000,  # Skewed
        'age': np.random.randint(18, 70, size=100),  # Continuous
        'education_level': ['High School', 'Bachelor', 'Master', 'PhD'] * 25,  # Ordered categories
        'city': ['New York', 'London', 'Tokyo', 'Paris'] * 25,  # Unordered categories
        'target': np.random.choice([0, 1], size=100),  # Binary target
    }
)
```

### Scaling

Algorithms that are sensitive to the size of numbers ([gradient descent](../deep_learning/gradient_descent.md), neural networks, KNN, SVMs) need features on comparable scales. Otherwise a feature measured in thousands (salary) drowns out one measured in tens (age).

- **Standardization** (z-score scaling) centers a feature at a mean of 0 with a standard deviation of 1.
- **Min-max scaling** squeezes a feature into the range 0 to 1.

```python
std_scaler = StandardScaler()
minmax_scaler = MinMaxScaler()

df['age_standardized'] = std_scaler.fit_transform(df[['age']])
df['age_minmax'] = minmax_scaler.fit_transform(df[['age']])

print(df[['age', 'age_standardized', 'age_minmax']].head(3).to_string(index=False))
```

**Rule of thumb:** Use scikit-learn's scalers rather than doing the math by hand. A fitted scaler remembers the training data's statistics, so you can apply the exact same transformation to new data later.

:::warning
Fit scalers on the **training set only**, then use `.transform()` on the test set. Fitting on the full dataset leaks information about the test set into training.
:::

### Handling skewed distributions

Highly skewed features, like income or website traffic, have long tails that can destabilize linear models. A **log transformation** or a **power transformation** pulls in the long tail and evens out the spread.

- `np.log1p()` computes `log(1 + x)`, which safely handles zeros.
- **Box-Cox** requires strictly positive values.
- **Yeo-Johnson** works with zero and negative values too.

```python
df['income_log'] = np.log1p(df['income'])

pt = PowerTransformer(method='yeo-johnson')
df['income_yeojohnson'] = pt.fit_transform(df[['income']])

print(df[['income', 'income_log', 'income_yeojohnson']].head(3).to_string(index=False))
```

### Encoding categorical variables

Models need numbers, so text categories must be converted. The right encoding depends on whether the categories have a natural order and how many distinct values there are.

#### One-hot encoding

**One-hot encoding** creates a new 0/1 column for each category. It's ideal for **nominal** categories (no natural order) with few distinct values, like `city`.

```python
df_encoded = pd.get_dummies(df, columns=['city'], drop_first=True, dtype=int)
print(df_encoded.filter(like='city_').head(3))
```

`drop_first=True` avoids the **dummy variable trap**. If you keep all four city columns, any one of them can be perfectly predicted from the other three (if it's not London, New York, or Paris, it must be Tokyo). That redundancy, called **multicollinearity**, can confuse linear models. Dropping one column removes it without losing information.

:::tip
`pd.get_dummies()` is great for quick analysis. Inside production pipelines, prefer scikit-learn's `OneHotEncoder`, which remembers the categories it saw during training.
:::

#### Ordinal encoding

**Ordinal encoding** maps categories to integers that preserve their natural order, like low → medium → high.

```python
education_mapping = {'High School': 1, 'Bachelor': 2, 'Master': 3, 'PhD': 4}
df['education_ordinal'] = df['education_level'].map(education_mapping)

print(df[['education_level', 'education_ordinal']].drop_duplicates())
```

#### Target (mean) encoding

**Target encoding** replaces each category with the average value of the target for that category. It's very effective for **high-cardinality** features with many distinct values (zip codes, user IDs) where one-hot encoding would create thousands of columns.

Because it uses the target, it can leak information and cause [overfitting](../deep_learning/regularization.md). Use **smoothing** (pulling rare categories toward the global average) and calculate it within [cross-validation](./evaluation.md#robust-validation-strategies) folds.

```python
def target_encode(data, categorical_col, target_col, smoothing=10):
    """Replace each category with a smoothed mean of the target."""
    global_mean = data[target_col].mean()

    stats = data.groupby(categorical_col)[target_col].agg(['count', 'mean'])
    counts = stats['count']
    means = stats['mean']

    # Rare categories are pulled toward the global mean
    smooth_means = (counts * means + smoothing * global_mean) / (counts + smoothing)

    return data[categorical_col].map(smooth_means)


df['city_target_encoded'] = target_encode(df, 'city', 'target')
print(df[['city', 'city_target_encoded']].drop_duplicates())
```

### Choosing an encoding

| Situation | Encoding |
|-----------|----------|
| Unordered categories, few values (`color`, `city`) | One-hot |
| Ordered categories (`low`, `medium`, `high`) | Ordinal |
| Unordered categories, many values (`zip_code`) | Target encoding (with smoothing) |

## Feature creation

**Feature creation** means building new columns out of the ones you already have. A model can only learn from what it's shown. If the useful pattern is hidden inside a *combination* of columns, creating that combination as its own feature hands the model the clue directly.

For example, a house's price depends heavily on its floor area. If your data only has `width` and `depth`, a linear model can't multiply them together on its own. Create `area = width * depth` and the pattern becomes a straight line it can learn easily.

Most created features come from a handful of recipes. The examples below use this small table of online orders:

```python
import numpy as np
import pandas as pd

orders = pd.DataFrame(
    {
        'customer_id': [1, 1, 2, 2, 2, 3],
        'order_time': pd.to_datetime(
            [
                '2025-03-01 09:15', '2025-03-08 21:40', '2025-03-02 13:05',
                '2025-03-03 23:55', '2025-03-09 10:30', '2025-03-05 18:20',
            ]
        ),
        'total': [120.0, 45.0, 300.0, 80.0, 150.0, 60.0],
        'items': [4, 1, 10, 2, 3, 3],
    }
)
```

### Ratios and differences

Dividing or subtracting two columns often captures what really matters better than either column alone:

```python
orders['avg_item_price'] = orders['total'] / orders['items']
print(orders[['total', 'items', 'avg_item_price']])
```

**Output:**

```text
   total  items  avg_item_price
0  120.0      4            30.0
1   45.0      1            45.0
2  300.0     10            30.0
3   80.0      2            40.0
4  150.0      3            50.0
5   60.0      3            20.0
```

Other common examples: price per square foot, debt-to-income ratio, clicks per visit, or the time between two events.

:::warning
Watch out for division by zero. If the denominator can be 0, decide what the ratio should mean in that case, and handle it explicitly (for example, with `np.where`).
:::

### Date and time parts

A raw timestamp is almost useless to most models. The parts inside it, like the hour, the day of the week, or whether it's a weekend, often carry the real signal:

```python
orders['hour'] = orders['order_time'].dt.hour
orders['day_of_week'] = orders['order_time'].dt.dayofweek  # Monday = 0
orders['is_weekend'] = (orders['day_of_week'] >= 5).astype(int)

print(orders[['order_time', 'hour', 'day_of_week', 'is_weekend']])
```

**Output:**

```text
           order_time  hour  day_of_week  is_weekend
0 2025-03-01 09:15:00     9            5           1
1 2025-03-08 21:40:00    21            5           1
2 2025-03-02 13:05:00    13            6           1
3 2025-03-03 23:55:00    23            0           0
4 2025-03-09 10:30:00    10            6           1
5 2025-03-05 18:20:00    18            2           0
```

#### Cyclical features

Some values wrap around. To a model, hour 23 and hour 0 look far apart (23 vs. 0), but they're only an hour apart in reality. Encoding the hour as a point on a circle, using sine and cosine, fixes that:

```python
orders['hour_sin'] = np.sin(2 * np.pi * orders['hour'] / 24)
orders['hour_cos'] = np.cos(2 * np.pi * orders['hour'] / 24)
```

Now 23:00 and 00:00 end up close together. The same trick works for day of the week (divide by 7) and month (divide by 12).

### Aggregations

Sometimes the most useful information about a row is how it compares to a *group* of rows. For orders, that might be each customer's typical spending:

```python
orders['customer_avg_total'] = orders.groupby('customer_id')['total'].transform('mean')
orders['customer_order_count'] = orders.groupby('customer_id')['total'].transform('count')

# How unusual is this order for this customer?
orders['total_vs_usual'] = orders['total'] / orders['customer_avg_total']

print(orders[['customer_id', 'total', 'customer_avg_total', 'total_vs_usual']])
```

**Output:**

```text
   customer_id  total  customer_avg_total  total_vs_usual
0            1  120.0           82.500000        1.454545
1            1   45.0           82.500000        0.545455
2            2  300.0          176.666667        1.698113
3            2   80.0          176.666667        0.452830
4            2  150.0          176.666667        0.849057
5            3   60.0           60.000000        1.000000
```

`transform()` calculates the statistic for each group and copies it back onto every row of that group, so the result lines up with the original table. Features like `total_vs_usual` are the backbone of fraud detection: a purchase five times larger than a customer's normal one is a strong signal.

:::warning
Aggregations are a common source of **data leakage**. The averages above use *all* of a customer's orders, including ones that happened after the order being predicted. When predicting something in time order, only aggregate over **past** rows, and calculate group statistics from the training set only.
:::

### Interactions

An **interaction feature** multiplies two features together. It captures effects that depend on both at once, like a discount that only matters on weekends, or floor area as width × depth. scikit-learn can generate every pairwise product for you:

```python
from sklearn.preprocessing import PolynomialFeatures

X = orders[['items', 'is_weekend']]

poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
X_interact = poly.fit_transform(X)

print(poly.get_feature_names_out())
```

**Output:**

```text
['items' 'is_weekend' 'items is_weekend']
```

:::tip
Interactions multiply quickly: 20 features produce 190 pairwise products. Create the few that make sense for your problem rather than all of them. Tree-based models like [random forests](../algorithms/random_forests.md) find many interactions on their own, so interaction features help linear models the most.
:::

### Binning

**Binning** turns a continuous feature into a small number of ranges. It's useful when the relationship changes in steps rather than smoothly, or when you want a model to treat "small", "medium", and "large" orders differently.

```python
orders['order_size'] = pd.cut(
    orders['total'],
    bins=[0, 75, 200, np.inf],
    labels=['small', 'medium', 'large'],
)
print(orders[['total', 'order_size']])
```

**Output:**

```text
   total order_size
0  120.0     medium
1   45.0      small
2  300.0      large
3   80.0     medium
4  150.0     medium
5   60.0      small
```

Binning throws away detail (an order of 76 and an order of 199 become identical), so use it deliberately. The result is a category, so [encode it](#encoding-categorical-variables) before training.

### Does the new feature help? Measure it

A created feature is a hypothesis: "this combination matters." Test it the same way you'd test a model, by comparing cross-validated scores with and without it.

Here, house prices depend on floor area, but the data only has width and depth:

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

np.random.seed(42)
houses = pd.DataFrame(
    {
        'width': np.random.uniform(20, 60, 300),  # Feet
        'depth': np.random.uniform(20, 60, 300),  # Feet
    }
)
# Price depends on area, plus noise
houses['price'] = 150 * houses['width'] * houses['depth'] + np.random.normal(0, 20000, 300)

model = LinearRegression()

before = cross_val_score(model, houses[['width', 'depth']], houses['price'], cv=5).mean()

houses['area'] = houses['width'] * houses['depth']
after = cross_val_score(model, houses[['width', 'depth', 'area']], houses['price'], cv=5).mean()

print(f"R^2 without area: {before:.3f}")
print(f"R^2 with area:    {after:.3f}")
```

**Output:**

```text
R^2 without area: 0.907
R^2 with area:    0.955
```

Adding one created feature noticeably improves the same simple model, with no extra tuning. If a new feature doesn't improve the cross-validated score, drop it: extra features that add nothing just make the model slower and easier to overfit.

### Feature creation best practices

- **Start from domain knowledge**: Ask what a human expert would look at. Loan officers think in debt-to-income ratios; fraud analysts think in "unusual for this customer." Those are your best feature ideas.
- **Never use information from the future**: Only build features from data that would actually be available at prediction time.
- **Create features inside your pipeline**: Apply the same feature-creation code to training data, test data, and new data in production, so they always match.
- **Measure, don't assume**: Keep a feature only if it improves validation performance.

## Summary

- Feature quality sets the ceiling on model performance.
- Clean first: impute missing values (simple, KNN, or MICE) and handle outliers (z-score or IQR, then remove or clip).
- Then transform: scale features for distance- and gradient-based models, and tame skewed distributions with log or power transforms.
- Encode categories based on order and cardinality, and always fit transformations on training data only.
- Create new features (ratios, date parts, aggregations, interactions, bins) to expose hidden patterns, avoid leaking future information, and keep only the ones that measurably help.

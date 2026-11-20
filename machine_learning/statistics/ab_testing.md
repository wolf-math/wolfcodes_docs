---
title: A/B Testing
sidebar_position: 3
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is A/B testing?

**A/B testing** is a controlled experiment that compares two versions of something to see which performs better. Users are randomly split into two groups: one sees version A, the other sees version B. You measure a key outcome for each group, then use a statistical test to decide whether the difference is real or just chance.

## Why this matters

Offline test scores only tell you how a model does on historical data. A/B testing tells you how it does with real users, right now. It's the standard way companies decide whether a new model, feature, or design actually ships, and it protects you from launching a change that only looked better by chance.

## A/B testing machine learning models

When deploying a model to production (a recommendation system, fraud detector, or click-through predictor), teams often use a **champion-challenger** setup:

- **Model A (champion)**: The model currently in production.
- **Model B (challenger)**: The new, upgraded model, such as a newly trained neural network or XGBoost model.

Incoming traffic is randomly split so each request is handled by either Model A or Model B. You then track **key performance indicators (KPIs)** like conversion rate, click-through rate, or revenue, and test whether the challenger *statistically* outperforms the champion.

**Rule of thumb:** A challenger that looks better on offline test data still needs to prove itself on live traffic before it replaces the champion.

## Example: comparing two recommendation models

Let's simulate an A/B test between two recommendation models. The outcome is binary: did the user click the recommended product (1) or not (0)?

### Set up the data

```python
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

# Model A (champion): 10,000 recommendations served, 1,250 clicks
clicks_a, served_a = 1250, 10000

# Model B (challenger): 10,000 recommendations served, 1,380 clicks
clicks_b, served_b = 1380, 10000

clicks = np.array([clicks_a, clicks_b])
served = np.array([served_a, served_b])
```

### Calculate the conversion rates

```python
rate_a = clicks_a / served_a
rate_b = clicks_b / served_b

print(f"Model A conversion rate: {rate_a:.2%}")
print(f"Model B conversion rate: {rate_b:.2%}")
```

**Output:**

```text
Model A conversion rate: 12.50%
Model B conversion rate: 13.80%
```

Model B looks better, but is a 1.3 percentage point difference real, or could it be random noise? That's what the test answers.

### Run a two-proportion z-test

```python
z_stat, p_value = proportions_ztest(clicks, served)

print(f"Z-statistic: {z_stat:.4f}")
print(f"P-value: {p_value:.6f}")
```

### Make the decision

```python
alpha = 0.05

if p_value < alpha:
    print('Reject the null hypothesis: Model B performs significantly better. Promote it to champion.')
else:
    print('Fail to reject the null hypothesis: keep Model A as champion.')
```

The p-value comes out around 0.007, well below 0.05. The test itself only says the two rates are significantly *different*; combined with Model B's higher rate, that means B's improvement is real.

The z-statistic prints as about -2.72. It's negative because `proportions_ztest` computes A minus B, and A's rate is lower. Only its size matters for the p-value.

:::note
The null hypothesis here is "both models have the same click rate." See [inferential statistics](./inferential_statistics.md) for how hypothesis tests and p-values work.
:::

## Z-tests

A **z-test** is a hypothesis test that checks whether two population means (or proportions) are significantly different. It's the test used in the example above.

### When to use a z-test

- The sample size is large (typically $n \ge 30$).
- The population variance is known, or can be estimated accurately thanks to a large sample (via the Central Limit Theorem).
- The test statistic follows a standard normal distribution (mean 0, standard deviation 1).

### Calculating a z-test by hand

`proportions_ztest` does this for you, but here's the same calculation step by step. It computes B minus A, so the z-score comes out positive (about 2.72):

```python
import numpy as np
from scipy import stats

count_a, n_a = 1250, 10000
count_b, n_b = 1380, 10000

# Sample proportions
p_a = count_a / n_a
p_b = count_b / n_b

# Pooled proportion, assuming the null hypothesis (no difference) is true
p_pooled = (count_a + count_b) / (n_a + n_b)

# Standard error of the difference
se = np.sqrt(p_pooled * (1 - p_pooled) * (1 / n_a + 1 / n_b))

# Z-score: how many standard errors apart the two rates are
z_score = (p_b - p_a) / se

# Two-tailed p-value
p_val = 2 * (1 - stats.norm.cdf(abs(z_score)))

print(f"Z-score: {z_score:.4f}")
print(f"P-value: {p_val:.6f}")
```

### Z-test vs. t-test

| Feature | Z-test | T-test |
|---------|--------|--------|
| **Sample size** | Large ($n \ge 30$) | Small ($n < 30$) |
| **Population variance** | Known, or well estimated from a large sample | Unknown, estimated from the sample |
| **Distribution** | Standard normal | Student's t (heavier tails) |
| **Typical use** | Conversion rates and click rates with lots of traffic | Comparing means from small experiments |

**Rule of thumb:** For A/B tests on live traffic with thousands of users, a z-test is the standard choice. With small samples, use a t-test.

## Common mistakes

### Peeking and stopping early

Checking the p-value every hour and stopping as soon as it drops below 0.05 greatly increases the chance of a false positive. Decide your sample size before the test starts, and analyze the results once it's reached.

### Splitting traffic unevenly or non-randomly

If Model B only serves weekend traffic, or only new users, you're comparing groups, not models. Assign users to A or B at random.

### Declaring a winner without a meaningful difference

A statistically significant 0.05% lift may not be worth the cost of deploying a new model. Decide in advance what size of improvement matters to the business.

## Summary

- A/B testing randomly splits traffic between two versions and compares a key metric.
- For ML models, the champion-challenger setup tests a new model against the current one on live traffic.
- A two-proportion z-test tells you whether a difference in rates is statistically significant.
- Use a z-test for large samples and a t-test for small ones.

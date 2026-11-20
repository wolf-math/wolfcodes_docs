---
title: Inferential Statistics
sidebar_position: 1
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What is inferential statistics?

**Descriptive statistics** summarize the data you already have: averages, ranges, counts. **Inferential statistics** go a step further. They let you draw conclusions about a larger **population** based on a limited **sample**, test assumptions, and measure how confident you can be in the result.

## Why this matters

In data science and machine learning, inferential statistics answer the question "is this real, or just luck?" They power:

- **Feature selection**: Which features have a statistically significant relationship with the target?
- **Model validation**: Is the new model's improvement genuine, or just random chance?
- **A/B testing**: Did a change to an app, algorithm, or product really change user behavior? See [A/B testing](./ab_testing.md).

## Hypothesis testing

**Hypothesis testing** is a structured way to make decisions with data. You set up two competing statements:

- **Null hypothesis ($H_0$)**: There is no effect, difference, or relationship. For example: "The new model does *not* improve conversion rates compared to the old one."
- **Alternative hypothesis ($H_a$ or $H_1$)**: There *is* an effect. For example: "The new model significantly improves conversion rates."

You then collect data and ask whether it's surprising enough to reject the null hypothesis.

### Type I and Type II errors

Any test can get it wrong in two ways:

- **Type I error ($\alpha$)**: Rejecting the null hypothesis when it's actually true. A **false positive**: you think the new model is better, but it isn't.
- **Type II error ($\beta$)**: Failing to reject the null hypothesis when it's actually false. A **false negative**: the new model really is better, but you missed it.

### P-values

The **p-value** measures the strength of evidence against the null hypothesis. It's the probability of seeing results at least as extreme as yours, *assuming the null hypothesis is true*.

You compare it to a **significance level** $\alpha$ chosen in advance (commonly $\alpha = 0.05$):

- If $p \le \alpha$: reject $H_0$. The result is **statistically significant**.
- If $p > \alpha$: fail to reject $H_0$. You don't have enough evidence of an effect.

:::note
In machine learning, p-values often show up in feature selection. Linear regression summaries from libraries like `statsmodels` report a p-value for each coefficient, telling you whether that feature's effect is significantly different from zero.
:::

### Example: comparing two models with a t-test

Suppose you want to know whether Model B responds faster than Model A. An **independent two-sample t-test** compares the means of two groups.

```python
import numpy as np
from scipy import stats

# Simulated response times (ms) for two models
np.random.seed(42)
model_a_latency = np.random.normal(loc=45.0, scale=5.0, size=100)
model_b_latency = np.random.normal(loc=42.5, scale=4.8, size=100)

t_stat, p_value = stats.ttest_ind(model_a_latency, model_b_latency)

print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print('Reject the null hypothesis: the latency difference is significant.')
else:
    print('Fail to reject the null hypothesis: no significant difference found.')
```

## Confidence intervals

A single number like "my model has 85% accuracy" only describes performance on one particular test set. Split the data differently and that number would change. A **confidence interval (CI)** gives a *range* of values that likely contains the true value, such as the model's real-world accuracy.

### What a 95% confidence interval means

If you repeated your sampling many times and built a confidence interval each time, about 95% of those intervals would contain the true value.

The width of the interval comes from the **margin of error**, which is calculated from the standard error and a critical value from the t-distribution or z-distribution.

### Why confidence intervals matter

1. **They account for sampling variability.** Your score depends on which examples landed in your test set; the interval shows how much it could reasonably move.
2. **They help compare models.** If Model A scores 86% and Model B scores 84%, are they really different? If their confidence intervals overlap heavily, the gap may just be noise.
3. **They communicate risk.** "Accuracy is between 81% and 89% with 95% confidence" tells stakeholders far more than a single optimistic number.

### Example: a confidence interval for model accuracy

Here's a 95% confidence interval for a model's mean accuracy across 30 cross-validation folds:

```python
import numpy as np
from scipy import stats

cv_accuracies = np.array([
    0.85, 0.88, 0.82, 0.89, 0.87, 0.86, 0.90, 0.84, 0.85, 0.88,
    0.86, 0.87, 0.83, 0.91, 0.86, 0.85, 0.89, 0.88, 0.84, 0.87,
    0.86, 0.88, 0.85, 0.89, 0.87, 0.86, 0.90, 0.85, 0.88, 0.86,
])

mean_acc = np.mean(cv_accuracies)
n = len(cv_accuracies)
std_err = stats.sem(cv_accuracies)  # Standard error of the mean

ci_lower, ci_upper = stats.t.interval(0.95, df=n - 1, loc=mean_acc, scale=std_err)

print(f"Mean accuracy: {mean_acc:.4f}")
print(f"95% confidence interval: ({ci_lower:.4f}, {ci_upper:.4f})")
```

:::note
Treat this interval as a rough guide. Cross-validation folds share most of their training data, so their scores aren't fully independent, and the interval comes out narrower than it should be.
:::

:::tip
When you can't assume a particular distribution, [bootstrapping](./bootstrapping.md) is another way to build a confidence interval.
:::

## F-tests

The **F-value** (or F-statistic) is a ratio of variances. It compares the variation your model or groups *explain* to the variation left over as random noise. A larger F-value means more of the variation is explained, which suggests a real effect.

### How the F-value and p-value relate

The F-value and p-value are two views of the same test:

1. **Map it to a distribution**: Once you calculate an F-value, you locate it on an F-distribution curve (whose shape depends on sample size and degrees of freedom).
2. **They move in opposite directions**: A large F-value lands far out in the tail of the curve, leaving very little probability beyond it, so the p-value is tiny.
3. **Make the decision**:
   - Large F-value → tiny p-value → reject the null hypothesis. The effect is significant.
   - Small F-value → large p-value → fail to reject the null hypothesis. Differences are likely noise.

### Where F-tests are used

- **One-way ANOVA (analysis of variance)**: Tests whether the means of three or more groups differ significantly.
- **Overall significance in linear regression**: Tests whether at least one feature has a non-zero coefficient, compared to a model with only an intercept.
- **Feature selection**: scikit-learn's `f_classif` and `f_regression` score each feature by its linear relationship with the target.

### Example: one-way ANOVA

Suppose you've trained three model architectures and want to know whether their mean accuracies really differ:

```python
from scipy import stats

model_a = [0.85, 0.88, 0.86, 0.89, 0.87]
model_b = [0.91, 0.90, 0.93, 0.92, 0.91]
model_c = [0.78, 0.80, 0.79, 0.82, 0.81]

f_stat, p_value = stats.f_oneway(model_a, model_b, model_c)

print(f"F-statistic: {f_stat:.4f}")
print(f"P-value: {p_value:.4e}")

if p_value < 0.05:
    print('Reject the null hypothesis: the models perform differently.')
else:
    print('Fail to reject the null hypothesis: no significant difference.')
```

### Example: regression F-test

In linear regression, the F-statistic tells you whether your features *collectively* explain a significant amount of the target's variance:

```python
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

np.random.seed(42)
n = 100
x1 = np.random.randn(n)
x2 = np.random.randn(n)
y = 3 * x1 + 2 * x2 + np.random.randn(n)  # y depends on x1 and x2 plus noise

df = pd.DataFrame({'y': y, 'x1': x1, 'x2': x2})

# Fit an ordinary least squares (OLS) model
model = smf.ols('y ~ x1 + x2', data=df).fit()

print(model.summary())  # Full report, including per-feature p-values
print(f"\nF-statistic: {model.fvalue:.4f}")
print(f"F-test p-value: {model.f_pvalue:.4e}")
```

## Common mistakes

### Reading the p-value as the probability the null is true

A p-value of 0.03 does **not** mean "there's a 3% chance the models are the same." It means: *if* the models were the same, results this extreme would happen about 3% of the time.

### Confusing "significant" with "important"

With enough data, even a tiny, meaningless difference becomes statistically significant. Always look at the size of the effect (and its confidence interval), not just the p-value.

### Testing many things and reporting the winner

Run 20 tests at $\alpha = 0.05$ and you should expect about one "significant" result by pure chance. If you test many features or models, account for it, or confirm the winner on fresh data.

## Summary

- Inferential statistics let you generalize from a sample to a population and judge whether results are real.
- Hypothesis tests compare a null hypothesis (no effect) against an alternative; the p-value measures the evidence against the null.
- Confidence intervals report a range instead of a single number, which makes model comparisons honest.
- F-tests compare explained variance to noise, and are used in ANOVA, regression, and feature selection.

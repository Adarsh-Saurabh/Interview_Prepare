# 02: Machine Coding & ML Pipeline

In Technical Round 1, Swiggy assesses mathematical rigor in ML theory, custom scikit-learn transformers, and low-level understanding of Gradient Boosted Decision Trees.

---

## 1. End-to-End Production ETA Regressor with Quantile Loss

Swiggy provides customers with a delivery window (e.g. "30–40 mins") rather than a single point estimate. This requires **Quantile Regression (Pinball Loss)**:

$$L_q(y, \hat{y}) = \max(q(y - \hat{y}), (1-q)(\hat{y} - y)) = (y - \hat{y})(q - \mathbb{I}_{y < \hat{y}})$$

For $q = 0.10$ (10th percentile, lower bound) and $q = 0.90$ (90th percentile, upper bound), the interval $[\hat{y}_{0.1}, \hat{y}_{0.9}]$ gives an empirical 80% confidence interval.

```python
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
import lightgbm as lgb
from sklearn.metrics import mean_pinball_loss, mean_absolute_error

class SwiggyFeatureEngineering(BaseEstimator, TransformerMixin):
    """
    Production feature pipeline:
    - Cyclical encoding of hour of day and day of week.
    - Haversine distance computation between DE, Restaurant, and Customer.
    - Smoothed Target Encoding for Restaurant IDs with empirical Bayes shrinkage.
    """
    def __init__(self, smoothing_weight=10.0):
        self.smoothing_weight = smoothing_weight
        self.restaurant_stats_ = {}
        self.global_mean_ = 0.0

    def fit(self, X, y):
        df = X.copy()
        df['target'] = y
        self.global_mean_ = float(y.mean())
        
        # Smoothed target encoding: S_i = (n_i * mean_i + m * global_mean) / (n_i + m)
        stats = df.groupby('restaurant_id')['target'].agg(['count', 'mean'])
        smooth = (stats['count'] * stats['mean'] + self.smoothing_weight * self.global_mean_) / (stats['count'] + self.smoothing_weight)
        self.restaurant_stats_ = smooth.to_dict()
        return self

    def transform(self, X):
        df = X.copy()
        
        # Cyclical temporal features
        hour = df['order_hour'].values
        df['hour_sin'] = np.sin(2 * np.pi * hour / 24.0)
        df['hour_cos'] = np.cos(2 * np.pi * hour / 24.0)
        
        dow = df['order_dow'].values
        df['dow_sin'] = np.sin(2 * np.pi * dow / 7.0)
        df['dow_cos'] = np.cos(2 * np.pi * dow / 7.0)
        
        # Vectorized Haversine distance
        lat1, lon1 = np.radians(df['rest_lat']), np.radians(df['rest_lon'])
        lat2, lon2 = np.radians(df['cust_lat']), np.radians(df['cust_lon'])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = np.sin(dlat / 2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0)**2
        c = 2 * np.arcsin(np.sqrt(a))
        df['haversine_km'] = 6371.0 * c
        
        # Apply target encoding
        df['rest_encoded_duration'] = df['restaurant_id'].map(self.restaurant_stats_).fillna(self.global_mean_)
        
        feature_cols = [
            'haversine_km', 'hour_sin', 'hour_cos', 'dow_sin', 'dow_cos',
            'rest_encoded_duration', 'kitchen_active_orders', 'rain_mm_per_hr'
        ]
        return df[feature_cols].values

class SwiggyQuantileETAPipeline:
    def __init__(self, quantiles=[0.1, 0.5, 0.9]):
        self.quantiles = quantiles
        self.fe = SwiggyFeatureEngineering()
        self.models = {}

    def fit(self, X_train, y_train):
        features = self.fe.fit_transform(X_train, y_train)
        
        for q in self.quantiles:
            reg = lgb.LGBMRegressor(
                objective='quantile',
                alpha=q,
                n_estimators=300,
                learning_rate=0.05,
                num_leaves=31,
                random_state=42,
                n_jobs=-1
            )
            reg.fit(features, y_train)
            self.models[q] = reg

    def predict_interval(self, X_test):
        features = self.fe.transform(X_test)
        preds = {}
        for q, model in self.models.items():
            preds[f'p{int(q*100)}'] = model.predict(features)
        return pd.DataFrame(preds)
```

---

## 2. Gradient Boosted Trees: Mathematical Split Derivation (XGBoost)

During technical grilling, Swiggy interviewers demand exact derivations of tree split criteria.

### Objective Function with Second-Order Taylor Expansion
Given training dataset $\mathcal{D} = \{(x_i, y_i)\}$, at step $t$, the objective is:
$$\mathcal{L}^{(t)} = \sum_{i=1}^n l(y_i, \hat{y}_i^{(t-1)} + f_t(x_i)) + \Omega(f_t)$$
Where tree complexity penalty is:
$$\Omega(f_t) = \gamma T + rac{1}{2}\lambda \sum_{j=1}^T w_j^2$$
Expanding $l(y_i, \hat{y}_i^{(t-1)} + f_t(x_i))$ via 2nd-order Taylor series around $\hat{y}_i^{(t-1)}$:
$$l(y_i, \hat{y}_i^{(t-1)} + f_t(x_i)) pprox l(y_i, \hat{y}_i^{(t-1)}) + g_i f_t(x_i) + rac{1}{2}h_i f_t^2(x_i)$$
Where:
$$g_i = rac{\partial l(y_i, \hat{y}^{(t-1)})}{\partial \hat{y}^{(t-1)}}, \quad h_i = rac{\partial^2 l(y_i, \hat{y}^{(t-1)})}{\partial (\hat{y}^{(t-1)})^2}$$

Removing constant terms:
$$	ilde{\mathcal{L}}^{(t)} = \sum_{j=1}^T \left[ \left(\sum_{i \in I_j} g_iight) w_j + rac{1}{2}\left(\sum_{i \in I_j} h_i + \lambdaight) w_j^2 ight] + \gamma T$$
Defining $G_j = \sum_{i \in I_j} g_i$ and $H_j = \sum_{i \in I_j} h_i$:
$$	ilde{\mathcal{L}}^{(t)} = \sum_{j=1}^T \left[ G_j w_j + rac{1}{2}(H_j + \lambda) w_j^2 ight] + \gamma T$$

### Optimal Leaf Weight $w_j^*$
Taking derivative with respect to $w_j$ and setting to zero:
$$rac{\partial 	ilde{\mathcal{L}}^{(t)}}{\partial w_j} = G_j + (H_j + \lambda)w_j = 0 \implies w_j^* = -rac{G_j}{H_j + \lambda}$$

Substituting $w_j^*$ back gives the minimum loss for fixed structure:
$$\mathcal{L}^* = -rac{1}{2}\sum_{j=1}^T rac{G_j^2}{H_j + \lambda} + \gamma T$$

### Tree Split Evaluation Gain Formula
When considering splitting a leaf into Left ($L$) and Right ($R$) subsets:
$$	ext{Gain} = rac{1}{2}\left[ rac{G_L^2}{H_L + \lambda} + rac{G_R^2}{H_R + \lambda} - rac{(G_L + G_R)^2}{H_L + H_R + \lambda} ight] - \gamma$$
If $	ext{Gain} \le 0$, the split is pruned.

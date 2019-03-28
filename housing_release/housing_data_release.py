import os
import tarfile
from six.moves import urllib
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import Imputer, StandardScaler
from sklearn.preprocessing import LabelBinarizer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor


DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "/housing.tgz"
rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    """Fetch the data"""
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path,"housing.tgz")  # 本地保存tgz文件的路径
    urllib.request.urlretrieve(housing_url,tgz_path)  # 将远程url的数据请求到本地
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path = housing_path)  # 解压文件到  "datasets/housing" 下
    housing_tgz.close()


def load_housing_data(housing_path=HOUSING_PATH):
    """Load the data"""
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):  # 这里定义超参数是否开启
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self  # nothing else to do

    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
        population_per_household = X[:, population_ix] / X[:, household_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]


class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.attribute_names].values


class PipelineFriendlyLabelBinarizer(LabelBinarizer):
    """overrides the method"""
    def fit_transform(self, X, y=None):
        return super(PipelineFriendlyLabelBinarizer, self).fit_transform(X)


def get_rmse_value(m_label, m_prediction):
    return np.sqrt(mean_squared_error(m_label, m_prediction))


def display_scores(scores):
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard deviation:", scores.std())


def my_linear_regression(m_prepared, m_labels):
    lin_reg = LinearRegression()
    lin_reg.fit(m_prepared, m_labels)

    m_predictions = lin_reg.predict(m_prepared)
    lin_rmse = get_rmse_value(m_labels, m_predictions)
    print("lin_rmse:\t", lin_rmse)

    lin_socres = cross_val_score(lin_reg, m_prepared, m_labels, scoring="neg_mean_squared_error", cv=10)
    lin_rmse_scores = np.sqrt(-lin_socres)
    display_scores(lin_rmse_scores)

    # some_data = housing.iloc[:5]
    # some_labels = housing_labels.iloc[:5]
    # some_data_prepared = full_pipeline.transform(some_data)  # 准备少量数据做测试用
    # print("Predictions:\t", lin_reg.predict(some_data_prepared))
    # print("Labels:\t\t", list(some_labels))


def my_decisiontreeRegressor(m_prepared, m_labels):
    tree_reg = DecisionTreeRegressor()
    tree_reg.fit(m_prepared, m_labels)

    my_predictions = tree_reg.predict(m_prepared)
    tree_rmse = get_rmse_value(m_labels, my_predictions)
    print("tree_rmse\t", tree_rmse)

    tree_socres = cross_val_score(tree_reg, m_prepared, m_labels, scoring="neg_mean_squared_error", cv=10)
    tree_rmse_scores = np.sqrt(-tree_socres)
    display_scores(tree_rmse_scores)


def my_random_forest_regressor(m_prepared, m_labels):
    forest_reg = RandomForestRegressor()
    forest_reg.fit(m_prepared, m_labels)

    my_predictions = forest_reg.predict(m_prepared)
    forest_rmse = get_rmse_value(m_labels, my_predictions)
    print("tree_rmse\t", forest_rmse)

    forest_socres = cross_val_score(forest_reg, m_prepared, m_labels, scoring="neg_mean_squared_error", cv=10)
    forest_rmse_scores = np.sqrt(-forest_socres)
    display_scores(forest_rmse_scores)




if __name__ == '__main__':
    fetch_housing_data()
    housing = load_housing_data()

    housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
    housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        strat_train_set = housing.loc[train_index]
        strat_test_set = housing.loc[test_index]

    for set in (strat_train_set, strat_test_set):
        set.drop(["income_cat"], axis=1, inplace=True)  # 分类之后，该特征值就没有什么用处了

    housing = strat_train_set.copy()
    housing = strat_train_set.drop("median_house_value", axis=1)
    housing_labels = strat_train_set["median_house_value"].copy()

    housing_num = housing.drop("ocean_proximity", axis=1)

    num_attribs = list(housing_num)
    print(num_attribs)
    cat_attribs = ["ocean_proximity"]

    num_pipeline = Pipeline([
        ('selector', DataFrameSelector(num_attribs)),
        ('imputer', Imputer(strategy="median")),
        ('attribs_adder', CombinedAttributesAdder()),
        ('std_scaler', StandardScaler()),
    ])

    cat_pipeline = Pipeline([
        ('selector', DataFrameSelector(cat_attribs)),
        ('label_binarizer', PipelineFriendlyLabelBinarizer()),
    ])

    full_pipeline = FeatureUnion(transformer_list=[
        ("num_pipeline", num_pipeline),
        ("cat_pipeline", cat_pipeline),
    ])

    housing_prepared = full_pipeline.fit_transform(housing)
    print(housing_prepared)
    print(housing_prepared.shape)
# LinearRegression
    # my_linear_regression(housing_prepared, housing_labels)
# DecisionTreeRegressor
    # my_decisiontreeRegressor(housing_prepared, housing_labels)
# RandomForestRegressor
    my_random_forest_regressor(housing_prepared, housing_labels)

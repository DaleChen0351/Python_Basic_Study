import matplotlib.pyplot as plt
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, Imputer

def show_data_histgram(mdata):
    mdata.hist(bins=50, figsize=(10, 8))  #
    plt.show()


class CsvDataClass(object):
    def __init__(self, data):
        self.data = data

    def print_info(self):
        print(self.data.info())

    def print_head(self, head_num=5):
        print(self.data.head(head_num))

    def print_describe(self):
        print(self.data.describe())


def print_value_counts(mdata, attr):
    print(mdata[attr].value_counts() / len(mdata))


def visualizing_data(mhousing):
    mhousing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
                 s=mhousing["population"] / 100, label="population",
                 c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,
                 )
    plt.legend()
    plt.show()


def calcu_corr(mdata, attr):
    corr_matrix = mdata.corr()
    print(corr_matrix[attr].sort_values(ascending=False))


rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6


class CombinedAttributeAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):  # 这里定义超参数是否开启
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self):
        return self

    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
        population_per_household = X[:, population_ix] / X[:, household_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]


num_pipline = Pipeline([
    ("imputer", Imputer(strategy="median")),
    ("attribs_adder", CombinedAttributeAdder()),
    ("std_scaler", StandardScaler()),
])

housing_num_tr = num_pipline.fit_transform(housing_num)
import os
import tarfile
from six.moves import urllib
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import train_test_split
from show_calcu_housing_data import calcu_corr, show_data_histgram, print_value_counts, visualizing_data,CombinedAttributeAdder
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelBinarizer



DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "/housing.tgz"


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


if __name__ == '__main__':
    fetch_housing_data()
    housing = load_housing_data()

    # show_data_histgram(housing)
    # train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

    housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
    housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        strat_train_set = housing.loc[train_index]
        strat_test_set = housing.loc[test_index]

    # print_value_counts(housing, "income_cat")
    # print_value_counts(strat_test_set, "income_cat")

    for set in (strat_train_set, strat_test_set):
        set.drop(["income_cat"], axis=1, inplace=True)  # 分类之后，该特征值就没有什么用处了

# Discover and Visualize the Data to Gain Insights
    housing = strat_train_set.copy()
    # visualizing_data(housing)
    # calcu_corr(housing, "median_house_value")

# transformation and combination
    housing["rooms_per_household"] = housing["total_rooms"] / housing["households"]
    housing["bedrooms_per_room"] = housing["total_bedrooms"] / housing["total_rooms"]
    housing["population_per_household"] = housing["population"] / housing["households"]
    # calcu_corr(housing, "median_house_value")

# separate the predictors and the labels
    housing = strat_train_set.drop("median_house_value", axis=1)
    housing_labels = strat_train_set["median_house_value"].copy()

# fill the missing features(numbers)
    housing_num = housing.drop("ocean_proximity", axis=1)
    imputer = Imputer(strategy="median")
    imputer.fit(housing_num)
    X = imputer.transform(housing_num)
    housing_tr = pd.DataFrame(X, columns=housing_num.columns)

# Handling Text and Categorical Attributes(labels)

    housing_cat = housing["ocean_proximity"]
    # # 一般编码
    # encoder = LabelEncoder()
    # housing_cat_encoded = encoder.fit_transform(housing_cat)
    # print(housing_cat_encoded)
    # #  one-hot encoder
    # encoder = OneHotEncoder()
    # housing_cat_1hot = encoder.fit_transform(housing_cat_encoded.reshape(-1, 1)) # ?
    # print(housing_cat_1hot)

    # 合二为一
    encoder = LabelBinarizer()  # get a sparse matrix instead by passing sparse_output=True to the LabelBinarizer
    housing_cat_1hot = encoder.fit_transform(housing_cat)
    # print(housing_cat_1hot)  # returns a dense NumPy array

    attr_adder = CombinedAttributeAdder(add_bedrooms_per_room=True)
    housing_extra_attribs = attr_adder.transform(housing.values)
    print(attr_adder.get_params())  # 获取超参数的值


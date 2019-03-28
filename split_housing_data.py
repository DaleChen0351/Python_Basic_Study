
import numpy as np
import hashlib



def simple_split_train_test(data, test_ratio):
    """
    :param data:
    :param test_ratio:
    :return:

    """
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]  # iloc 一维参数是对行取数


def split_train_test_by_id(data, test_ratio, id_column, hash=hashlib.md5):
    """
    :param data: DataFrame which got from a CSV file before
    :param test_ratio: ratio value
    :param id_column:
    :param hash: hash 算法
    :return: test_set and train_set that all built as type of DataFrame

    :采用index作为ID
    house_with_id = housing.reset_index()  # housing 基础上增加了一列index
    train_set, test_set = split_train_test_by_id(house_with_id, 0.2, "index")

    :采用精度和维度作为ID
    housing_with_id["id"] = housing["longitude"] * 1000 + housing["latitude"]
    train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "id")
    """
    def test_set_check(identifier, test_ratio, hash):
        """
        计算HASH值
        :param identifier:
        :param test_ratio:
        :param hash:
        :return:
        """
        return hash(np.int64(identifier)).digest()[-1] < 256 * test_ratio
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
    return data.loc[~in_test_set], data.loc[in_test_set]  # 生成一个序列，按照序列中True和False 对行（样本）进行筛选
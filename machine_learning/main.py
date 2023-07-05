from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import jieba


def datasets_demo():
    """
    sklearn数据集的使用
    :return:
    """
    # 获取数据集
    iris = load_iris()
    print("鸢尾花数据集：\n", iris)
    print("产看数据集描述\n", iris["DESCR"])

    # 数据集划分
    # 训练集特征值，测试集特征值，训练集目标值，测试集目标值
    x_train, x_test, y_train, t_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)
    print("训练集的特征值:\n", x_train, x_train.shape)

    return None


def dict_demo():
    """
    字典特征提取
    :return:
    """
    data = [{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 60},
            {'city': '深圳', 'temperature': 30}]
    # 1.实例化一个转换器类
    # separator稀疏矩阵(将非零值按位置表示)
    transfer = DictVectorizer(sparse=False)
    # 2.调用fit_transform()
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new)
    print("特征名字：\n", transfer.get_feature_names_out())

    return None


def count_demo():
    """
    文本特征抽取:CountVecotrizer
    :return:
    """
    data = ["life is short,i like like python", "life is too long,i dislike python"]
    # 1.实例化一个转换器类
    # stop_words停用词
    transfer = CountVectorizer()
    # 2、调用fit_transform
    data_new = transfer.fit_transform(data)
    # 采用toarray()还原separator稀疏矩阵
    print("data_new:\n", data_new.toarray())
    print("特征名字：\n", transfer.get_feature_names_out())
    return None


def count_chinese_demo():
    """
    中文文本特征抽取，自动分词
    :return:
    """

    data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]
    # 将中文文本进行分词
    data_new = []
    for sent in data:
        data_new.append(" ".join(list(jieba.cut(sent))))  # 将sent列表用“ ”连接起来
    # print(data_new)
    # 1、实例化一个转换器类
    transfer = CountVectorizer(stop_words=["一种", "所以"])

    # 2、调用fit_transform
    data_final = transfer.fit_transform(data_new)
    print("data_new:\n", data_final.toarray())
    print("特征名字：\n", transfer.get_feature_names_out())

    return None


def tfidf_demo():
    """
    用TF-IDF的方法进行文本特征抽取->关键词：本文章多，别的文章少的词
    :return:
    """
    # 将中文文本进行分词
    data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]

    data_new = []
    for sent in data:
        data_new.append(" ".join(list(jieba.cut(sent))))
    # print(data_new)
    # 1、实例化一个转换器类
    transfer = TfidfVectorizer(stop_words=["一种", "所以"])

    # 2、调用fit_transform
    data_final = transfer.fit_transform(data_new)
    print("data_new:\n", data_final.toarray())
    print("特征名字：\n", transfer.get_feature_names_out())

    return None
    # 将中文文本进行分词


if __name__ == "__main__":
    # 代码1: sklearn数据集的使用
    # datasets_demo()
    # 代码2: 字典特征提取
    dict_demo()
    # 代码3：文本特征抽取：CountVecotrizer
    # count_demo()
    # 代码4: 中文分词
    # count_chinese_demo()
    # 代码5: 用TF-IDF的方法进行文本特征抽取->关键词
    # tfidf_demo()

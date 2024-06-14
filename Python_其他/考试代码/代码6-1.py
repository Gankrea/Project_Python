from sklearn.datasets import load_diabetes

# 6-1
diabetes = load_diabetes()
print(f"diabetes数据集的长度为：", len(diabetes))
print(f"diabetes数据集的类型为：", type(diabetes))

# 6-2
# 获取数据集的数据
diabetes_data = diabetes['data']
print(f"diabetes的数据集为：", '\n', diabetes_data)
# 获取数据集的标签
diabetes_target = diabetes['target']
print(f"diabetes数据集的标签为：", '\n', diabetes_target)
# 获取数据集的特征名
diabetes_names = diabetes['feature_names']
print(f"diabetes数据集的特征名为：", '\n', diabetes_names)
# 获取数据集的描述信息
diabetes_desc = diabetes['DESCR']
print(f"diabetes数据集的描述信息为：", " \n", diabetes_desc)

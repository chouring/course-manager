# 类，数据结构和算法的轮子实现

import json


class Student():
    id = -1
    pwd = ""
    name = ""
    class_id = -1
    courses = []
    activities = []

    def __init__(self, id, pwd, name, class_id, courses, activities):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.class_id = class_id
        self.courses = courses
        self.activities = activities


# ----------数据结构
# datas/information.txt 每行存储1个学生信息，利用Python文件操作每次读取一行，利用json包实现 字符串/Python dict/json的转换


# 根据id和pwd查找学生，找到返回一个json对象
def search_stu_by_id_and_pwd(rid, rpwd):
    f = open('datas/information.txt', 'r', encoding="utf-8")
    lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        obj = json.loads(lines[i])
        if obj['id'] == rid and obj['pwd'] == rpwd:
            return obj
    return {}

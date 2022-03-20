# 主模块，学生/管理员的信息，活动的增删改查

import json
from flask import Flask, render_template, request

# navigate和clock子模块
from nagivate import navigate
from clock import clock
app = Flask(__name__, template_folder='templates')
app.register_blueprint(navigate, url_prefix='/navigate')
app.register_blueprint(clock, url_prefix='/clock')


# 导入一些轮子
from src import Student
from src import search_stu_by_id_and_pwd


# 初始页面
@app.route('/')
def welcome():
    return render_template('welcome.html')


# 注册
@app.route('/register', methods=['POST'])
def register():
    rid = request.form['id']
    rpwd = request.form['pwd']
    rname = request.form['name']
    class_id = request.form['class_id']
    obj = Student(rid, rpwd, rname, class_id, [], [])
    data2 = json.dumps(obj.__dict__, ensure_ascii=False)
    f = open('datas/information.txt', 'a', encoding="utf-8")
    f.write(data2 + '\n')
    f.close()
    return render_template('stu_menu.html', id=rid, pwd=rpwd, name=rname)


# 登录
@app.route('/login', methods=['POST'])
def login():
    rid = request.form['id']
    rpwd = request.form['pwd']
    stu = search_stu_by_id_and_pwd(rid, rpwd)
    if stu != {}:
        return render_template('stu_menu.html', id=rid, pwd=rpwd, name=stu['name'])
    return render_template('opt_res.html', res="登录失败，输入错误或该账号不存在")


# 学生展示课程
@app.route('/to_show_course', methods=['POST'])
def show_course():
    stu = search_stu_by_id_and_pwd(request.form['id'], request.form['pwd'])
    return render_template('show_course.html', array=stu['courses'])


# 学生添加课程-默认
@app.route('/to_add_course', methods=['POST'])
def add_course_default():
    return render_template('add_course.html', id=request.form['id'], pwd=request.form['pwd'])


# 学生添加课程-操作
@app.route('/add_course', methods=['POST'])
def add_course():
    flag = False
    rid = request.form['id']
    rpwd = request.form['pwd']
    f = open('datas/information.txt', 'r', encoding="utf-8")
    lines = f.readlines()
    f.close()
    res = "添加失败"
    for i in range(len(lines)):
        obj = json.loads(lines[i])
        if obj['id'] == rid and obj['pwd'] == rpwd:
            course_id = request.form['course_id']
            course_name = request.form['course_name']
            begin_time = request.form['begin_time']
            end_time = request.form['end_time']
            item = {
                'course_id': course_id,
                'course_name': course_name,
                'begin_time': begin_time,
                'end_time': end_time
            }
            obj['courses'].append(item)
            lines[i] = json.dumps(obj, ensure_ascii=False) + '\n'
            flag = True
            break
    if flag:
        f = open('datas/information.txt', 'w', encoding="utf-8")
        f.writelines(lines)
        f.close()
        res = "添加成功"
    return render_template('opt_res.html', res=res)


@app.route('/to_delete_course', methods=['POST'])
def to_delete_course():
    return render_template('delete_course.html', id=request.form['id'], pwd=request.form['pwd'])


@app.route('/delete_course', methods=['POST'])
def delete_course():
    flag = False
    res = "删除失败"
    rid = request.form['id']
    rpwd = request.form['pwd']
    rcourse_id = request.form['course_id']
    rcourse_name = request.form['course_name']
    f = open('datas/information.txt', 'r', encoding="utf-8")
    lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        obj = json.loads(lines[i])
        if obj['id'] == rid and obj['pwd'] == rpwd:
            arr = obj['courses']
            for j in range(len(arr)):
                if arr[j]['course_id'] == rcourse_id and arr[j]['course_name'] == rcourse_name:
                    del obj['courses'][j]
                    lines[i] = json.dumps(obj, ensure_ascii=False) + '\n'
                    flag = True
                    break
    if flag:
        f = open('datas/information.txt', 'w', encoding="utf-8")
        f.writelines(lines)
        f.close()
        res = "删除成功"
    return render_template('opt_res.html', res=res)






if __name__ == '__main__':
    app.run()


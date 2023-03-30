from flask import (
    render_template,
    request,
    current_app as app,
    session,
    flash,
    redirect,
)
import sqlite3
from function import hash_code
from pathlib import Path

from exts import db
from models import Gender_pay
from sqlalchemy import func
from schema import GenderPay
from statistics import median

PROJECT_ROOT = Path(__file__).parent

Gender_schema = GenderPay(many=True)


def get_median_by_field(query_result, field_name):
    # 获取所有符合条件的字段值
    field_values = [getattr(item, field_name) for item in query_result]
    # 计算中位数
    return median(field_values)


def get_Average(field_type, value):
    # 使用select语句和func对象计算平均值和中位数
    from sqlalchemy import func

    # 根据 Region 和 Industry 和 EmployerSize 字段值为条件，查询各列的平均值
    max_avg = Gender_pay.query.filter_by(**{field_type: value}).with_entities(
        func.avg(Gender_pay.DiffMeanHourlyPercent),
        func.avg(Gender_pay.DiffMedianHourlyPercent),
        func.avg(Gender_pay.DiffMeanBonusPercent),
        func.avg(Gender_pay.DiffMedianBonusPercent),
        func.avg(Gender_pay.MaleBonusPercent),
        func.avg(Gender_pay.FemaleBonusPercent),
        func.avg(Gender_pay.MaleLowerQuartile),
        func.avg(Gender_pay.FemaleLowerQuartile),
        func.avg(Gender_pay.MaleLowerMiddleQuartile),
        func.avg(Gender_pay.FemaleLowerMiddleQuartile),
        func.avg(Gender_pay.MaleUpperMiddleQuartile),
        func.avg(Gender_pay.FemaleUpperMiddleQuartile),
        func.avg(Gender_pay.MaleTopQuartile),
        func.avg(Gender_pay.FemaleTopQuartile),
        func.avg(Gender_pay.EmployerSizeMedian),
    ).all()
    return max_avg


def get_madian(field_type, value):
    query_result = Gender_pay.query.filter_by(**{field_type: value}).all()
    diff_mean_hourly_percent_median = get_median_by_field(query_result=query_result, field_name="DiffMeanHourlyPercent")
    diff_median_hourly_percent_median = get_median_by_field(query_result=query_result,
                                                            field_name="DiffMedianHourlyPercent")
    diff_mean_bonus_percent_median = get_median_by_field(query_result=query_result, field_name="DiffMeanBonusPercent")
    diff_median_bonus_percent_median = get_median_by_field(query_result=query_result,
                                                           field_name="DiffMedianBonusPercent")
    male_bonus_percent_median = get_median_by_field(query_result=query_result, field_name="MaleBonusPercent")
    female_bonus_percent_median = get_median_by_field(query_result=query_result, field_name="FemaleBonusPercent")
    male_lower_quartile_median = get_median_by_field(query_result=query_result, field_name="MaleLowerQuartile")
    female_lower_quartile_median = get_median_by_field(query_result=query_result, field_name="FemaleLowerQuartile")
    male_lower_middle_quartile_median = get_median_by_field(query_result=query_result,
                                                            field_name="MaleLowerMiddleQuartile")
    female_lower_middle_quartile_median = get_median_by_field(query_result=query_result,
                                                              field_name="FemaleLowerMiddleQuartile")
    male_upper_middle_quartile_median = get_median_by_field(query_result=query_result,
                                                            field_name="MaleUpperMiddleQuartile")
    female_upper_middle_quartile_median = get_median_by_field(query_result=query_result,
                                                              field_name="FemaleUpperMiddleQuartile")
    male_top_quartile_median = get_median_by_field(query_result=query_result, field_name="MaleTopQuartile")
    female_top_quartile_median = get_median_by_field(query_result=query_result, field_name="FemaleTopQuartile")
    employer_size_median_median = get_median_by_field(query_result=query_result, field_name="EmployerSizeMedian")
    data_median = [diff_mean_hourly_percent_median,
                   diff_median_hourly_percent_median,
                   diff_mean_bonus_percent_median,
                   diff_median_bonus_percent_median,
                   male_bonus_percent_median,
                   female_bonus_percent_median,
                   male_lower_quartile_median,
                   female_lower_quartile_median,
                   male_lower_middle_quartile_median,
                   female_lower_middle_quartile_median,
                   male_upper_middle_quartile_median,
                   female_upper_middle_quartile_median,
                   male_top_quartile_median,
                   female_top_quartile_median,
                   employer_size_median_median]
    return data_median


def get_events():
    all_events = db.session.query(Gender_pay.Region, Gender_pay.Industry).distinct().all()
    event_json = Gender_schema.dump(all_events)
    return event_json


def get_event(event_id):
    event = db.session.query(getattr(Gender_pay, event_id)).distinct().all()
    result = Gender_schema.dump(event)
    return result


@app.route("/display_event/<event_id>")
def display_event(event_id):
    ev = get_event(event_id)
    print(ev)
    return render_template("index_second.html", event_second=ev)


@app.route("/display_data/<field_type>/<field_name>")
def display_data(field_type, field_name):
    print("field_name:{}".format(field_name))
    print("field_type:{}".format(field_type))
    response_avg = get_Average(field_type, field_name)
    response_median = get_madian(field_type, field_name)
    response = response_avg, response_median
    print("response:{}".format(response))
    return render_template("table.html", data_list=response)


@app.route('/')
def index():  # put application's code here
    response = get_events()
    return render_template("index.html", event_list=response)


@app.route('/index')
def home():
    response = get_events()
    return render_template("index.html", event_ist=response)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 获取请求中的数据
        username = request.form.get('username')
        password = hash_code(request.form.get('password'))

        # 连接数据库，判断用户名+密码组合是否匹配
        conn = sqlite3.connect('data/gender.db')
        cur = conn.cursor()
        try:
            # sqlite3支持?占位符，通过绑定变量的查询方式杜绝sql注入
            sql = 'SELECT 1 FROM USER WHERE USERNAME=? AND PASSWORD=?'
            is_valid_user = cur.execute(sql, (username, password)).fetchone()

            # 拼接方式，存在sql注入风险, SQL注入语句：在用户名位置填入 1 or 1=1 --
            # sql = 'SELECT 1 FROM USER WHERE USERNAME=%s AND PASSWORD=%s' % (username, password)
            # print(sql)
            # is_valid_user = cur.execute(sql).fetchone()
        except:
            flash('Wrong Username or Password！')
            return render_template('login.html')
        finally:
            conn.close()

        if is_valid_user:
            # 登录成功后存储session信息
            session['is_login'] = True
            session['name'] = username
            return redirect('/')
        else:
            flash('Wrong Username or Password！')
            return render_template('login.html')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password')
        confirm_password = request.form.get('confirm')
        # 判断所有输入都不为空
        if username and password and confirm_password:
            if password != confirm_password:
                flash('Unmatched！')
                return render_template('register.html', username=username)
            # 连接数据库
            conn = sqlite3.connect('data/gender.db')
            cur = conn.cursor()
            # 查询输入的用户名是否已经存在
            sql_same_user = 'SELECT 1 FROM USER WHERE USERNAME=?'
            same_user = cur.execute(sql_same_user, (username,)).fetchone()
            if same_user:
                flash('Username Exists！')
                return render_template('register.html', username=username)
            # 通过检查的数据，插入数据库表中
            sql_insert_user = 'INSERT INTO USER(USERNAME, PASSWORD) VALUES (?,?)'
            cur.execute(sql_insert_user, (username, hash_code(password)))
            conn.commit()
            conn.close()
            # 重定向到登录页面
            return redirect('/login')
        else:
            flash('All fields are required！')
            if username:
                return render_template('register.html', username=username)
            return render_template('register.html')
    return render_template('register.html')


@app.route('/logout')
def logout():
    # 退出登录，清空session
    if session.get('is_login'):
        session.clear()
        return redirect('/')
    return redirect('/')


@app.route('/display_alldata')
def display_alldata():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    data = Gender_pay.query.paginate(page=page, per_page=per_page, error_out=False)
    return render_template('data_table.html', data=data)

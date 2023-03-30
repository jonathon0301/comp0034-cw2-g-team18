import csv
import sqlite3

# 创建数据库连接
conn = sqlite3.connect('gender.db')
c = conn.cursor()
# 读取CSV文件并插入到表格中
with open('gender_pay_gap.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        DiffMeanHourlyPercent = row['DiffMeanHourlyPercent']
        DiffMedianHourlyPercent = row['DiffMedianHourlyPercent']
        DiffMeanBonusPercent = row['DiffMeanBonusPercent']
        DiffMedianBonusPercent = row['DiffMedianBonusPercent']
        MaleBonusPercent = row['MaleBonusPercent']
        FemaleBonusPercent = row['FemaleBonusPercent']
        MaleLowerQuartile = row['MaleLowerQuartile']
        FemaleLowerQuartile = row['FemaleLowerQuartile']
        MaleLowerMiddleQuartile = row['MaleLowerMiddleQuartile']
        FemaleLowerMiddleQuartile = row['FemaleLowerMiddleQuartile']
        MaleUpperMiddleQuartile = row['MaleUpperMiddleQuartile']
        FemaleUpperMiddleQuartile = row['FemaleUpperMiddleQuartile']
        MaleTopQuartile = row['MaleTopQuartile']
        FemaleTopQuartile = row['FemaleTopQuartile']
        EmployerSize = row['EmployerSize']
        Region = row['UK region']
        Industry = row['Industry']
        EmployerSizeMedian = row['EmployerSizeMedian']
        c.execute(
            "INSERT INTO t_Gender_pay (DiffMeanHourlyPercent, DiffMedianHourlyPercent, DiffMeanBonusPercent,DiffMedianBonusPercent,MaleBonusPercent,FemaleBonusPercent,MaleLowerQuartile,FemaleLowerQuartile,MaleLowerMiddleQuartile,FemaleLowerMiddleQuartile,MaleUpperMiddleQuartile,FemaleUpperMiddleQuartile,MaleTopQuartile,FemaleTopQuartile,EmployerSize,Region,Industry,EmployerSizeMedian) VALUES (?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?,?, ?, ?)",
            (DiffMeanHourlyPercent, DiffMedianHourlyPercent, DiffMeanBonusPercent, DiffMedianBonusPercent,
             MaleBonusPercent, FemaleBonusPercent, MaleLowerQuartile, FemaleLowerQuartile, MaleLowerMiddleQuartile,
             FemaleLowerMiddleQuartile, MaleUpperMiddleQuartile, FemaleUpperMiddleQuartile, MaleTopQuartile,
             FemaleTopQuartile, EmployerSize, Region, Industry, EmployerSizeMedian))

# 提交更改并关闭连接
conn.commit()
conn.close()

from gender_app.app import db
from sqlalchemy import Column, String, Integer


# from flask_login import UserMixin


class Gender_pay(db.Model):
    __tablename__ = 't_Gender_pay'
    id = Column(Integer, primary_key=True, autoincrement=True)
    DiffMeanHourlyPercent = Column(String(128), nullable=False)
    DiffMedianHourlyPercent = Column(String(128), nullable=False)
    DiffMeanBonusPercent = Column(String(128), nullable=False)
    DiffMedianBonusPercent = Column(String(128), nullable=False)
    MaleBonusPercent = Column(String(128), nullable=False)
    FemaleBonusPercent = Column(String(128), nullable=False)
    MaleLowerQuartile = Column(String(128), nullable=False)
    FemaleLowerQuartile = Column(String(128), nullable=False)
    MaleLowerMiddleQuartile = Column(String(128), nullable=False)
    FemaleLowerMiddleQuartile = Column(String(128), nullable=False)
    MaleUpperMiddleQuartile = Column(String(128), nullable=False)
    FemaleUpperMiddleQuartile = Column(String(128), nullable=False)
    MaleTopQuartile = Column(String(128), nullable=False)
    FemaleTopQuartile = Column(String(128), nullable=False)
    EmployerSize = Column(String(128), nullable=False)
    Region = Column(String(128), nullable=False)
    Industry = Column(String(128), nullable=False)
    EmployerSizeMedian = Column(String(128), nullable=False)

    def __repr__(self):
        """
        Returns the attributes of the event as a string
        :returns str
        """
        clsname = self.__class__.__name__
        return f"<{clsname}: {self.DiffMeanHourlyPercent},{self.DiffMedianHourlyPercent}, {self.DiffMeanBonusPercent}, {self.DiffMedianBonusPercent}, {self.MaleBonusPercent}, {self.FemaleBonusPercent}, {self.MaleLowerQuartile}, {self.FemaleLowerQuartile}, {self.end}, {self.disabilities_included}, {self.MaleLowerMiddleQuartile}, {self.FemaleLowerMiddleQuartile}, {self.MaleUpperMiddleQuartile}, {self.FemaleUpperMiddleQuartile}, {self.MaleTopQuartile}, {self.FemaleTopQuartile}, {self.EmployerSize}, {self.Region}, {self.Industry}, {self.EmployerSizeMedian}>"

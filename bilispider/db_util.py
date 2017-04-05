from sqlalchemy import create_engine, Column, String, Date, BIGINT, Integer, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
url = 'mysql+pymysql://spider:92qrjz$WfM#8@rdstvr064r8x3r6u0p8wo.mysql.rds.aliyuncs.com/bilibili?charset=utf8'
engine = create_engine(url, echo=False)


class DB_Util(object):
    @staticmethod
    def get_session(url=None):
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    @staticmethod
    def init_db():
        Base.metadata.create_all(engine)


# 在线人数
# http://www.bilibili.com/video/online.html
class MostWatched(Base):
    __tablename__ = 'square_mostWatched'
    id = Column(BIGINT, autoincrement=True, primary_key=True)
    time = Column(DateTime)
    av = Column('av_id', BIGINT)
    title = Column(String(128))
    audience = Column(Integer)
    replay = Column(BIGINT)
    danmuku = Column(BIGINT)
    uploader = Column(String(32))


# 排行榜
# http://www.bilibili.com/ranking#!/all/0/0/1/
class Ranking(Base):
    __tablename__ = 'square_ranking'
    id = Column(BIGINT, autoincrement=True, primary_key=True)
    date = Column(Date)
    pole = Column(String(16)) # 榜单名
    channel = Column('channel_id', Integer)
    position = Column(Integer)
    av = Column('av_id', BIGINT)
    title = Column(String(128))
    replay = Column(BIGINT)
    danmuku = Column(BIGINT)
    uploader = Column(String(32))
    score = Column(BIGINT)


# 视频详情
class Video(Base):
    __tablename__ = 'video_info'
    id = Column('av_id', BIGINT, primary_key=True)
    title = Column(String(128))
    channel = Column(String(128))
    post_time = Column(DateTime)
    his_rank = Column(Integer)
    uploader = Column('user_id', BIGINT)
    tag_list = Column(Text)
    descrp = Column(Text)


# 视频持续监测
class VideoLogging(Base):
    __tablename__ = 'video_log'
    id = Column(BIGINT, autoincrement=True, primary_key=True)
    time = Column(DateTime)
    av = Column('av_id', BIGINT, primary_key=True)
    coin = Column(BIGINT)
    favorite = Column(BIGINT)
    his_rank = Column(Integer)
    now_rank = Column(Integer)
    comments = Column(BIGINT)
    share = Column(BIGINT)
    replay = Column(BIGINT)
    danmuku = Column(BIGINT)
    audience = Column(BIGINT)
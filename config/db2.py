from sqlalchemy import create_engine, MetaData

#engine = create_engine("mysql+pymysql://root:Feifei3619/@127.0.0.1:3306/vintec_m3")
engine = create_engine("mysql+pymysql://root:Feifei3619/@127.0.0.1:3306/henry_checkpoint_m3")
#conn = engine.connect() no usar

meta_data = MetaData()

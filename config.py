

import os

basedir = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = './application/tracks'
SHIPMENT_FOLDER = './tracks'
#UPLOAD_FOLDER = './OriginalUnit/racks'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'application.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository') #자동 생성된 db_repository의 위치를 구합니다.
SQLALCHEMY_TRACK_MODIFICATIONS = True # 내가 설정함
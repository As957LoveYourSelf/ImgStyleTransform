import pymysql
import os, sys
import traceback
import datetime


# use mysql by pymysql
class SQLutil:
    def __mysql_connector(self, user, password, db):
        try:
            db_conn = pymysql.connect(host="localhost", port=3306, user=user, password=password, db=db)
            print("连接成功")
            return db_conn
        except:
            traceback.print_exc()
            print("连接失败")

    def __mysql_closer(self, db_conn):
        conn = db_conn
        try:
            conn.close()
            print("数据库连接关闭")
        except:
            traceback.print_exc()

    def __insert_tran_image(self, conn, image_name, image_type, image_data_code, date):
        try:
            if self.__had_image(conn,image_name,_type="tran"):
                print("图片已存在")
                return
            print("begin insert: {}".format(image_name + '.' + image_type))
            sql = "insert into tran_image values (%s, %s, %s, %s);"
            arg = (image_name, image_type, image_data_code, date)
            print(sql)
            cursor = conn.cursor()
            cursor.execute(sql, arg)
            conn.commit()
            cursor.close()
            print("insert {} success.".format(image_name + '.' + image_type))
        except:
            traceback.print_exc()
            conn.rollback()

    def __insert_org_image(self, conn, image_name, image_type, image_data_code, date):
        try:
            if self.__had_image(conn,image_name,_type="org"):
                print("图片已存在")
                return
            print("begin insert: {}".format(image_name + '.' + image_type))
            sql = "insert into org_image values (%s, %s, %s, %s);"
            arg = (image_name, image_type, image_data_code, date)
            cursor = conn.cursor()
            cursor.execute(sql, arg)
            conn.commit()
            cursor.close()
            print("insert {} success.".format(image_name + '.' + image_type))
        except:
            traceback.print_exc()
            conn.rollback()

    def __update_image(self):
        pass

    def __had_image(self, conn, image_name, _type=None):
        if _type is None:
            print("Undefined type.")
            return False
        sql = "select id from {}_image where id='{}'".format(_type, image_name)
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                sql_result = cursor.fetchone()
                return sql_result is not None
        except pymysql.err.ProgrammingError:
            traceback.print_exc()
            return True

    def __readall_image(self):
        pass

    def __del_image(self):
        pass

    def image2mysql(self, image_path, _type):
        # 数据库连接
        try:
            user = "root"
            password = "520521"
            db = "images"
            db_conn = self.__mysql_connector(user, password, db)
            # 数据获取 image_name, image_code, date
            image = open(image_path, 'rb')
            print("image path: ", image_path)
            image_code = image.read()
            image.close()
            img = os.path.split(image_path)[-1]
            image_name = img.split('.')[0]
            print("Insert image name: ", image_name)
            image_type = img.split('.')[1]
            print("Image type: ", image_type)
            image_datacode = pymysql.Binary(image_code)[3:]
            date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # 插入表类型判断
            if _type == "tran":
                self.__insert_tran_image(db_conn, image_name, image_type, image_datacode, date)
            elif _type == "org":
                self.__insert_org_image(db_conn, image_name, image_type, image_datacode, date)
            else:
                print("Undefined image type. Input 'org' or 'tran' please.")
                self.__mysql_closer(db_conn)
                return
            self.__mysql_closer(db_conn)
        except:
            traceback.print_exc()

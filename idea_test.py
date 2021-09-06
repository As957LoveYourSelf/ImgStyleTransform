import pymysql
import cv2
import os, sys
import numpy as np
import traceback
import datetime
from PIL import Image

# use mysql by pymysql
def mysql_connector(user, password, db):
    try:
        db_conn = pymysql.connect(host="localhost", port=3306, user=user, password=password, db=db)
        print("连接成功")
        return db_conn
    except:
        traceback.print_exc()
        print("连接失败")


def mysql_closer(db_conn):
    conn = db_conn
    try:
        conn.close()
    except:
        traceback.print_exc()


def insert_image(conn, image_name, image_type, image_data_code, date):
    try:
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


def update_image():
    pass


def select_image(conn, image_name):
    sql = "select * from tran_image where id='{}'".format(image_name)
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            sql_result = cursor.fetchone()
            print("Result: ", sql_result)
    except:
        traceback.print_exc()


def readall_image():
    pass


def del_image():
    pass


def main():
    # 图像编码转化
    image_path = "./result"
    image_list = os.listdir(image_path)
    # image = cv2.imread(os.path.join(image_path,image_list[0]))
    # img_encode = cv2.imencode(os.path.splitext(image_list[0])[1],image)
    # data_encode = np.array(img_encode)
    # print(data_encode.shape)
    # print(data_encode)
    # print(sys.getsizeof(data_encode))
    # 数据库连接、使用
    # user = str(input("Input user: "))
    # password = str(input("Input {} password: ".format(user)))
    # db = str(input("Input database: "))
    # print(user, password, db)
    db_conn = mysql_connector('root', '520521', 'images')
    # 数据获取 image_name, image_code, date
    # print("{} images in local.".format(len(image_list)))
    # count = 0
    # for img in image_list:
    #     image = open(os.path.join(image_path, img), 'rb')
    #     print("image path: ", os.path.join(image_path, img))
    #     image_code = image.read()
    #     image.close()
    #     # image = cv2.imread(os.path.join(image_path,image_list[0]))
    #     # img_encode = cv2.imencode(os.path.splitext(image_list[0])[1],image)
    #     # data_encode = np.array(img_encode)
    #     image_name = img.split('.')[0]
    #     image_type = img.split('.')[1]
    #     image_datacode = pymysql.Binary(image_code)[3:]
    #     date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #     insert_image(db_conn, image_name, image_type, image_datacode, date)
    #     count += 1
    # print("{} images inserted.".format(count))
    image = readimage(db_conn,'1630370511849')
    img = open(image[0]+'.'+image[1],'wb')
    img.write(image[2])
    img.close()
    mysql_closer(db_conn)

def readimage(conn, id):
    sql = "select id,image_type,image_code from org_image where id='{}'".format(id)
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            image = cursor.fetchone()
            # print("Result: ", sql_result)
            return image
    except:
        traceback.print_exc()

if __name__ == '__main__':
    main()
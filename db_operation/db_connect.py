# -*-coding:utf-8 -*-
# 这两行用于指定在linux下面的数据库连接符编码方式
import os
import cx_Oracle, redis
from config.get_config import get_db_args, get_redis_args
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


def get_con():
    args = get_db_args()
    dsn = cx_Oracle.makedsn(args['host'], args['port'], args['db_name'])
    conn = cx_Oracle.connect(args['user'], args['password'], dsn)
    return conn


def db_close(con):
    con.close()


def db_queryall(con, sql):
    cursor = con.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result


def db_queryone(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    return result


def db_queryone_params(con, sql, params):
    cursor = con.cursor()
    cursor.execute(sql, params)
    result = cursor.fetchone()
    cursor.close()
    return result


def db_queryall_params(con, sql, params):
    cursor = con.cursor()
    cursor.execute(sql, params)
    result = cursor.fetchall()
    cursor.close()
    return result


def db_dml(con, sql):
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()
    cursor.close()


def db_dml_parms(con, sql, parms):
    cursor = con.cursor()
    cursor.execute(sql, parms)
    con.commit()
    cursor.close()


def db_dml_many(con, sql, params_list):
    cursor = con.cursor()
    cursor.executemany(sql, params_list)
    con.commit()
    cursor.close()


def get_redis_con():
    args = get_redis_args()
    return redis.Redis(host=args['host'], port=args['port'], db=args['db_name'])


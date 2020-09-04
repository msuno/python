import pymysql

conn = pymysql.connect(
    host='47.102.201.87',
    user='root',
    password='Asd@950826',
    database='db_halo',
    charset='utf8'
)


def query(sql):
    cursor = conn.cursor()
    raws = cursor.execute(sql)
    print raws
    columns = cursor.fetchall()
    for a in columns:
        print a


if __name__ == '__main__':
    query('show tables')

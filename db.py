import PyMySQL


try:
    db = PyMySQL.connect("den1.mysql2.gear.host", "chandracanth95", "onlinedatabase",
                         "chandracanth95$chan");
    cur=db.cursor();
    cursor.execute("create table sample(num int);")
except:
    print("error")
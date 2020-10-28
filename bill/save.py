import sqlite3, datetime, json


class SaveAs:
    def __init__(self, list1,list2 ,name):
        self.list = list2
        self.list_top_entry = list1
        self.name = name
        self.cerate()

    def cerate(self):
        self.date = str(datetime.datetime.now().strftime("%d-%m-%Y"))
        tabel = sqlite3.connect(f"{self.name}_{self.date}.db")
        car = tabel.cursor()
        car.execute(
            "CREATE TABLE bill(nameP,address,prodakt_name,qit,rate,totel)")  # for macking a tabbel which name is bill
        tabel.commit()
        car.close()
        self.add_in_tabel()

    def add_in_tabel(self):
        tabel = sqlite3.connect(f"{self.name}_{self.date}.db")
        car = tabel.cursor()

        for list in self.list:
            print(type(list[0]), list[0].get(), list[1].get(), list[2].get(), list[3].get(), list[4].get())
            print()
            car.execute('INSERT INTO bill(nameP,address,prodakt_name,qit,rate,totel) VALUES(?,?,?,?,?,?)',
                        (list[0].get(), list[1].get(), list[2].get(),
                         list[3].get(), list[4].get(),
                         list[5].get()))  # inselting the data in sqlit3 data bass
        print("completed")
        tabel.commit()
        car.close()


class Show:
    def show_tabel(self, file_name):
        self.file_name = file_name
        tabel = sqlite3.connect(self.file_name)
        print(self.file_name)
        car = tabel.cursor()

        carpat = car.execute("SELECT nameP,address,prodakt_name,qit,rate,totel from bill")
        # for fetchall all data
        self.valu = car.fetchall()
        print(self.valu)
        tabel.commit()
        car.close()
        return self.valu

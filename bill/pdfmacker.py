import json
import os
import sqlite3
import subprocess
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

import calculation
from reportlab.pdfgen import canvas


class Summit:
    def __init__(self, list_of_top_entrys, list_of_all_entrys):


        self.list_of_top_entrys = list_of_top_entrys
        self.list_of_all_entrys = list_of_all_entrys

        self.cal = calculation.clculation()
        self.list_name = self.list_of_all_entrys
        print(self.list_of_all_entrys)
        self.datetime = self.cal.time()



        self.init()


    def init(self):
        self.start()
        self.data_saver_in_data_basses()
        self.drawing_data()

    def start(self):
        # ------------------------------------------------------------------------------
        # -----------------------------------------------------data storing in self value
        self.invoic_number = self.list_of_top_entrys[0]
        self.date = self.list_of_top_entrys[1]
        self.name = self.list_of_top_entrys[2]
        self.address = self.list_of_top_entrys[3]
        self.gst_in_percentage = self.list_of_top_entrys[4]
        self.gst_number = self.list_of_top_entrys[5]
        self.state = self.list_of_top_entrys[6]
        self.state_code = self.list_of_top_entrys[7]
        # -------------------------------------------------------------------------------
        # --------------------------------Some Thing--------------------------------------
        self.pdf = canvas.Canvas(f"{self.name}{self.datetime}.pdf")
        self.pdf.drawImage('pdf_3.jpg', 0, 00, width=595.276, height=841.89)


    def data_saver_in_data_basses(self):
        self.one = sqlite3.connect("one.db")
        self.cursor = self.one.cursor()
        try:
            self.cursor.execute("""CREATE TABLE histry_profile_4(invoice_num,address ,gst_num ,gst_pursanyage,name,date,product)
            """)
        except:
            return
        finally:
            print(self.list_name)
            for name, qui, rate, size in self.list_name:
                with open("histry.txt", "a") as file:
                    file.write(f"\n"
                               f"                  Invoice No.      {self.invoic_number} \n"
                               f"                    Invoic date    {self.date} \n"
                               f"                    Name           {self.name}\n"
                               f"                    address         {self.address} \n"
                               f"                    gst_in%          {self.gst_in_percentage} \n"
                               f"                    state          {self.state} \n"
                               f"                    gstin          {self.gst_number}\n"
                               f"                    state code     {self.state_code}\n"
                               f"                    name fo the pro{name}\n"
                               f"                    qui            {qui}\n"
                               f"                    rate           {rate}\n"
                               f"                    size           {size} ")
        list_mane = json.dumps(self.list_name)
        self.cursor.execute(
            f"""INSERT INTO histry_profile_4 VALUES (:invoice_num,:address,:gst_num ,:gst_in_num,:name,:invoice_date,:product)""",
            {"invoice_num": self.invoic_number,
             "address": self.address,
             "gst_num": self.gst_number,
             "gst_in_num": self.gst_in_percentage,
             "name": self.name,
             "invoice_date": self.date,
             "product": list_mane})
        self.one.commit()
        self.one.close()

    def drawing_data(self):


        try:
            print(self.gst_in_percentage)
            self.gst = int(self.gst_in_percentage)

        except:
            print("error",self.gst_in_percentage)

        self.pdf.setFontSize(9)
        self.name = self.name.upper()
        self.pdf.drawString(130, 622, self.invoic_number)
        self.pdf.drawString(130, 610, self.date)
        self.pdf.drawString(90, 575, self.name)
        if len(self.address) > 38:
            address_1 = self.address[0:38]
            address_2 = self.address[38:]
            self.pdf.drawString(90, 560, address_1)
            if len(address_2) > 38:
                self.pdf.setFontSize(7)
            self.pdf.drawString(90, 548, address_2)
            self.pdf.setFontSize(9)
        else:
            self.pdf.drawString(90, 560, self.address)

        self.pdf.drawString(90, 528, self.gst_number)
        self.pdf.drawString(90, 515, self.state)
        self.pdf.drawString(250, 510, self.state_code)
        self.pdf.drawString(130, 600, "UTTARAKHAND")
        self.pdf.drawString(250, 600, "05")
        self.prooses()


    def prooses(self):
        y = 452
        num = 1
        totel = 0
        print(self.list_name)
        for list, qty, rate, size in self.list_name:
            qty,rate,size=int(qty),int(rate),int(size)
            string = ""
            # for ls in list_sq[1:]:
            #     string += f" {ls} "
            string="---"

            amount = size * (qty * rate)



            totel += amount

            qty = str(qty)
            rate = str('%.0f' % rate)
            num_1 = str(num)
            self.pdf.drawString(55, y, str(num))

            if len(list) > 45:
                list_1 = list[0:40]
                list_2 = list[40:]
                self.pdf.drawString(80, y, list_1)

                y -= 15
                self.pdf.drawString(80, y, list_2)

                self.pdf.drawString(372, y, f"{qty} ")
                self.pdf.drawString(427, y, f"{rate}/-{string}")
                self.pdf.drawString(482, y, f"{str(amount)}/-")

            else:
                self.pdf.drawString(80, y, list)
                self.pdf.drawString(372, y, f"{qty} ")
                self.pdf.drawString(427, y, f"{rate}/-{string}")
                self.pdf.drawString(482, y, f"{str('%.0f' % amount)}/-")

            y -= 15
            num += 1
        print("----------------M------------------1--")

        self.pdf.drawString(482, 190, f"{str('%.0f' % totel)}/-")

        gst_va = totel * (self.gst / 100)
        all_totel = int(round(totel + gst_va))

        all_totel_str = str("%.0f" % all_totel)
        print("'%.0f'" % gst_va)
        gst_va_str = str("%.0f" % gst_va)
        self.pdf.drawString(482, 150, f"{gst_va_str} /-")
        self.pdf.drawString(482, 130, f"{all_totel_str} /-")

        word = self.cal.num2words(all_totel)
        print("----------------M------------------2--")
        if len(word + "only") > 44:
            word_1 = word.split(" ")[0:6]
            n = ""
            for word_1 in word_1:
                n = n + " " + word_1 + " "
            word_2 = word.split(" ")[6:]
            m = ""
            for word_2 in word_2:
                m = m + " " + word_2 + " "
            self.pdf.drawString(175, 173, f"{n} ")
            if len(word_1) > 60:
                self.pdf.setFontSize(7)
            self.pdf.drawString(50, 156, f"{m} only")
        else:

            self.pdf.drawString(180, 173, f"{word} only")
        self.add(gst_va)
        print("----------------M------------------1--")


        # calculation.clculation.replace("self", self.invoic_number)

        os.chdir('C:\\Users\\User\\PycharmProjects\\pyqt\\test_pdf')
        self.pdf.save()
        print("-------------------------Ok--------------------------")






    def add(self, gst):
        gst=int(gst)
        gst_va_haff = gst / 2
        gst_va_haff_str = str("%.0f" % gst_va_haff)

        gst = int(self.gst_in_percentage)
        gst_div = gst / 2
        gst_str = str(gst_div)
        gst_str = str(gst / 2)
        print(gst_str)
        self.pdf.drawString(160, 202, f"{gst_va_haff_str}")
        self.pdf.drawString(90, 202, f"{gst_va_haff_str}")
        self.pdf.drawString(113, 216, f"{gst_str}")
        self.pdf.drawString(183, 216, f"{gst_str}")
#
#
# class Show:
#     def __init__(self, e1, e2, e3, e4, e5, e5_1, e7, e8, e8_1, e9, oid):
#         self.invoic_number = e1
#
#         self.date = e2
#         self.name = e3
#         self.address = e4
#         self.gst_in_percentage = e5
#         self.gst_number = e5_1
#         self.entry_7 = e7
#         self.entry_8 = e8
#         self.entry_8_1 = e8_1
#         self.entry_9 = e9
#         self.entry_oid = oid
#         self.histryshow()
#
#     def histryshow(self):
#         m = 0
#         oid = self.entry_oid.get()
#
#         one = sqlite3.connect("one.db")
#         cursor = one.cursor()
#         cursor.execute(f"SELECT oid FROM histry_profile_4 ")
#         number = cursor.fetchall()
#
#         if not f"{oid}," in f"{str(number)}":
#             messagebox.showerror("ERROR", "ENTER IN VALUE IN oid num BOX#")
#             return
#         else:
#             m += 1
#
#         cursor.execute(f"SELECT * FROM histry_profile_4 WHERE oid=:oid",
#                        {"oid": oid}
#                        )
#         value = cursor.fetchall()
#         self.invoic_number.delete(0, last=1000)
#         self.address.delete(0, last=1000)
#         self.gst_number.delete(0, last=1000)
#         self.gst_in_percentage.delete(0, last=1000)
#         self.name.delete(0, last=1000)
#         self.date.delete(0, last=1000)
#         for value in value:
#             self.address.insert(0, value[1])
#             self.gst_number.insert(0, value[2])
#             self.gst_in_percentage.insert(0, value[3])
#             self.name.insert(0, value[4])
#             self.date.insert(0, value[5])
#
#         row = 1
#         num = 1
#         try:
#             joky = json.loads(value[6])
#             self.root_1 = Tk()
#             size = "200"
#             if len(json.loads(value[6])) > 5:
#                 size = str(200 + (20 * len(json.loads(value[6]))))
#             self.root_1.geometry(f"200x{size}")
#
#             m += 1
#             label_show = Label(self.root_1, text="S.No")
#             label_show_1 = Label(self.root_1, text="Name")
#
#             label_show_2 = Label(self.root_1, text="Qty")
#             label_show_3 = Label(self.root_1, text="Rate")
#             label_show_4 = Label(self.root_1, text="size")
#             label_show.grid(row=0, column=0)
#             label_show_1.grid(row=0, column=1)
#             label_show_2.grid(row=0, column=2)
#             label_show_3.grid(row=0, column=3)
#             label_show_4.grid(row=0, column=4)
#             list_k = 0
#             for ks in json.loads(value[6]):
#                 print(ks)
#                 label = Label(self.root_1, text=f"{num}")
#                 label.grid(row=row, column=0)
#                 label = Label(self.root_1, text=f"{ks[0]}")
#                 label.grid(row=row, column=1)
#                 label = Label(self.root_1, text=f"{ks[1]}")
#                 label.grid(row=row, column=2)
#                 label = Label(self.root_1, text=f"{ks[2]}")
#                 label.grid(row=row, column=3)
#                 label = Label(self.root_1, text=f"{ks[3]}")
#
#                 label.grid(row=row, column=4)
#                 row += 1
#                 list_k += 1
#                 num += 1
#         except:
#             messagebox.showerror("ERROR", "ENTER IN VALUE IN oid num BOX#")
#             return
#         label_show_4 = Label(self.root_1, text="Num:-")
#         label_show_4.grid(row=row, column=0)
#
#         self.entry_rate = Entry(self.root_1)
#         self.entry_rate.grid(row=row, column=1, columnspan=5)
#         but = Button(self.root_1, text="show", command=lambda: self.happy(joky))
#         but.grid(row=row + 1, column=1)
#         one.commit()
#         one.close()
#         if m == 2:
#             self.root_1.mainloop()
#
#     def happy(self, value):
#
#         print(value)
#         try:
#
#             get = int(self.entry_rate.get()) - 1
#
#             print(get)
#             if len(value) < get:
#                 messagebox.showerror("ERROR", "ENTER WRITE VALUE")
#
#             self.entry_7.delete(0, 1000)
#             self.entry_8.delete(0, 1000)
#             self.entry_8_1.delete(0, 1000)
#             self.entry_9.delete(0, 1000)
#
#             self.entry_7.insert(0, str(value[get][0]))
#             self.entry_8.insert(0, str(value[get][1]))
#             self.entry_9.insert(0, str(value[get][2]))
#             self.entry_8_1.insert(0, str(value[get][3]))
#
#
#
#
#         except TypeError:
#             messagebox.showerror("ERROR", "ENTER WRITE VALUE")
#         finally:
#             self.root_1.destroy()

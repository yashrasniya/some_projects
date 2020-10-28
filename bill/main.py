from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QApplication, QAction, QMenu
import threading
import save, pdfmacker


class my_cal(QMainWindow):
    def __init__(self):
        super(my_cal, self).__init__()
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle("Bill")
        self.start()

    def start(self):
        self.all_entry_list, self.but, self.y, self.totle_list_label = [], [], [], []  # f=list of entry,i =list of button and entry

        self.y.append(100)
        self.entry()  # start
        self.start=True
        # self.all_entry_list[-1][-1].returnPressed.connect(self.entry)  # when press enter it create a row
        self.loop()
        self.menu()
        self.top_entrys()
        self.Qlabel = QtWidgets.QLabel(self)
        self.Qlabel.setGeometry(500, 500, 200, 50)
        b1=QtWidgets.QPushButton(self)
        b1.clicked.connect(self.creating_pdf)


    def donothing(self):
        pass

    def save_as(self):
        self.geting_all_values()
        js = filedialog.asksaveasfilename()  # creating a dialogebox for name

        save.SaveAs(self.geting_values_of_top_list,
                         self.data_all_entry_list, js)

    def open(self):

        open_file = str(filedialog.askopenfile()).split("'")  # creating a dialogebox for file path
        self.all_entry_list.clear()  # delete all data of list
        self.i.clear()  # delete all data of list
        self.i.append(1)  # add 1 for loop funtion
        value = save.Show()

        value = value.show_tabel(open_file[1])
        num = 0

        print(value)
        for v in value:
            self.entry("v")
            l = 0
            for j in v:
                self.all_entry_list[num][l].insert(0, j)  # display all data in entry
                l += 1
            num += 1

    def menu(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        editMenu = menubar.addMenu('Edit')

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)
        self.actionCopy = QtWidgets.QAction(self)

        copy = editMenu.addMenu("Copy")
        paste = editMenu.addMenu("Paste")
        cut = editMenu.addMenu("Cut")
        self.actionCopy.setObjectName("actionCopy")
        copy.addAction(self.actionCopy)

        newAct = QAction('New', self)
        _translate = QtCore.QCoreApplication.translate
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        menubar.show()

        # menubar = Menu(root)
        # filemenu = Menu(menubar, tearoff=0)
        #
        # filemenu.add_command(label="Open", command=open)
        #
        # filemenu.add_command(label="Save as...", command=self.save_as)
        #
        #
        # filemenu.add_separator()
        #
        # filemenu.add_command(label="Exit", command=root.quit)
        # menubar.add_cascade(label="File", menu=filemenu)
        #
        #
        # root.config(menu=menubar)

    def top_entrys(self):

        # ----------------------------------------------#
        # ----------------location----------------------#

        self.x_1, self.y_1 = [], []
        self.x_1.append(0)
        self.y_1.append(50)

        # -------------------------------------------label------------------------------------------------------------------
        label_values = [" Invoic number", "Date", "Name", "Addres", "Gst in Percentage", "Gst Number", "State",
                        "State Code"]
        self.label = []
        for name in label_values:
            self.label.append(QtWidgets.QLabel(self))
            self.label[-1].setText(f"{name}")
            self.label[-1].setGeometry(self.x_1[-1], 20, 100, 30)
            self.x_1.append(self.x_1[-1] + 100)
            self.label[-1].show()
        self.x_1.clear()
        self.x_1.append(0)
        # -------------------------------entry box---------------------------------------------------
        invoic_number = QLineEdit(self)
        date = QLineEdit(self)
        name = QLineEdit(self)
        addres = QLineEdit(self)
        gst_in_percentage = QLineEdit(self)
        gst_number = QLineEdit(self)
        state = QLineEdit(self)
        state_code = QLineEdit(self)
        self.top_entry = [invoic_number, date, name, addres, gst_in_percentage, gst_number, state, state_code]
        for valu in self.top_entry:
            valu.setGeometry(self.x_1[-1], self.y_1[-1], 100, 30)
            self.x_1.append(self.x_1[-1] + 100)
            print(valu)
            valu.show()
        self.list_for_product =['Name',
                                'Gst',
                                'Size',
                                'Quantity',
                                'Rate']
        self.list_of_product_pyqt=[]
        self.x_1.clear()
        self.x_1.append(0)
        for value in self.list_for_product:
            self.list_of_product_pyqt.append(QtWidgets.QLabel(self))
            self.list_of_product_pyqt[-1].setText(f"{value}")
            self.list_of_product_pyqt[-1].setGeometry(self.x_1[-1]+5, self.y_1[-1]+30, 100, 30)
            self.x_1.append(self.x_1[-1] + 100)
            self.list_of_product_pyqt[-1].show()
        print('-------------------2---')

    def entry(self):  # for creating a new row of entry

        try:
            self.all_entry_list[-1][-1].returnPressed.disconnect(self.entry)  # unbind the last entry
            pass

        except:
            pass

        en = []
        self.i = []
        self.i.append(0)

        for ii in range(0, 5):  # for 5 entry

            # text  boxs
            x = self.i[-1]
            en.append(QLineEdit(self))

            en[ii].setGeometry(x, self.y[-1]+5, 100, 30)
            en[ii].show()

            self.i.append(self.i[-1] + 100)

        self.totle_list_label.append(QtWidgets.QLabel(self))
        self.totle_list_label[-1].setGeometry(self.i[-1], self.y[-1]+5, 100, 30)


        self.y.append(self.y[-1] + 50)
        self.totle_list_label[-1].setText("0.0")
        self.totle_list_label[-1].show()
        self.all_entry_list.append(en)
        print(self.all_entry_list)
        self.all_entry_list[-1][-1].returnPressed.connect(self.entry)  # when press enter it create a row
    def loop(self):
        # ---------------- for loopcution in side the entry-------------------------------------

        time = 1  # wait for 1 sec
        self.get_qut = []  # list of entry3
        self.get_rate = []  # list of entry4
        self.get_size = []  # list of entry2
        self.get_gst = []
        multiply = []  # list of adtion of entry3 + entry4
        for num in range(len(self.all_entry_list)):
            try:
                if self.all_entry_list[num][-2].text() != "" and self.all_entry_list[num][-3].text() != "" and self.all_entry_list[num][-1].text() != "":
                    self.get_qut.append(int(self.all_entry_list[num][-2].text()))  # geting entry3
                    self.get_rate.append(int(self.all_entry_list[num][-1].text()))  # geting entry4
                    self.get_size.append(int(self.all_entry_list[num][-3].text()))
                    self.get_gst.append(int(self.all_entry_list[num][-4].text()))# geting entry2
                else:
                    print(self.all_entry_list[num][-2].text())
            except:
                try:
                    str(self.all_entry_list[num][-1].text())
                    str(self.all_entry_list[num][-2].text())
                    print("-------------------------------")
                except:

                    print("something went wrong!")

        try:
            for a in range(0, len(self.get_qut)):
                print(a, "get")
                print(self.get_qut, self.get_rate)
                t = self.get_qut[a] * self.get_rate[a] * self.get_size[a] # multiply qui and rate

                multiply.append((t,self.get_gst[a]))
            nos = 0
            ks = 0
            with_gst_totel=0
            for nass ,gst in multiply:
                print(":")
                print("::")
                pre = nass + ks
                with_gst_totel=(nass*gst)/100+with_gst_totel


                self.totle_list_label[nos].setText(f"without gst:{nass} withgst:{(nass*gst)/100} Total:{pre} Total withgst:{with_gst_totel}")  # show the data as label
                self.totle_list_label[nos].adjustSize()
                self.totle_list_label[nos].show()
                ks=pre
                nos += 1
        except:
            time = 5
            print("error")
            pass

        time = threading.Timer(time, self.loop)
        if self.start==False:
            time.cancel()
        else:
            time.start()  # start the loop

    def geting_all_values(self):
        self.start=False
        # -------------------------------------geting all values by entrys------------------------------------
        self.geting_values_of_top_list = []
        self.data_all_entry_list = []
        for vaues in self.top_entry:
            self.geting_values_of_top_list.append(vaues.text())
        for data in self.all_entry_list:
            tamperli_list = []
            for data in data:
                tamperli_list.append(data.text())
            self.data_all_entry_list.append(tamperli_list)





        # ---------------------------------creating pdf-------------------------------------
    def creating_pdf(self):
        self.geting_all_values()
        pdfmacker.Summit(self.geting_values_of_top_list,
                         self.data_all_entry_list)


def main():
    app = QApplication(sys.argv)
    win = my_cal()
    win.show()
    try:
        exit(app.exec_())
    except:
        print("----------Error---------")

main()
root = Tk()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from general import *
from ip_address import *
from nmap import *
from whois import *
from url_manipu import *
from webscanner import Ui_MainWindow
from result_final import Ui_FMainWindow

Root_DIR = 'Result'
create_dir(Root_DIR)


def gather_info1(name, url1):
    ip = get_ip_address(url1)
    ports = get_nmap('-F', ip)
    whois = get_whois(url1)
    url_mani = geturlmanip(url1)
    result(name, url1, ip, ports, whois, url_mani)


def result(name, furl, ip, ports, whois, url_mani):
    project_dir = Root_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/furl.txt', furl)
    write_file(project_dir + '/ip.txt', ip)
    write_file(project_dir + '/ports.txt', ports)
    write_file(project_dir + '/whois.txt', whois)
    write_file(project_dir + '/url_manipulation', url_mani)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start)
        self.ui.pushButton.clicked.connect(self.resultfi)

    def start(self):
        self.url = self.ui.lineEdit.text()
        print(self.url)
        gather_info1('info', self.url)

    def resultfi(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_FMainWindow()
        self.ui.setupUi(self.window2)
        self.ui.label.setText(self.url)
        self.ui.label_10.setText(self.url)
        self.window2.show()
        path = "C:\\Users\\atish\\PycharmProjects\\WEBSCANNER\\Result\\info\\ip.txt"
        with open(path, "r") as f:
            ip = f.readline()
            self.ui.label_14.setText(ip)
        path1 = "C:\\Users\\atish\\PycharmProjects\\WEBSCANNER\\Result\\info\\ports.txt"
        with open(path1, "r") as f1:
            ports = f1.read()
            self.ui.textBrowser.setText(ports)
        path2 = "C:\\Users\\atish\\PycharmProjects\\WEBSCANNER\\Result\\info\\url_manipulation"
        with open(path2, "r") as f2:
            link = f2.read()
            self.ui.textBrowser_2.setText(link)
        path3 = "C:\\Users\\atish\\PycharmProjects\\WEBSCANNER\\Result\\info\\whois.txt"
        with open(path3, "r") as f3:
            whois = f3.read()
            self.ui.textBrowser_4.setText(whois)
        if 300 < len(ports) <= 500:
            self.ui.label_24.setText("10")
            self.ui.label_7.setText("AWESOME! YOUR WEBSITE HAS VERY LOW SECURITY RISK")
            path4 = "C:\\Users\\atish\\PycharmProjects\\WEBSCANNER\\SQL.txt"
            with open(path4, "r") as f5:
                sql = f5.read()
                self.ui.textBrowser_3.setText(sql)
        elif 500 < len(ports) <= 550:
            self.ui.label_24.setText("8")
            self.ui.label_7.setText("GREAT! YOUR WEBSITE HAS LOW SECURITY RISK")
            path4 = "C:\\Users\\atish\\PycharmProjects\\WEBSCANNER\\SQL.txt"
            with open(path4, "r") as f5:
                sql = f5.read()
                self.ui.textBrowser_3.setText(sql)
        elif 550 < len(ports) <= 600:
            self.ui.label_24.setText("6")
            self.ui.label_7.setText("NOT GOOD! YOUR WEBSITE HAS MODERATE SECURITY RISK")
            path4 = "C:\\Users\\atish\\PycharmProjects\\WEBSCANNER\\SQLMAP.txt"
            with open(path4, "r") as f5:
                sql = f5.read()
                self.ui.textBrowser_3.setText(sql)
        elif len(ports)>600:
            self.ui.label_24.setText("4")
            self.ui.label_7.setText("BAD! YOUR WEBSITE HAS CRITICAL SECURITY RISK")
            path4 = "C:\\Users\\atish\\PycharmProjects\\WEBSCANNER\\SQLMAP.txt"
            with open(path4, "r") as f5:
                sql = f5.read()
                self.ui.textBrowser_3.setText(sql)
        with open(path3, "r") as f4:
            str = f4.read()
            c = str.find("Name Server")
            c1 = str.find("DN")
            c = c + 15
            c1 = c1 - 4
            f4.seek(c)
            self.ui.label_15.setText(f4.read(c1 - c))
            d = str.find("Domain ID")
            d1 = str.find("Registrar WHOIS")
            d = d + 13
            d1 = d1 - 4
            f4.seek(d)
            self.ui.label_16.setText(f4.read(d1 - d))


app = QApplication(sys.argv)
robot = Main()
robot.show()
exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
from twittercreds import Ui_dlgTwitterCreds
from percentagesdialog import Ui_PercentagesDialog
from freqdistdialog import Ui_FreqDistDialog
import psycopg2


class TwitterCredsWindow(QtWidgets.QDialog, Ui_dlgTwitterCreds):
    def __init__(self, parent=None):
        super(TwitterCredsWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.btnSave.clicked.connect(self.btnSaveClicked)
        self.btnSaveSetDefault.clicked.connect(self.btnSaveSetDefaultClicked)
        #This is a primitive implementation of using databases in this program for testing purposes. It will have the option to allow the user to input credentials for their own database in the future
        conn_string = "host='localhost' dbname='postgres' user='postgres' password='test'"
        print("Connecting to database\n ->%s " % (conn_string))
        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()
        cur.execute("select exists(select * from information_schema.tables where table_name=%s)", ('twitter_creds',))
        if not cur.fetchone()[0]: #if the twitter credentials table doesn't yet exist, create it.
            cur.execute("CREATE TABLE twitter_creds (id serial PRIMARY KEY, consumer_key varchar, consumer_secret varchar, access_key varchar, access_secret varchar);")
        else:
            print("Table already exists!")

        cur.execute("SELECT * FROM twitter_creds;")
        TwitCreds = cur.fetchone()
        self.leConsumerKey.setText(TwitCreds[1])
        self.leConsumerSecret.setText(TwitCreds[2])
        self.leAccessKey.setText(TwitCreds[3])
        self.leAccessSecret.setText(TwitCreds[4])
        conn.commit()
        # Close communication with the database
        cur.close()
        conn.close()

    def btnSaveClicked(self):
        #save the credentials only temporarily for this run of the program
        global consumer_key_string
        consumer_key_string = self.leConsumerKey.text()
        global consumer_secret_string
        consumer_secret_string = self.leConsumerSecret.text()
        global access_key_string
        access_key_string = self.leAccessKey.text()
        global access_secret_string
        access_secret_string = self.leAccessSecret.text()

    def btnSaveSetDefaultClicked(self):
        twitterCreds = []
        # Temporary database implementation for testing purposes. Will implement for user input later.
        conn_string = "host='localhost' dbname='postgres' user='postgres' password='test'"

        # print the connection string we will use to connect
        print("Connecting to database\n ->%s " % (conn_string))

        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)

        cur = conn.cursor()

        thefile = open('twittercreds.txt', 'w')
        global consumer_key_string
        consumer_key_string = self.leConsumerKey.text()
        twitterCreds.append(consumer_key_string)
        global consumer_secret_string
        consumer_secret_string = self.leConsumerSecret.text()
        twitterCreds.append(consumer_secret_string)
        global access_key_string
        access_key_string = self.leAccessKey.text()
        twitterCreds.append(access_key_string)
        global access_secret_string
        access_secret_string = self.leAccessSecret.text()
        twitterCreds.append(access_secret_string)
        # Write the credentials to a text file in case the user does't have database implementation
        for item in twitterCreds:
            thefile.write("%s\n" % item)
        cur.execute("DELETE FROM twitter_creds where 1=1")
        cur.execute(
            "INSERT INTO twitter_creds  (consumer_key, consumer_secret, access_key, access_secret) VALUES (%s, %s, %s, %s)",
            (consumer_key_string, consumer_secret_string, access_key_string, access_secret_string))
        conn.commit()
        # Close communication with the database
        cur.close()
        conn.close()

class PercentagesWindow(QtWidgets.QDialog, Ui_PercentagesDialog):
    def __init__(self, parent=None):
        super(PercentagesWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)

class FreqDistWindow(QtWidgets.QDialog, Ui_FreqDistDialog):
    def __init__(self, parent=None):
        super(FreqDistWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
import pandas as pd
import tweepy
import sys
import MenuClasses
import csv
import glob
from threading import Thread
from PyQt5 import QtWidgets
import DataProgram
import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist


global completed
completed = 0
global linescount
linescount = 0
global includeIndvFreqDists
includeIndvFreqDists = False
global includeDateFilter
includeDateFilter = False
global includeMetaFreqDist
includeMetaFreqDist = False
global consumer_key_string
global consumer_secret_string
global access_key_string
global access_secret_string
global content

def get_all_tweets(self, screen_name):
    if self.leDiscardAccounts.isEnabled():
        TweetMinimum = int(StartQT5.leDiscardAccounts.Text())
    else:
        TweetMinimum = 1;
    consumer_key = content[0]
    consumer_secret = content[1]
    access_key = content[2]
    access_secret = content[3]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    alltweets = []
    try:
        new_tweets = api.user_timeline(screen_name=screen_name, count=200)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        RowCount = 0
        while len(new_tweets) > 0:
            print("Getting Tweets for", screen_name)
            new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
            alltweets.extend(new_tweets)
            oldest = alltweets[-1].id - 1
            print("...%s tweets downloaded so far" % (len(alltweets)))
            data = [[obj.user.screen_name, obj.user.name, obj.user.id_str, obj.user.description,
                     obj.created_at.year, obj.created_at.month, obj.created_at.day,
                     "%s.%s" % (obj.created_at.hour, obj.created_at.minute),
                     "%s.%s.%s" % (obj.created_at.month, obj.created_at.day, obj.created_at.year), obj.id_str,
                     obj.favorite_count, obj.retweet_count, obj.text] for obj in alltweets]
            data2 = [[obj.text] for obj in alltweets]
            dataframe = pd.DataFrame(data, columns=['Screen Name', 'Name', 'Twitter ID', 'Description', 'Year', 'Month',
                                                    'Day', 'Time', 'Date', 'Tweet ID', 'Favorite Count',
                                                    'Retweet Count', 'Tweet'])
            dataframe2 = pd.DataFrame(data2, columns=['Tweet'])
            currentRowCount = dataframe2.shape[0]
            RowCount += currentRowCount
            dataframe.to_csv("%s_tweets.csv" % (screen_name), index=True)
            dataframe2.to_csv("%s_tweetsonly.csv" % (screen_name), index=False)
        filename = ("%s_tweetsonly.csv" % (screen_name))
        global includeIndvFreqDists
        includeIndvFreqDists = True
        if self.cbIncludeFreqDist.isChecked():
            StartQT5.runFreqDist(self, filename)
        print("Finished Mining Tweets for", screen_name)
        if RowCount < TweetMinimum:
            StartQT5.txtBadUsernames.append(self, screen_name)
        if includeDateFilter:
            StartQT5.filterDates(self)
    except tweepy.TweepError:
        self.txtBadUsernames.append(screen_name)
        pass
    except IndexError:
        self.txtBadUsernames.append(screen_name)
        pass


class StartQT5(QtWidgets.QMainWindow, DataProgram.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.progressBar.setValue(0)

        self.actionDeveloper_Credentials.triggered.connect(self.openTwitterCreds)
        self.actionContent_Analysis.triggered.connect(self.openPercentageResults)
        self.actionView_Last_Frequency_Distribution.triggered.connect(self.openFreqDist)
        self.cbDiscardAccounts.stateChanged.connect(self.enableMinTweets)
        self.cbExcludeShortWords.stateChanged.connect(self.enableMinFreqWords)
        self.cbIncludeFreqDistAllAccounts.stateChanged.connect(self.enableMetaFreqDist)
        self.cbCommonWords.stateChanged.connect(self.enableCommonWords)
        self.cbCommonWords.stateChanged.connect(self.enableCommonWords)
        self.cbFilterDate.stateChanged.connect(self.enableDateFitler)
        self.btnStart.clicked.connect(self.btnStart_clicked)

        with open('twittercreds.txt') as f:
            global content
            content = f.readlines()
        global content
        content = [x.strip() for x in content]

        self.initUI()

    def initUI(self):
        self.show()
    def enableMetaFreqDist(self):
        if self.cbIncludeFreqDistAllAccounts.isChecked():
           global includeMetaFreqDist
           includeMetaFreqDist = True
        else:
            includeMetaFreqDist = False
    def enableMinTweets(self):
        if self.cbDiscardAccounts.isChecked():
            self.leDiscardAccounts.setEnabled(True)
        else:
            self.leDiscardAccounts.setEnabled(False)

    def enableDateFitler(self):
        if self.cbFilterDate.isChecked():
            self.deTweetOldest.setEnabled(True)
            self.deTweetRecent.setEnabled(True)
            global includeDateFilter
            includeDateFilter = True
        else:
            self.deTweetOldest.setEnabled(False)
            self.deTweetRecent.setEnabled(False
                                          )
    def enableCommonWords(self):
        if self.cbCommonWords.isChecked():
            self.leCommonWords.setEnabled(True)
        else:
            self.leCommonWords.setEnabled(False)
            global includeDateFilter
            includeDateFilter = False

    def enableMinFreqWords(self):
        if self.cbExcludeShortWords.isChecked():
            self.leExcludeChars.setEnabled(True)
        else:
            self.leExcludeChars.setEnabled(False)

    def enableIndvFreqDist(self):
        if self.cbIncludeFreqDist.isChecked():
            global includeIndvFreqDists
            includeIndvFreqDists = True
        else:
            global includeIndvFreqDists
            includeIndvFreqDists = False
    def openTwitterCreds(self):
        self.nd = MenuClasses.TwitterCredsWindow(self)
        self.nd.show()

    def openPercentageResults(self):
        self.nd = MenuClasses.PercentagesWindow(self)
        self.nd.show()

    def openFreqDist(self):
        self.nd = MenuClasses.FreqDistWindow(self)
        self.nd.show()

    def runFreqDist(self, filename):
        # tokenize tweets
        raw = open(filename).read()
        tokens = nltk.tokenize.casual.casual_tokenize(raw, preserve_case=False, reduce_len=True, strip_handles=True)
        # convert tokens to NLTK text
        words = [w.lower() for w in tokens]
        minWordLength = 3

        if self.leExcludeChars.isEnabled():
            minWordLength = self.leExcludeChars.Text()
        if self.leCommonWords.isEnabled():
            freqDistNum = self.leCommonWords.Text()
        else:
            freqDistNum = 100
        # remove stop words
        stop_words = set(stopwords.words('english'))
        stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
        with open('stopwords.txt') as f: #custom stop word list to add to nltk's list
            for line in f:
                stop_words.update(line)
        filtered_words = [word for word in words if word not in stop_words and len(word) > minWordLength]

        # Perform normal frequency distribution
        fdist1 = FreqDist(filtered_words)

        # Save to csv file
        with open(filename + '_freqdist.csv', "w") as fp:
            writer = csv.writer(fp, quoting=csv.QUOTE_ALL, lineterminator='\n')
            writer.writerows(fdist1.most_common(freqDistNum))
        print("Finished running frequency distribution for" + filename)

    def runMetaFreqDist(self):
        allfreqwords = []
        for filename in glob.glob('*.csv'):
            if filename.endswith("_freqdist.csv"):
                with open(filename, 'r') as inp:
                    for row in csv.reader(inp):
                        allfreqwords.append(row[0])
        print(allfreqwords)
        metaFreqDist = FreqDist(allfreqwords)
        with open('OverallFreqDist.csv', 'a', newline='', encoding='utf8') as out:
            writer = csv.writer(out, quoting=csv.QUOTE_ALL, lineterminator='\n')
            writer.writerows(metaFreqDist.most_common(100))


    def btnStart_clicked(self):
        self.progressBar.setValue(0)
        self.startMiner()
        # self.btnStart.setEnabled(self, False)

    def updateValue(self, data):
        self.progressBar.setValue(data)

    def filterDates(self):
        yearoldest = self.deTweetOldest.date().year()
        montholdest = self.deTweetOldest.date().month()
        dayoldest = self.deTweetOldest.date().day()

        yearnewest = self.deTweetRecent.date().year()
        monthnewest = self.deTweetRecent.date().month()
        daynewest = self.deTweetRecent.date().day()

        for filename in glob.glob('*.csv'):
            if filename.endswith("_tweets.csv"):
                with open(filename, 'r') as inp, open(filename + '_datesfiltered.csv', 'a', newline='', encoding='utf8') as out:
                    writer = csv.writer(out)
                    firstline = True
                    for row in csv.reader(inp):
                        try:
                            if not firstline:
                                if int(row[5]) == yearoldest:
                                    if ((int(row[6]) == montholdest) and (int(row[7]) >= dayoldest)):
                                        writer.writerow(row)
                                    elif (int(row[6]) > montholdest):
                                        writer.writerow(row)
                                elif int(row[5]) == yearnewest:
                                    if ((int(row[6]) == monthnewest) and (int(row[7]) <= daynewest)):
                                        writer.writerow(row)
                                    elif ((int(row[6]) < monthnewest)):
                                        writer.writerow(row)
                                elif ((int(row[5]) < yearnewest) and (int(row[5]) > yearoldest)):
                                    writer.writerow(row)
                                else:
                                    x = 1
                            else:
                                firstline = False
                        except IndexError:
                            pass
                        except csv.Error:
                            pass

    def startMiner(self):
        tusers = self.TeTwitterUsernames.toPlainText()
        completedCount = 0
        global linescount
        linescount = 0
        for line in tusers.splitlines():
            if line is not None:
                global linescount
                linescount += 1
        for line in tusers.splitlines():
            if line is not None:
                try:
                    thread = Thread(target = get_all_tweets, args = (self, line.rstrip()))
                    thread.start()
                    thread.join()
                    completedCount += 1
                    global completed
                    completed = ((completedCount / linescount) * 100)
                    self.progressBar.setValue(completed)
                except(tweepy.TweepError):
                    self.txtBadUsernames.append(line)
                    pass
                except(IndexError):
                    pass
        print("Finished Mining Tweets")
        global includeMetaFreqDist
        if includeMetaFreqDist:
            StartQT5.runMetaFreqDist(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = StartQT5()
    sys.exit(app.exec_())



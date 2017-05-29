This program is still incomplete and continuously being added to. There may be some bugs, but all included functionality should work just fine. This program was created for mining Tweets and associated information from specificed twitter accounts for the purpose of social science research and analysis. 

By default if frequency distributions are enabled, unless otherwise changed by the user under frequency distribution options, the program will only search for words greater than or equal to three characters. Anything less would defeat the purpose, but the user can change it to be less or more. By default the program will also perform the frequency distribution for the 100 most common words unless otherwise specified by the user. 

The program will output the tweet and frequency distribution files in the same directory as the program. These should be moved to the appropriate place by the user after each mining to ensure no data corruption. 

If the user should choose to filter by date, the tweets that will be filtered will be ones among the 3200 most recent. Twitter does not allow mining based on date. The only way tweets can be mined is by downloading a specific number up to 3200. Therefore when date filtering is enabled, it will filter out tweets based on that set of up to 3200 tweets. 

There will be future updates to allow the user to choose where to save the files and more options for how the frequency distributions are done. A content analysis module will be integrated as well.
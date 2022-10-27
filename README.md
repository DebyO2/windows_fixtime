# windows_fixtime
does ur time gets messed up everytime u boot into windows after u had booted in ur ubuntu well heres the fix


# how does it work?
-the main script asks for time from a api using ur ip and returns the time

-i first made a caller script and i converted my main file into exe then put it in windows folder then put it's file name in the caller and then made a shortcut for caller and also placed in windows folder so now all i need to do is use win + r and type fixtime and it will ask for permissions and then run the file yay
very ducktaped but works

# how to replicate it?

* first put the exe file into the windows folder

* then make a shortcut of ur caller script , the pyw means it will not open a terminal for itself

* put the caller script shortcut in the windows folder , rename ur caller script shortcut to "timefix"

* now when u do win + r then in the run pop-up u can type the name of ur shortcut that is "timefix" and it will ask for permissions allow cuz u are changing system time so it needs those permissions

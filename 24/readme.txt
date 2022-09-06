first use gmane.py to spider every email from 'http://mbox.dr-chuck.net/sakai.devel/'
and then every email will save into content.sqlite, which will contain:
    1) unique id
    2) email adress send by
    3) time sent at
    4) subject
    5) headers
    6) body

then uses the gmodel.py to clean up the data for example:
    1) fix the sender(using mapping.sqlite) if some sender is changed(company name changed, etc).
    2) creat new tables storing every data thats cleaned up(which is making a multi relation data base).
    3) compress the header and the body useing zlib.

and then you can check useing gbasic.py prints:
    1) sourts howmany email is send by each email.
    2) prints the top what ever you want number of the emails(bised on howmany emails send).
    3) prints the top email organizations(also sourted by howmany email send).

next up you can use gword.py to do:
    1) scan throw all the messages for message.
    2) cleaning up each message.
    3) then using a loop to count each word in the message.
    4) produses a file named 'gword.js' that has the java scrip data that can be used to visualise.
then you can open gword.htm to visualise the data thats stored in side 'gword.js'

lastly use gline.py to swort:
    1) scan throw all the messages for sending organizations.
    2) scan for the month send for each organizations.
    3) loop throw each message to save it all into a dictonary.
    4) outputing all data as a java scrip file to 'gline.js'
then you can open gline.htm to visualise the data in 'gline.js'
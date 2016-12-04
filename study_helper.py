from datetime import datetime
from random import randint
import webbrowser
import time
now = datetime.now()
print "Hello , I am the study helper ."
if now.time() != "17:00:00.000000":
    print "Remember to backpack at 6:00 pm and remember this also that you had to study at 6:30 pm or 7:00 pm or early if you want ."
print "Study in thing just below is timepass ."
if randint(1,2) == 1:
    print "You will study in drawing room . "
else:
    print "You will study in poojaroom . "
webbrowser.open("http://www.textfixer.com/tools/random-choice.php")
periods = []
first_p = raw_input("What is the first period ? ")
periods.append(first_p)
second_p = raw_input("What is the second period ? ")
periods.append(second_p)
third_p = raw_input("What is the third period ? ")
periods.append(third_p)
fourth_p = raw_input("What is the fourth period ? ")
periods.append(fourth_p)
fifth_p = raw_input("What is the fifth period ? ")
periods.append(fifth_p)
sixth_p = raw_input("What is the sixth period ? ")
periods.append(sixth_p)
seventh_p = raw_input("What is the seventh period ? ")
periods.append(seventh_p)
eighth_p = raw_input("What is the eighth period ? ")
periods.append(eighth_p)
ninth_p = raw_input("What is the ninth period ? ")
periods.append(ninth_p)
for p in periods:
    print p
    time.sleep(30*60)
    webbrowser.open("C:\Users\SANJAY\Documents\Study Time.html")
which_subject = raw_input("Which subject do you want to study ? ")
if which_subject == "Hindi" or which_subject == "hindi" or which_subject == "HINDI":
    what_purpose = raw_input("What is your purpose further hindi ? ")
    if what_purpose == "VIDEO" or what_purpose == "Video" or what_purpose == "video":
        which_chapter = raw_input("Which chapter do you want to study in hindi ? ")
        webbrowser.open("https://www.google.co.in/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q="+which_chapter+"&tbm=vid")
    if what_purpose == "SOLUTION" or what_purpose == "Solution" or what_purpose == "solution":
        webbrowser.open("http://mycbseguide.com/downloads/cbse-class-07-hindi/1922/ncert-solutions/5/")
if which_subject == "Science" or which_subject == "science" or which_subject == "SCIENCE":
    what_purpose = raw_input("What is your purpose further science ? ")
    if what_purpose == "VIDEO" or what_purpose == "Video" or what_purpose == "video":
        webbrowser.open("http://mycbseguide.com/video/cbse-class-07-science/1525/")
    if what_purpose == "SOLUTION" or what_purpose == "Solution" or what_purpose == "solution":
        webbrowser.open("http://mycbseguide.com/downloads/cbse-class-07-science/1525/ncert-solutions/5/")
if which_subject == "MATHS" or which_subject == "Maths" or which_subject == "maths":
    what_purpose = raw_input("What is your purpose further maths ? ")
    if what_purpose == "VIDEO" or what_purpose == "Video" or what_purpose == "video":
        webbrowser.open("http://mycbseguide.com/video/cbse-class-07-mathematics/1509/")
    if what_purpose == "SOLUTION" or what_purpose == "Solution" or what_purpose == "solution":
        webbrowser.open("http://mycbseguide.com/downloads/cbse-class-07-mathematics/1509/ncert-solutions/5/")
if which_subject == "SST" or which_subject == "Sst" or which_subject == "sst":
    what_purpose = raw_input("What is your purpose further sst ? ")
    if what_purpose == "VIDEO" or what_purpose == "Video" or what_purpose == "video":
        print "If the chapter is not of geography than erase geography ."
        which_chapter = raw_input("Which chapter do you want to study in hindi ? ")
        webbrowser.open("https://www.youtube.com/results?search_query="+which_chapter+" geography")
    if what_purpose == "SOLUTION" or what_purpose == "Solution" or what_purpose == "solution":
        webbrowser.open("http://mycbseguide.com/downloads/cbse-class-07-social-science/1544/ncert-solutions/5/")
if which_subject == "SANSKRIT" or which_subject == "Sanskrit" or which_subject == "sanskrit":
    webbrowser.open("https://www.youtube.com/watch?v=CToOTFb6_jg&list=PL9vL8QnJ37pLZoSSkMwcUGWQ1mSZ7ndv0")
if which_subject == "ENGLISH" or which_subject == "English" or which_subject == "english":
    if randint(0,1) == 0:
        print "You will study coursebook today . "
    else:
        print "You will study workbook today . "
else:
    what_thing = raw_input("Then what do you want ? ")
    if what_thing == "TEST" or what_thing == "Test" or what_thing == "test":
        webbrowser.open("http://mycbseguide.com/onlinetest/")
    if what_thing == "PRACTICE" or what_thing == "Practice" or what_thing == "practice":
        webbrowser.open("http://mycbseguide.com/practice/")
    if what_thing == "WHATSAPP" or what_thing == "Whatsapp" or what_thing == "whatsapp":
        webbrowser.open("http://web.whatsapp.com")
    if what_thing == "MD" or what_thing == "Md" or what_thing == "md":
        print "FA-3 Modules :- "
        print " 15/11/16 - 17/11/16 = Hindi"
        print " 18/11/16 - 21/11/16 = Maths"
        print " 22/11/16 - 24/11/16 = English"
        print " 29/11/16 - 30/11/16 = Science"
        print " 01/12/16 -  3/12/16 = S.S.T."
        print " 05/12/16 -  7/12/16 = Sanskrit"
        print " 12/12/16 - 17/12/16 = Class Test"
    if what_thing == "CT" or what_thing == "Ct" or what_thing == "ct":
        print "12/12/16 - 17/12/16 = Class Test"
    if what_thing == "MOODLE" or what_thing == "Moodle" or what_thing == "moodle":
        webbrowser.open("http://ecourse.asu.apeejay.edu/my/")
    if what_thing == "FB" or what_thing == "Fb" or what_thing == "fb":
        webbrowser.open("http://epathshala.nic.in/e-pathshala-4/flipbook/")
    if what_thing == "OT" or what_thing == "Ot" or what_thing == "ot":
        webbrowser.open("http://mycbseguide.com/downloads/")
    if what_thing == "TT" or what_thing == "Tt" or what_thing == "tt":
        print
        print
        print "                     Time table              "
        print "_________________________________________________________"
        print "Day      1st | 2nd   | 3rd | 4th | 5th | 6th | 7th | 8th"
        print "Monday - Bio | Hindi | Art | Sans| Math| Phys| Eng | H&C"
        print "Tueday - Comp| H&C   | Phys| Math| Game| Eng | Chem| Hin"
        print "Wed    - Phys| Geo   | Math| Chem| Lib | Sans| Hin | Eng"
        print "Thurs  - Geo | Eng   | Comp| Chem| H&C | Math| G.K.| Hin"
        print "Friday - Bio | Maths | Comp| H&C | Hin | Geo | Mus | Eng"
        print "Sat    -  -  | Bio   | Sans| Hin | Math|Dance| Eng | Art"

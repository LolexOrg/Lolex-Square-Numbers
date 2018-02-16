import sys,os,subprocess,io,time
sys.path.insert(0, "./")
if not os.path.isfile("./squarenumber.py"):
    with open ("./squarenumber.py","a") as f: f.write("squarenumbers = 2\noriginsquare = 2")
    subprocess.call("./Squarensquare.py", shell = True)
import squarenumber
squarenumbers = squarenumber.squarenumbers
originsquare = squarenumber.originsquare
gone = 0
while True:
    squarenumbers = originsquare*originsquare
    originsquare = originsquare + 1
    print(squarenumbers)
    #time.sleep(0.2)
    gone = gone + 1
    if gone == 1000 or gone>1000:
        os.remove("./squarenumber.py")
        a = open("./squarenumber.py", "a")
        a.write("squarenumbers = ")
        a.write(str(squarenumbers))
        a.write("\noriginsquare = ")
        a.write(str(originsquare))
        a.close()
        gone = 0


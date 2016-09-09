import glob
import importlib
import random
import csv

def Test(studentModule, keyModule, gradewriter, numTests):
    mainTestFailed = 0
    funTestFailed = 0
    
    for i in range(0, numTests):
        # Main test
        if not fModule.Main() == keyModule.Main():
            mainTestFailed += 1
        
        # Fun test
        num = random.randint(0, 1000)
        text = random.choice(["h", "bee", "hi there", "", "ring"])
        if not fModule.Fun1(num, text) == keyModule.Fun1(num, text):
            funTestFailed += 1
    
    arr = [studentName, mainTestFailed, funTestFailed]
    gradewriter.writerow(arr)
    print(str(arr))

studentFiles = glob.glob('StudentFiles/*.py')
studentFiles.remove('StudentFiles/__init__.py')
with open('hw1.csv', 'wb') as csvfile:
    gradewriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    keyModule = importlib.import_module("Key")
    
    for fName in studentFiles:
        fFix = fName[:-3]
        addr = fFix.split("/")  
        fFix = ".".join(addr)
        studentName = addr[1].split("_")[2]
        
        try:
            fModule = importlib.import_module(fFix)
        except Exception:
            print studentName + ": failed to import."
            continue
            
        Test(fModule, keyModule, gradewriter, 100)
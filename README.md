
## Python program to solve the assignment problem using Hungarian method

## [Hungarian Assignment](https://en.wikipedia.org/wiki/Hungarian_algorithm "Wiki")

__Prerequisite__:

   We need to have python installed on your Windows/Linux machine. Just like we need a compiler for C++, we need the python interpreter installed. It is pre-installed on linux.

   [How to install python on Windows](http://www.howtogeek.com/197947/how-to-install-python-on-windows/)
   
#Direct Run
 
You can choose to run the program without installing python / tkinter. Navigate to Direct Executables folder
Run **hungarianAssignment.exe** to start the program.
Linux users may use wine to directly run the executable


#GUI MODEL

__Features__:

   Create any number of rows and columns.

   View the final result directly.  

   View step wise results.

   Save the result to a file.


For GUI to work correctly you need to install tkinter module on your machine.
    
    sudo pip install tkinter
    
    

**Usage**:

   Simply open up a terminal and run the program 
        
        python GUI_HA.py
        
![Start](http://i.imgur.com/4RTzmC5.jpg)
    
![Fill](http://i.imgur.com/I9MMm6Z.jpg)

![Result](http://i.imgur.com/uRbJ6wv.jpg)   

![Output](http://i.imgur.com/kh5Bmgu.jpg)
       


#Command Line Interface MODEL

**Usage**:

1) Use the input files present in the Testcases folder or 
   generate a new file with the following standards:
   
        N M
        A1 A2 A3 ...... AM
        B1 B2 B3 ...... BM
        ..................
        ..................
        ..................
        N1 N2 N2 ...... NM
   
    
   Where __N__ are the number of rows in the matrix and __M__ are the columns.
   
![Creating a file](http://i.imgur.com/hclDAaj.jpg)
   
 
Once the input file, say inputFile, is prepared run the program as follows:


  ```python
     python assignmentProb.py inputFile
  ```
  
![Running python](http://i.imgur.com/BQsIcwe.jpg)
   
   
   
  
 2)  Or you can simply use the already created 14 testcases using   
 
  ```python
     python assignmentProb.py TestCases/A/inputA
  ```
   
   
   
   

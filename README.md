## [Hungarian Assignment](https://en.wikipedia.org/wiki/Hungarian_algorithm "Wiki") ##
### Python program to solve the assignment problem using Hungarian method ###
----

### Motivation ###
```
During my four year undergraduate course majoring in Computer Science, we had an open elective course called as
Operations Research. It employs techniques from other mathematical sciences, such as mathematical modeling, 
statistical analysis,  and mathematical optimization, operations research arrives at optimal or near-optimal 
solutions to complex decision-making problems. It was taught by a teacher with a non programming background.

At the end of the course, the teacher requested students from C.S/E.C.E to submit a program that solves the job
assignment problem using the Hungarian method. Since, nobody from the class was interested, I took it up as a
challenge. First I solved the problem of creating a command line program that reads the input which the user 
provides in a file,  parses it and lists the maximum assignment possible using the Hungarian method. If no such
method is possible, we let the user know.

Before submitting the program as a python script, I realized that the teacher who requested the program shouldn't
be dealing with the nitty gritties of command line. Hence, I came across the tkinter Python library for creating 
GUI's. I researched for a day, and then went ahead executing the GUI with Tkinter. I was overjoyed.

However, once again I was in a fix because while preparing the GitHub readme, in the prerequisites section, I 
mentioned Python as it was necessary for the project. I was using a Linux Machine with all the utilities 
installed. It doesn't take a genius to figure out that the machine on which Sir would eventually run might not
even contain the python binary, let alone GUI support for Tkinter. We can't expect him to install python now,
can we?

At the end, I converted the python program to an .exe executable that's portable enough to run on most 
computers. I burnt the program onto a C.D, sparing him the troubles of git clone and submitted it to my professor.
Later that day, I received an email saying that the program was very helpful and he can now quickly create custom
questions and verify its correctness while checking the answer sheets. The fact that my GUI showed execution
traces and the steps it took, were the icing on the cake.

Needless, to say, I received the 'S' grade, which was the highest. Everybody in the batch now took a copy of my
program and submitted it. There were a lot of things I learnt in this project, both technical and psychological.
If I hadn't vouched for creating the program that day, you wouldn't be reading this and I would have remained 
remiss of the other aspects of programming.
```

----

## Prerequisite: ## 

   We need to have python installed on your Windows/Linux machine. Just like we need a compiler for C++, we need the python interpreter installed. It is pre-installed on linux.

   [How to install python on Windows](http://www.howtogeek.com/197947/how-to-install-python-on-windows/)

----

## Direct Run using binary (No installs needed) ##
 
You can choose to run the program without installing python / tkinter. Navigate to Direct Executables folder
Run ```hungarianAssignment.exe``` to start the program.
Linux users may use wine to directly run the executable

----

### Graphical Mode using Tkinter ###

* Create any number of rows and columns.

* View the final result directly.  

* View step wise results.

* Save the result to a file.


For GUI to work correctly you need to install tkinter module on your machine.
    
    sudo pip install tkinter
    
----    

### Usage (GUI) ###

   Simply open up a terminal and run the program 
        
        python GUI_HA.py

----

### Usage (Command Line Interface (CLI) MODE) ###

* Use the input files present in the Testcases folder or 
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
   
   
  
 *  Or you can simply use the already created 14 testcases using   
 
  ```python
     python assignmentProb.py TestCases/A/inputA
  ```
   
----

## Examples ##

### Example of a 4 x 4 matrix that's easily solvable by covering all zeroes ###
![Start](http://i.imgur.com/4RTzmC5.jpg) ![Fill](http://i.imgur.com/nJhx0bM.jpg)
![Result](http://i.imgur.com/uRbJ6wv.jpg) ![Output](http://i.imgur.com/kh5Bmgu.jpg)
       
----

### Example of a 5 x 5 matrix that requires a second pass ###

![5x5](https://user-images.githubusercontent.com/12872673/72884830-ccad8280-3d2c-11ea-866e-b83710dd9214.png)
![Initial reduced matrix](https://user-images.githubusercontent.com/12872673/72884928-f8306d00-3d2c-11ea-9fba-648e5cfe22b0.png)
![Covering zeroes](https://user-images.githubusercontent.com/12872673/72884987-0ed6c400-3d2d-11ea-8631-e60524b38299.png)
![Not optimal](https://user-images.githubusercontent.com/12872673/72885016-1dbd7680-3d2d-11ea-9c7a-c5853167d9e6.png)
![Prepare for second pass](https://user-images.githubusercontent.com/12872673/72885160-670dc600-3d2d-11ea-95b0-1efdbae28c31.png)
![Updated lines](https://user-images.githubusercontent.com/12872673/72885222-7b51c300-3d2d-11ea-8c99-252892445719.png)
![Optimal result](https://user-images.githubusercontent.com/12872673/72885249-87d61b80-3d2d-11ea-8718-5def63c95442.png)

Note that this sample case was taken from [here](http://ecoursesonline.iasri.res.in/mod/resource/view.php?id=4955) at Example 2

----

### I want to contibute ###
Please fork the project and submit a PR


----

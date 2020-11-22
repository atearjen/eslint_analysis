# eslint_analysis #
Finding the correlation of eslint result with npm package popularity 


# File Order # 
1) npminstall.py. 
2) githubClone.py. 
3) eslintDirs.py. 
4) eslintParser.py. 

## Order does Matter!! ##
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; eslintDirs.py  is dependent on githubClone.py  , file 4 is dependent on file 3. 


# How to Run the files # 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. ``` python3 filename.py ``` in the terminal. 


# OverWrite My Textfiles # 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. in npmpackages.txt for example, those are packages 2790 -2990, if you want packages 0-200 or the middle 200.   
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Copy your selection from the google drive, and paste over the text file ( CMD/CTRL + A, CTRL/CMD + C).  
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; on Excel/Drive, (CMD/CTRL + A, Ctrl/CMD + P) on your. text editor,  I used Sublime. 


#### GitHub Clone will create a lot of directories, make sure to run a script in a giant directory #### 
#### EslintDirs will create a lot of text files, make sure when you are running it that you are in a directory you want to be in ####

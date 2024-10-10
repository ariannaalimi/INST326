"""A template for a python script deliverable for INST326.
Driver: Arianna Alimi
Navigator: None
Assignment: Template INST326
Date: 9_18_24
Challenges Encountered: I had some challenges with the line strip and looping through the filename. However I was able to resolve these issues
"""

def line_length(filename, lineReturn = 3):
    """
    Returns the length of a specific line read in a file

    Arguments:
    filename(str): the filename that is being read
    lineReturn(int): the line of the file being read

    Returns:
    int : length of the line

    """

    
    x = 1 #loop increment
    try:
        with open(filename, 'r') as f:
            for line in f: #loops through the file lines
                if (x != lineReturn): #if it is not the line wanted, continue looping
                    x += 1
                    continue
                
                if (x == lineReturn): #if it is line wanted, return length of line
                    return len(line.rstrip('\r\n')) + 1 #ChatGPT, needed help with the rstrip part
        
    except FileNotFoundError: #throw exception if file was not found
        return f"File {filename} does not exist"

def find_string(filename, lineReturn, charStart = 0, charEnd = 1):
    """
    Returns the characters of a specific line from the charStart to charEnd

    Arguments:
    filename(str): name of the file being read
    lineReturn(int): specific line that is being read
    charStart(int): the index of the first character of the line
    charEnd(int): the index of the last character of the line

    Returns:
    theLine(str): returns the line of characters that user wanted when inputting lineReturn, charStart and charEnd

    """


    x = 1 #loop increment
    theLine = "" #line needed to return

    with open(filename, 'r') as f:
        for line in f: #loops through file lines
            if(x == lineReturn): #if wanted line:
                for i in range(charStart, charEnd): #loop through the lines characters from wanted start to wanted end
                                                        #We have to do charEnd + 1 since range ends 1 below
                    theLine += line[i] #add the character to the line string from charStart to charEnd
                return theLine
            if (x != lineReturn): #if line is not wanted, increment x and continue looping
                x += 1
                continue

"Question 2: Yes, there are docstrings in the program"
"Question 3: The context manager is used when opening and reading a file"
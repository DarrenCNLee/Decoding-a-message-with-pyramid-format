import sys 

# The decode function creates a dictionary to map the line numbers to the word on that line numbers. 
# The keptLines list includes all the numbers at the end of each pyramid line such as 1, 3, 6, etc.
# After reading the message_file line by line and creating the mappings of line numbers to words,
# the function concatenates each word for each pyramid line end number to the decoded string then 
# that string.
def decode(message_file):
    numToWord = {}
    keptLines = []
    
    numLines = 0
    row = 0
    col = 0
       
    # read the file line by line
    while True:
        line = message_file.readline().split()
        if not line:
            break
        lineNum, word = line
        # map each line number to the word on that line
        numToWord[int(lineNum)] = word
        numLines += 1
        
    # create the list of numbers at the end of each pyramid line
    # these are the lines that we need for the decoded string
    while col < numLines:
        row += 1
        col += row 
        keptLines.append(col)
    
    decodedString = ""   
    # concatenate all the words that we need to the decoded string
    for num in keptLines:
        decodedString += numToWord[num] + " "
        
    return decodedString.rstrip()

def main():
    infile = open(sys.argv[1], "r")
    outfile = open(sys.argv[2], "w")
    
    outfile.write(decode(infile))
    
    infile.close()
    outfile.close()    
        
if __name__ == "__main__":
    main()
    
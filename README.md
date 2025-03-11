# Decoding-a-message-with-pyramid-format

Implements a function named decode(message_file). This function should read an encoded message from a .txt file and return its decoded version as a string. The function must be able to process an input file with the following format:

3 love
6 computers
2 dogs
4 cats
1 I
5 you
In this file, each line contains a number followed by a word. The task is to decode a hidden message based on the arrangement of these numbers into a "pyramid" structure. The pyramid increases by one number per line, like so:

  1
 2 3
4 5 6
The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line (in this example, 1, 3, and 6). You should ignore all the other words.

https://stackoverflow.com/questions/77883772/decoding-a-message-from-a-text-file-issue-with-formatting

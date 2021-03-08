if __name__ == '__main__':
    """
        How do you open a file?
         
        There's a built-in-function
    
        File name is a string, literal, or a variable.
        
    """
    if False:
        x = 3
        # pycharm is reading everything as being based in the main directory.
        # because we're in a subdirectory, we need to tell it that.
        # two ways to denote directories
        # my_file_name = 'files_dir\\blah.txt'
        my_file_name = 'files_dir/blah.txt'  # this one is best
        print(my_file_name)
        # reason is, \\ are an escape sequence which stands for one backslash
        # backslashes are the windows style directory markings, forward slash is linux/mac style
        # you can always use the linux style even in windows, and python generally fixes it up for you.
        # \\ like \n \r \t (\a <-- doesn't always work) ...
        """
            3 modes in python, read, write, and append
            for now, let's talk about read mode.
            
            Accidentally just try to read from the file name string, rather than the file itself.
            Open is a function that takes two strings, file_name, mode, returns "file" object    
        """
        my_file = open(my_file_name)  # we're in read MODE, default is 'r'
        print(my_file.read())
        # .read() reads the entire file at once
        # .read() can be dangerous if you don't know that the file will be small.  Take a long time.
        # most of the time you won't use read, but you should know it exists and use it if it makes sense
        my_file.close()
        # tells the OS (windows/linux/mac) that we're finished looking at the file

        my_file = open(my_file_name, 'r')  # we're in read MODE
        # the plural one, readlines makes a list of the lines
        the_lines = my_file.readlines()  # creates a list of each line
        print(the_lines[3])
        for line in the_lines:
            print(line)
            # if you haven't stripped the new line, there will be two newlines
            print(line.strip('\n'))
            print(line, end="")

        print('\n\n\n')

        # little hiccup in the function.  (not a bug, it's a feature)
        # my_file.read().split('\n') and my_file.readlines()  readlines will still have the newline characters...
        # a bit subtle maybe?
        my_file.close()

        my_file = open(my_file_name, 'r')  # we're in read MODE

        """
            How can we explain this behavior?
                a file has a "cursor"
                it's a place where the OS thinks is the current position.  
        """
        my_line = my_file.readline()
        while my_line:
            print("here is a line: " + my_line.strip('\n'))
            my_line = my_file.readline()
            # when my_file.readline() reaches "EOF = end of file" then it'll return empty string
            # empty string evaluates to false.

        my_file.close()

        """
            Elegant, beautiful, great way to do it.
            Use python's in-built iteration processes
        """

        my_file = open(my_file_name)
        # most common way to read
        for my_line in my_file:
            print('iteration is great\t', my_line.strip())
        # python is basically saying to the file "what's next?"
        # the file will call readline for you and put that result into the variable.

        # not closing a file in read mode == not the end of the world, you're going to be ok
        my_file.close()
        # not closing a file in write mode == 'unpredictable... scary times'

        """
            Write and Append modes
                Write mode.
                
                
        """
        write_file_name = 'files_dir/movies.txt'
        write_file = open(write_file_name, 'w')

        movie_name = input('Tell me movie: ')
        while movie_name != 'quit':
            # difference between these two is that write takes a string, writelines takes a List[str]
            write_file.write(movie_name + '\n')
            # readlines /read/readline does not REMOVE a newline character
            # write does not add newline characters
            # have to add the new line in
            movie_name = input('Tell me movie: ')

        # naughty human
        write_file.close()
        input('This is useless just a placeholder, hang on...')
        """
            Massive warning, danger label on 'w' mode.  
            
            Write mode will annihilate your file, set it to empty, delete everything, goodbye file contents
        """
        write_file = open(write_file_name, 'w')

        book_name = input('Tell me book: ')
        while book_name != 'quit':
            # difference between these two is that write takes a string, writelines takes a List[str]
            write_file.write(book_name + '\n')
            # readlines /read/readline does not REMOVE a newline character
            # write does not add newline characters
            # have to add the new line in
            book_name = input('Tell me book: ')

        write_file.close()

        """
            Maybe you don't want that... there's a slight compromise way to do that
            
            mode = 'a' = append mode
            Opens the file (just like write mode)
            Sets the cursor to the end
            Doesn't blank the file
            Is ready to write.  
        """
        append_file = open(write_file_name, 'a')  # uber-mega-definitely important to get right.

        book_name = input('Tell me game: ')
        while book_name != 'quit':
            # difference between these two is that write takes a string, writelines takes a List[str]
            append_file.write(book_name + '\n')
            # readlines /read/readline does not REMOVE a newline character
            # write does not add newline characters
            # have to add the new line in
            book_name = input('Tell me game: ')

        append_file.close()

        """
            Rule: it takes about 2-3x as long as i think to do any given task.  There we go.  
        """
    new_test = 'files_dir/test.txt'
    new_test_file = open(new_test, 'w')
    # test.txt didn't exist until i created it with this command.
    lines = ['apple', 'bag', 'cheese', 'dog']
    for i in range(len(lines)):
        # definitely have to add the newlines
        lines[i] = lines[i] + '\n'

    new_test_file.writelines(lines)
    # I didn't think writelines (even though you might think based on the name... ) added the \n characters
    # as it turns out i was actually right, huh...
    new_test_file.close()

"""
    All you need to know is r, w, a.

    You probably won't need byte mode unless I specify.
    You won't need the + modes.  r+, w+, a+ all kinds of weird partial modes read/write 
"""
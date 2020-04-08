#Importing the required module.
import os

#Function to list oout all the files with the .c extension.

def list_files_in_dir(search_dir):

    #Base case - If we have a file we just print out the name and return.
    if os.path.isfile(search_dir):
        if search_dir.endswith(".c"):
                print(search_dir)
        return
    #Otherwise all we have to do is to recursively go inside the directory to search for the files in that
    #directory
    arr = os.listdir(search_dir)
    for i in arr:
        list_files_in_dir(search_dir+"/"+i)

#We get the path of the directory this file is present in.
def get_c_files(testdir):
    curr_path = os.getcwd()

#We specify the path to the diirectory where we want to search our files.
    search_dir = curr_path + "/"+testdir


#We call the recursive function to list out all the files that have the .c extension.
    list_files_in_dir(search_dir)

#Testcase1  : testdir
print("For testcase 1")
get_c_files("testdir")
#Testcase2  : testdir
print("For testcase 2")
get_c_files("testdir1")
#Testcase3  : testdir
print("For testcase 3, Edge case, no c files")
get_c_files("testdir2")
'''
Outputs for test cases.

Note: The directories are present in the zipped file. 

For testcase 1
/home/learner/Desktop/raghavddps2/UD_DSA/Course1/Project1 - Show me the data structures/Problem 2/testdir/subdir5/a.c
/home/learner/Desktop/raghavddps2/UD_DSA/Course1/Project1 - Show me the data structures/Problem 2/testdir/subdir3/subsubdir1/b.c
/home/learner/Desktop/raghavddps2/UD_DSA/Course1/Project1 - Show me the data structures/Problem 2/testdir/t1.c
/home/learner/Desktop/raghavddps2/UD_DSA/Course1/Project1 - Show me the data structures/Problem 2/testdir/subdir1/a.c

For testcase 2
/home/learner/Desktop/raghavddps2/UD_DSA/Course1/Project1 - Show me the data structures/Problem 2/testdir1/sub4/r.c
/home/learner/Desktop/raghavddps2/UD_DSA/Course1/Project1 - Show me the data structures/Problem 2/testdir1/sub5/t.c
/home/learner/Desktop/raghavddps2/UD_DSA/Course1/Project1 - Show me the data structures/Problem 2/testdir1/sub3/a.c
/home/learner/Desktop/raghavddps2/UD_DSA/Course1/Project1 - Show me the data structures/Problem 2/testdir1/sub6/45.c
/home/learner/Desktop/raghavddps2/UD_DSA/Course1/Project1 - Show me the data structures/Problem 2/testdir1/sub6/rtf/1.c
/home/learner/Desktop/raghavddps2/UD_DSA/Course1/Project1 - Show me the data structures/Problem 2/testdir1/sub2/su1/dsc2/1.c
/home/learner/Desktop/raghavddps2/UD_DSA/Course1/Project1 - Show me the data structures/Problem 2/testdir1/sub2/su1/dsc2/5.c
/home/learner/Desktop/raghavddps2/UD_DSA/Course1/Project1 - Show me the data structures/Problem 2/testdir1/sub2/q.c
/home/learner/Desktop/raghavddps2/UD_DSA/Course1/Project1 - Show me the data structures/Problem 2/testdir1/sub1/1.c
/home/learner/Desktop/raghavddps2/UD_DSA/Course1/Project1 - Show me the data structures/Problem 2/testdir1/sub1/sub2/1.c
/home/learner/Desktop/raghavddps2/UD_DSA/Course1/Project1 - Show me the data structures/Problem 2/testdir1/sub1/sub2/2.c
/home/learner/Desktop/raghavddps2/UD_DSA/Course1/Project1 - Show me the data structures/Problem 2/testdir1/sub1/sub1/1.c

For testcase 3
None
'''
'''
4. Experiment with 'glob' (see below)

Using the glob library you can more easily open a set of files.  Notice how I use the shell '*' character to match *_cdp.txt.  I could then open all of these files and process the data inside of them.

>>>> CODE <<<<

# This code assumes that all of the CDP files are in a subdirectory called 
# CDP_DATA beneath the current working directory 

>>> from glob import glob
>>> cdp_files = glob('CDP_DATA/*_cdp.txt')

>>> cdp_files
['CDP_DATA/r1_cdp.txt', 'CDP_DATA/r2_cdp.txt', 'CDP_DATA/r3_cdp.txt',  'CDP_DATA/sw1_cdp.txt', 'CDP_DATA/r4_cdp.txt', 'CDP_DATA/r5_cdp.txt']

>>>> END CODE <<<<
'''

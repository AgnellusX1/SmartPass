import re
from progress.bar import Bar
# Progress Bar
bar = Bar('Processing', max=20)

dataset = open (r"Dataset/rockyou", "r",encoding='latin-1')
# Regex Statements
'''
'''
pattern = '[!@#$%^&*(),.?":{}|<>]'
file_num = open ("Dataset/specialChar", "w",encoding='latin-1')
for i in dataset:
    x = re.search (pattern, i)
    if x:
        print ("Adding " + x.string)
        file_num.write (x.string)
        bar.next()
bar.finish()
file_num.close ()
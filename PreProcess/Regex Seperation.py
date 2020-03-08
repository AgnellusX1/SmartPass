import re
from progress.bar import Bar

# Progress Bar
bar = Bar('Processing', max=20)

dataset = open(r"Datasets/xato.txt", "r", encoding='latin-1')
# ADD the Regex Statements here Regex Statements
'''

    Only character Lowercase
    Only Numbers
    Only Characters (Upper Case + Lower Case)
    Starting with Numbers containing Special characters
    Staring with Characters containing Numbers
    
    NOTE: Change the File Name Each time
    
'''
pattern = "[A-Z]"
file_num = open("Datasets/Processed/lower", "w", encoding='latin-1')
l = dataset.readlines()
for i in l:
    x = re.search(pattern, i)
    if x:
        print("Adding " + x.string)
        file_num.write(x.string)
        bar.next()
bar.finish()
file_num.close()

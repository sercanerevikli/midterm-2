def printingShareHolder(shareList,shares):
    l = len(sharesList)
    needed = sharesList[0]

    count = 1
    while count != l:
        if needed > shares/2:
            print('You need the support of top', count,'shareholders for this number of votes')
            count = l;
        else:
            count = count + 1
            needed = needed + sharesList[count]
    filename = input("enter the file name to save: ")
    f = open("C:/Users/SERCAN/Desktop/mıdterm2file/{}". format(filename), "w") #I USE FILE DIRECTORY FOR THE CREATING FILE YOU CAN CHANGE THE DIRECTORY IF YOU WANT
    f.write("-----Sharers-----\n")
    f.write("Total Share Count:{}\n". format(shares))
    f.write("Need Share For Majority:{}\n". format(int(shares/2)))
    f.write("Need the support of top shareholders:{}\n". format(count))
    f.close()



inp = 1
shares = 0
sharesList = []

while inp != int(0):
    inp = int(input("Please enter the number of shares: "))
    shares = shares + int(inp)
    if inp < 0:
        print("Invalid input!")
    elif inp > 0:
        sharesList.append(inp)
print(sharesList)

print('Thank you! There is a total of', shares, 'shares represented here.')
print('Shares needed for majority vote is ', int(shares/2), '.')

sharesList.sort()
sharesList.reverse()

fileindex = printingShareHolder(sharesList,shares)
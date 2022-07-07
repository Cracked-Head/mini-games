def printPicnic(items,leftWidth,rightWidth):
    print('Picnic Table'.center(leftWidth+rightWidth,'-'))
    for k,v in items.items():
        print(k.ljust(leftWidth,'.')+str(v).rjust(rightWidth))
        
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
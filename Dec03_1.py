#!/usr/bin/env python
# coding: utf-8

# In[5]:


from pprint import pprint
   
def allCharsAreDots(s):
    return all(c == '.' for c in s)
   
schem = []
sum = 0
with open("parts.txt") as fin:
    for line in fin:
        schem.append(line.strip())
    pprint(schem)
    # Use last line to determine row length
    row_len = len(line.strip())
    for row in range(len(schem)):
        print('row ', row)
        col = 0
        start = -1
        end = -1
        while col < row_len:
            # Determine start and end of each sequence of digits
            #print(schem[row][col])
            if schem[row][col].isdigit():
                if start == -1:
                    start = col
                if col == row_len - 1:
                    end = row_len
            else:
                if start != -1:
                    end = col
            # Start and end were found.
            # Check above, below, and left and righ of group of digits for non-dot chars
            if start != -1 and end != -1:
                # Get part number
                part = int(schem[row][start:end])
                print('row ', row, start, end, part)
                # Check left side if number does not start in col 0
                if start > 0:
                    # Adjust start to check left side on same row and diags for above and below on left side
                    start -= 1
                    print('left ', schem[row][start])
                    if schem[row][start] != '.':
                        sum += part
                        print('sum ', sum)
                        if end >= row_len - 1:
                            break
                        start = -1
                        end = -1
                        continue
                # Check right side if end is not at end of row
                if end != row_len:
                    print('right ', schem[row][end])
                    if schem[row][end] != '.':
                        sum += part
                        print('sum ', sum)
                        if end == row_len - 1:
                            break
                        start = -1
                        end = -1
                        continue

                # Adjust end to check diagonals above and below
                if end < row_len - 1:
                    end += 1
                # Check above
                if row > 0:
                    print('above ', schem[row-1][start:end])
                    if not allCharsAreDots(schem[row-1][start:end]):
                        sum += part
                        print('sum ', sum)
                        if end >= row_len - 1:
                            break
                        start = -1
                        end = -1
                        continue;
                # Check below
                if row < len(schem) - 1:
                    print('below ', schem[row+1][start:end])
                    if not allCharsAreDots(schem[row+1][start:end]):
                        sum += part
                        print('sum ', sum)
                        if end >= row_len - 1:
                            break
                        start = -1
                        end = -1
                        continue;
    
                if end > row_len - 1:
                    break
                start = -1
                end = -1
    
            col += 1
                       
    print('total: ', sum)            


# In[ ]:







"""
Strategy:
Consider the harvest area as a moving sub-matrix hovering over the farm from its top left to its bottom right;
calculate as follows:
1.initially, place the moving sub-matrix over the top-left-most corner of farm and calculate total fruit inside it (@total_fruit)
and set it to max no. of fruit harvested (@max_harvest);
2.save @total_fruit to a var (@total_fruit0) whenever we find ourselves back again hovering over the left-most border of farm;
3.sum the total fruit in top-most row and save it to a var (@total_row_0), if we happen to focus on left-most border of farm;
4.sum the total fruit in left-most column of sub-matrix and save sum in a var (@total_col_0);
5.move the sub-matrix one column to the right;
6.subtract @total_col_0 from the total fruit we had before (@total_fruit <- @total_fruit - @total_col_0);
7.sum the total fruit in the right-most column of harvest area we've just moved to the right and add it to previous sum
(@total_fruit <- @total_fruit + @total_col_1)
8.replace @max_harvest with @total_fruit if @total_fruit > @max_harvest (what if we find 2 areas with same maximum result???)
9.continue from 5. until our sub-matrix hits right-most border of farm or we've scanned whole farm
10.re-focus sub-matrix over left-most border of farm
11.slide down sub-matrix one row
12.retrieve previous left-most total fruit count again (@total_fruit <- @total_fruit0) (see 2.)
13.subtract @total_row_0 from @total_fruit (@total_fruit <- @total_fruit - @total_row_0)
14.calculate total fruit in bottom-most row of current harvest area and add it to @total_fruit
15.compare @max_harvest again with current @total_fruit and replace it with @total_fruit if @total_fruit > @max_harvest
16.repeat from 5;

"""

# read input
l, c, m, n = (int(x) for x in input().split())
# pre-allocate farm mtx static mem
farm = [0 for x in range(l)]
# input fruit info into farm
for i in range(l):
    farm[i] = [int(x) for x in input().split()]


# calculate total fruit within submatrix defined by row column pairs (r1, c1) -> (r2, c2)
def calc_total_fruit(r1, c1, r2, c2):
    total = 0
    col = c1
    while r1 < r2:
        total += farm[r1][col]
        col += 1
        if col > c2:
            col = c1
            r1 += 1
    return total


# 1.initially, place the moving sub-matrix over the top-left-most corner of farm and 
# calculate total fruit inside it (@total_fruit); set it to max no. of fruit harvested (@max_harvest);
row0 = col0 = 0             # matrix row and column cell pointers
max_harvest = 0             # accumulator for max. fruit count in sub-matrix
while row0+m < l+1:
    total_fruit = calc_total_fruit(row0, col0, row0 + m, col0 + n - 1)
    if total_fruit > max_harvest:
        max_harvest = total_fruit
    # 2.save @total_fruit to a var (@total_fruit0) whenever we find ourselves 
    # back again hovering over the left-most border of farm;
    if col0 == 0:
        total_fruit_0 = total_fruit
        # 3.sum the total fruit in top-most row of current sub-matrix position and save it to a var (@total_row_0),
        # if we happen to focus on left-most border of farm;
        total_row_0 = calc_total_fruit(row0, col0, row0, col0)
        # 4.sum the total fruit in left-most column of sub-matrix and save sum in a var (@total_col_0);
        total_col_0 = calc_total_fruit(row0, col0, row0 + m, col0)
        # 5.move the sub-matrix one column to the right;
    col0 += 1
    # 10.re-focus sub-matrix over left-most border of farm
    if col0 + n == c + 1:
        col0 = 0
        # 11.slide sub-matrix down one row
        row0 += 1
        # 12.retrieve previous left-most total fruit count again (@total_fruit <- @total_fruit0) (see 2.)
        total_fruit = total_fruit_0
        # 13.subtract @total_row_0 from @total_fruit (@total_fruit <- @total_fruit - @total_row_0)
        total_fruit = total_fruit - total_row_0
        # 14.calculate total fruit in bottom-most row of current harvest area and add it to @total_fruit
        total_fruit += calc_total_fruit(row0 + m - 1, col0, row0 + m - 1, col0 + n - 1)
    else:
        # 6.subtract @total_col_0 from the total fruit we had before (@total_fruit <- @total_fruit - @total_col_0);
        total_fruit = total_fruit - total_col_0
        # 7.sum the total fruit in the right-most column of harvest area we've just moved to the right
        # and add it to previous sum (@total_fruit <- @total_fruit + @total_col_1)
        total_fruit = total_fruit + calc_total_fruit(row0, col0 + m - 1, row0 + n - 1, col0 + m - 1)

    # 8.replace @max_harvest with @total_fruit if @total_fruit > @max_harvest
    # (what if we find 2 areas with same maximum result??? Which one are we supposed to report?Both?)
    if total_fruit > max_harvest:
        max_harvest = total_fruit

print(max_harvest)










from sys import stdin

engine = []
for line in stdin:
    engine.append( "." + line[:-1] + "." )

engine.append( "." * len(engine[1]) )
engine.insert( 0, "." * len(engine[1]) )

partnumbers_sum = 0
gears = {}
ratios_sum = 0

i = 0
while i < len(engine):
    j = 0
    while j < len( engine[i] ):

        if engine[i][j].isdigit():
            i_level = i
            j_start = j
            while engine[i][j].isdigit():
                j += 1
            j_end = j
            number = int( engine[i][j_start:j_end] )

            found_symbol = False
            gears_on_this_number = []
            for check_i in range( i-1, i+2):
                for check_j in range( j_start-1, j_end+1 ):
                    if engine[check_i][check_j] == "." or engine[check_i][check_j].isdigit():
                        continue
                    elif engine[check_i][check_j] == "*":
                        found_symbol = True
                        gear_coord = str(check_i) + "," + str(check_j)
                        if gear_coord in gears:
                            gears[ gear_coord ].append( (number, i_level, j_start) )
                        else:
                            gears[ gear_coord ]   = [ ( (number, i_level, j_start) ) ]
                    else:
                        found_symbol = True

            if found_symbol:
                partnumbers_sum += number
                print(number, partnumbers_sum)

        j += 1
    i += 1

for g in gears:
    if len( gears[g] ) == 2:
        ratios_sum += gears[g][0][0] * gears[g][1][0]

print(ratios_sum)

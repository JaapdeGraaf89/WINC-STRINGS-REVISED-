# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1 

scorer_0 = "Ruud Gullit"
scorer_1 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = scorer_0 + " " + str(goal_0) + "," + " "+ scorer_1 + " " + str(goal_1)   # Spaties tussen + operator gedaan.

print(scorers)

report = f"{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute"    # F-Strings, de haakjes verwijderd. 

print(report)

# Part 2 

player = "Sergey Gotsmanov"
first_name = player[:player.find(" ")]
last_name_len = len(player[player.find(" ") +1:])   # Gebruik van .find zodat de invoer generiek kan zijn. 
print(player)


name_short_firstletter = player[0]
name_short_full_last= (player[player.find(" ") +1:]) # Zelfde methode toegepast. Nu alleen echter om ipv de Lengte van string, de substring er uit te pakken. 

name_short = f'{name_short_firstletter}. {name_short_full_last}'
print(name_short)

exclamation_mark= "!"
chant = (f'{first_name}{exclamation_mark} '*len(first_name))
chant = chant.rstrip()                                       # Overbodige chant_trim verwijderd. 

print(chant)

good_chant = chant[-1] != " "
print(good_chant)
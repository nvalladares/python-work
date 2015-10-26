# # # ------ Exercise 1
# # print "Hello world!"
# # print "Hello again"
# # print "I like typing this."
# # print "This is fun."
# # print 'Yay! printing.'
# # print "I'd much rather You 'not'."
# # print 'I "said" do not touch this.'
# # print "Cats are awesome!"
# # # print "cats are better than dogs!"

# # # -------- Exercise 2
# # # A comment, this is so you can read your program later.
# # # Anything after the # is ignored by python.

# # print "I could have code like this." # and the comment after is ignored

# # # You can also use a comment to "disable" or comment out a piece of code:
# # # print "This won't run."

# # print "This will run."

# # --------- Exercise 3
# # prints "I will now count my chickens"
# print "I will now count my chickens:"

# # adds 25+30 and divides the answer by 6 and prints the answer = 30
# print "Hens", 25 + 30 / 6

# # * and % take precedence over -, so we first evaluate 25 * 3 % 4.  * and % have the same priority and associativity from left to right, so we evaluate from left to right, starting with 25 * 3. This yields 75. Now we evaluate 75 % 4, yielding 3. Finally, 100 - 3 is 97. 
# print "Roosters", 100 - 25 * 3 % 4

# # prints "Now I will count the eggs"
# print "Now I will count the eggs:"

# # the answer is 7. The % (modulo) operator yields the remainder from the division of the first argument by the second. The numeric arguments are first converted to a common type. A zero right argument raises the ZeroDivisionError exception. The arguments may be floating point numbers, e.g., 3.14%0.7 equals 0.34 (since 3.14 equals 4*0.7 + 0.34.) The modulo operator always yields a result with the same sign as its second operand (or zero); the absolute value of the result is strictly smaller than the absolute value of the second operand [2].
# print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
# print "Is it true that 3 + 2 < 5 - 7?"
# print 3 + 2 < 5 - 7
# print "What is 3 + 2?", 3 + 2
# print "What is 5 - 7?", 5 - 7
# print "Oh, that's why it's False."
# print "How about some more."
# print "Is it greater?", 5 > -2
# print "Is it greater or equal?", 5 >= -2
# print "Is it less or equal?", 5 <= -2

# -------- Exercise 4

# variable 'cars' has a value of 100
# cars = 100

# variable for 'space in a car' has a value of 4.0
# space_in_a_car = 4.0

# variable for 'drivers' has a value of 30
# drivers = 30

# variable for 'passengers' has a value of 90
# passengers = 90

# var 'cars not driven' value is the difference of 'cars' - 'drivers'
# cars_not_driven = cars - drivers

# var for 'cars driven' is equal to 'drivers'
# cars_driven = drivers

# var 'carpool capacity' is the product of 'cars driven' * 'space in a car'
# carpool_capacity = cars_driven * space_in_a_car

# var 'average of passengers per car' takes average of 'passengers' divided by 'cars driven'
# average_passengers_per_car = passengers / cars_driven

# outputs value of var 'cars' (100)
# print "There are", cars, "cars available."

# outputs value of var 'drivers' (30)
# print "There are only", drivers, "drivers available."

# outputs difference of 'cars' - 'drivers'
# print "There will be", cars_not_driven, "empty cars today."

# outputs value of var 'carpool capacity' which is the product of 'cars driven' * 'space in a car'
# print "We can transport", carpool_capacity, "people today."

# outputs value of var 'passengers' (90)
# print "We have", passengers, "to carpool today."

# outputs average of 'passengers' divided by 'cars driven'
# print "We need to put about", average_passengers_per_car, "in each car."

# --------------- Exercise 5

my_name = 'Frodo Baggins'
my_age = 33 # when I left the Shire
my_height = 42 # inches
my_weight = 80 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on how close to Mordor he is." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)



















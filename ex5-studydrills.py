name = 'Lynn'
age = 25 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Black'
teeth = 'White'
hair = 'Black'
height_cm = height * 2.54
weight_kg = weight * 0.4535924

print "Let's talk about %s." % name
print "He's %d cm tall." % height_cm
print "He's %d kg heavy." % weight_kg
print "Actually that's not too thin."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height_cm, weight_kg, age + height_cm + weight_kg)


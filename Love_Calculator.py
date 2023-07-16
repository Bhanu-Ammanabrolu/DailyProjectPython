print("--------Welcome to the LOVE CALCULATOR!--------")

name1 = input("Love Bird 1 Name: ").lower()
name2 = input("Love Bird 2 Name: ").lower()

Birds_together = name1 + name2

t_occurs = Birds_together.count("t")
r_occurs = Birds_together.count("r")
u_occurs = Birds_together.count("u")
e1_occurs = Birds_together.count("e")

total1 = t_occurs + r_occurs + u_occurs + e1_occurs

l_occurs = Birds_together.count("l")
o_occurs = Birds_together.count("o")
v_occurs = Birds_together.count("v")
e_occurs = Birds_together.count("e")

total2 = l_occurs + o_occurs + v_occurs + e_occurs

result = int(str(total1) + str(total2))

if result < 10 or result > 90:
    print(f"your score is {result}, Time to run away")
elif result >= 40 & result <= 50:
    print(f"Your score is {result}, Stick together!")
else:
    print(f"Your Score is {result}, On your choice")

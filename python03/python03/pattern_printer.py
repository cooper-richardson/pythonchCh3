stars = ""
number = int(input("How many stars?: "))
for count in range(number):
    stars = stars + "*"
    #Since stars is not an integer, adding adds the character to the end
    print(stars)
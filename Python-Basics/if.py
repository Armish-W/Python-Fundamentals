# num=input("Enter a Number:")
# num=int(num)
# if num%2==0:
#     print(num, "is an even number.")
# else:
#     print(num, "is an odd number.")

# Pakistani_Cuisine=['Biryani','Nihari','Daleem']
# Indian_Cuisine=['Bara pav', 'Rajma chawal', 'Samosa']
# Chinese_Cuisine=['Egg Fried Rice', 'Chowmein', 'Chicken Mongolian']
# Food=input("Enter food name, I will tell you which cuisine it belongs to:").strip()
# if Food in Pakistani_Cuisine:
#     print(Food,"belongs to Pakistani Cuisine.")
# elif Food in Indian_Cuisine:
#     print(Food,"belongs to Indian_Cuisine.")
# elif Food in Chinese_Cuisine:
#     print(Food,"belongs to Chinese_Cuisine.")
# else:
#     print("Due to my limited knowledge, I don't know which cuisine your food belongs to.")
Pakistani_Cuisine = ['biryani', 'nihari', 'daleem']
Indian_Cuisine = ['bada pav', 'rajma chawal', 'samosa']
Chinese_Cuisine = ['egg fried rice', 'chowmein', 'chicken mongolian']

# .strip() removes outer spaces, .lower() ignores upper/lower casing
raw_food = input("Enter food name, I will tell you which cuisine it belongs to: ").strip()
food_lower = raw_food.lower()

if food_lower in Pakistani_Cuisine:
    print(f"{food_lower.title()} belongs to Pakistani Cuisine.")
elif food_lower in Indian_Cuisine:
    print(f"{food_lower.title()} belongs to Indian Cuisine.")
elif food_lower in Chinese_Cuisine:
    print(f"{food_lower.title()} belongs to Chinese Cuisine.")
else:
    print("Due to my limited knowledge, I don't know which cuisine your food belongs to.")
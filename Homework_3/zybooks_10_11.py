#  Helmut Brenner  #
#  2037275 #

class FoodItem:
    def __init__(self, name='None', fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == '__main__':
    # Get user inputs
    user_input = [str(input())]
    for i in range(4):
        user_input.append(float(input()))

    #  Use instance methods to create class object, then calculate cal with class method.
    food_tester = FoodItem()
    food1 = FoodItem(user_input[0], user_input[1], user_input[2], user_input[3])
    cal = food1.get_calories(user_input[4])

    # Print required information.
    food_tester.print_info()
    print('Number of calories for {:.2f} serving(s): 0.00\n'.format(user_input[4]))
    food1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(user_input[4], cal))

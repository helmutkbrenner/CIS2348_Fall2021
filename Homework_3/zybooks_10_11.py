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
    user_input = []
    for i in range(5):
        user_input.append(input())

    food1 = FoodItem(user_input[0], int(user_input[1]), int(user_input[2]), int(user_input[3]))
    cal = food1.get_calories(int(user_input[4]))
    print(cal)

    food1.print_info()
    print('Number of calories for {} serving(s): {}'.format(user_input[4], cal))

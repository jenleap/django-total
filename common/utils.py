# common/utils/macro.py

class Macros:
    def __init__(self, calories, carbs, protein, fat):
        self.calories = calories
        self.carbs = carbs
        self.protein = protein
        self.fat = fat

    def __str__(self):
        return f"Calories: {self.calories}, Carbs: {self.carbs}, Protein: {self.protein}, Fat: {self.fat}"

    def to_dict(self):
        return {
            "calories": self.calories,
            "carbs": self.carbs,
            "protein": self.protein,
            "fat": self.fat
        }

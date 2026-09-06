# Last updated: 9/6/2026, 2:55:22 PM
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        Determines which recipes can be made given initial supplies and dependencies.

        Args:
            recipes (List[str]): List of recipe names.
            ingredients (List[List[str]]): List of ingredient lists for each recipe.
            supplies (List[str]): List of available starting supplies.

        Returns:
            List[str]: List of recipes that can be made.
        """
        available = set(supplies)  # Convert supplies to a set for fast lookup
        possible_recipes = set()  # Store successful recipes
        
        while True:
            new_recipe_added = False  # Track if any new recipe gets added
            
            for i in range(len(recipes)):
                if recipes[i] in possible_recipes:  
                    continue  # Skip if we've already added this recipe

                if set(ingredients[i]).issubset(available):
                    possible_recipes.add(recipes[i])
                    available.add(recipes[i])  # This recipe now acts as a supply
                    new_recipe_added = True  # We made progress

            if not new_recipe_added:
                break  # Stop if no new recipes were added in this iteration

        return list(possible_recipes)

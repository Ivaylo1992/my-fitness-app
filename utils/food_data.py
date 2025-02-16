
def get_food_data(food_data):
    """
    Filter the essential information and ignore unnecessary data
    """

    filtered_data = {}
    
    for food in food_data:
        result = f'result {food_data.index(food) + 1}'

        filtered_data[result] = {
                'Name': '',
                'Protein': 0,
                'Total lipid (fat)': 0,
                'Carbohydrate, by difference': 0,
                'Energy': 0,
                'serving_size_unit': None,
                'serving_size': 0,
            }

        food_name = food.get('description', 'unknown food')
        serving_size_unit = food.get('servingSizeUnit', 'g')
        serving_size = food.get('servingSize', 100)

        filtered_data[result]['serving_size'] = serving_size
        filtered_data[result]['Name'] = food_name
        filtered_data[result]['serving_size_unit'] = serving_size_unit


        for nutrient in food.get("foodNutrients", []):
            nutrient_name = nutrient["nutrientName"]
            if nutrient_name in filtered_data[result].keys():
                nutrient_value = nutrient['value']
                filtered_data[result][nutrient_name] = nutrient_value
            

    return list(filtered_data.values())

def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        "full_name" : "Pujan Magar",
        "student_id" : '10319564',
        "pizza_toppings" : ["CHEESE", "BACON", "PINEAPPLE"],
        "movies" : [
            {"title": "Kanjuri", "genre": "Horror"},
            {"title": "Tiger 3", "genre": "Action"}
        ]
    }

    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {"title": "Hate Story", "genre": "Romance"}
    about_me["movies"].append(new_movie)
    print_student_name_and_id(about_me)
    add_pizza_toppings(about_me, ["ONION", "PEPPERONI"])
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me)


# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = full_name.split()[0]
    student_id = about_me["student_id"]
    print(f"My name is {full_name}, but you can call me Mr.{first_name}")
    print(f"My student ID is {student_id}")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me["pizza_toppings"].extend(toppings)
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    pizza_toppings = about_me['pizza_toppings']
    print(f"My favourite pizza toppings are:") 
    [print(f"-{topping}") for topping in about_me["pizza_toppings"]]
    print()  
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    movie_genres = [movie["genre"] for movie in about_me["movies"]]
    print("I like to watch ", ", ".join(movie_genres),'movies.\n')
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    movie_titles = [movie["title"] for movie in movie_list ["movies"]]
    print("Some of my favourite movies are", ", ".join(movie_titles))
    return
    
if __name__ == '__main__':
    main()  

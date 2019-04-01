def print_model(unprinted_models,completed_models):
    while unprinted_models:
        current_model=unprinted_models.pop()
        print("Printing model: " + current_model)
        completed_models.append(current_model)
def show_completed_models(completed_models):
    print("This models are completed")
    for n in completed_models:
        print(n.title())
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models=[]
# print_model(unprinted_designs[:],completed_models)
# show_completed_models(completed_models)
# print(unprinted_designs)
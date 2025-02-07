def hello(name):
    print(f"Hello {name}!")
name = input("What is your name? \n")

clean_name = ' '.join(name.split())

hello(clean_name)
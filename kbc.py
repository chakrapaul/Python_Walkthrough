questions_list=["What is the capital of Australia?","Who was the first President of the United States?"

,"Which planet is known as the Red Planet?",

"What is the largest ocean on Earth?",

"Who invented the telephone?",

"What is the chemical symbol for gold?",

"Which country is famous for the Eiffel Tower?",

"What is the hardest natural substance on Earth?",

"How many continents are there?",

"What is the tallest mountain in the world?",

"Who wrote Romeo and Juliet?",

"What gas do plants absorb from the atmosphere?",

"Which is the longest river in the world?",

"What is the smallest planet in our solar system?",

"Who discovered gravity?"]

multiple_choice_options = [""]

answers_list=["Canberra","George Washington","Mars","Pacific Ocean","Alexander Graham Bell","Au","France","Diamond",
"Seven","Mount Everest","William Shakespeare","Carbon dioxide","The Nile River","Mercury","Sir Isaac Newton"]


price_money = 0


for q,a in zip(questions_list,answers_list):
    print(q)
    choice=input("Enter your answer:")
    if(choice==a):
        price_money = price_money + 500
        print(price_money)
    else:
        break
print("Wrong choice") 
    
print("Price money you won:",price_money)



questions = [
    ["Who is the prime minister of Pakistan?", "Ali", "Muhammad", "Imran Khan", "Shahbaz Sharif", 4],
    ["What is the capital of Pakistan?", "Karachi", "Lahore", "Islamabad", "Peshawar", 3],
    ["What is the national language of Pakistan?", "Sindhi", "Punjabi", "Urdu", "Pashto", 3],
    ["What is the national sport of Pakistan?", "Hockey", "Cricket", "Football", "Squash", 1],
    ["When is Pakistan's Independence Day?", "14th August", "23rd March", "25th December", "6th September", 1],
    ["Who is the founder of Pakistan?", "Allama Iqbal", "Liaquat Ali Khan", "Muhammad Ali Jinnah", "Sir Syed Ahmed Khan", 3],
    ["Which is the largest city in Pakistan?", "Lahore", "Karachi", "Islamabad", "Faisalabad", 2],
    ["What currency is used in Pakistan?", "Rupee", "Dollar", "Taka", "Euro", 1],
    ["What is the national animal of Pakistan?", "Tiger", "Peacock", "Markhor", "Elephant", 3],
    ["What is the national flower of Pakistan?", "Rose", "Jasmine", "Sunflower", "Tulip", 2],
    ["What is the national drink of Pakistan?", "Tea", "Sugarcane juice", "Lassi", "Rooh Afza", 2],
    ["Which sea is located south of Pakistan?", "Red Sea", "Caspian Sea", "Arabian Sea", "Mediterranean Sea", 3],
    ["Which mountain range is found in Pakistan?", "Himalayas", "Rocky Mountains", "Andes", "Karakoram", 4],
    ["What is the largest province of Pakistan by area?", "Sindh", "Punjab", "Balochistan", "Khyber Pakhtunkhwa", 3],
    ["Which river is known as the lifeline of Pakistan?", "Chenab", "Indus", "Ravi", "Jhelum", 2],
    ["What is the national fruit of Pakistan?", "Mango", "Banana", "Apple", "Guava", 1],
    ["Which is the tallest mountain in Pakistan?", "Nanga Parbat", "Broad Peak", "K2", "Rakaposhi", 3],
    ["What is the national bird of Pakistan?", "Eagle", "Peacock", "Chukar Partridge", "Sparrow", 3],
    ["Which Pakistani cricketer is known as the 'Boom Boom'?", "Shoaib Akhtar", "Babar Azam", "Imran Khan", "Shahid Afridi", 4],
    ["Which city is known as the 'City of Gardens' in Pakistan?", "Karachi", "Peshawar", "Lahore", "Quetta", 3],
    ["What is the official religion of Pakistan?", "Christianity", "Islam", "Hinduism", "Buddhism", 2],
    ["Which famous poet is known as the 'National Poet of Pakistan'?", "Mir Taqi Mir", "Ghalib", "Faiz Ahmed Faiz", "Allama Iqbal", 4],
    ["Which city is known as the 'City of Lights' in Pakistan?", "Lahore", "Islamabad", "Karachi", "Quetta", 3],
    ["Which Pakistani airport is named after a former prime minister?", "Jinnah Airport", "Benazir Bhutto Airport", "Allama Iqbal Airport", "Quaid-e-Azam Airport", 2],
    ["What does the green color in Pakistan's flag represent?", "Islam", "Unity", "Progress", "Peace", 1]
]


levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000,1250000,2500000,5000000,10000000]

money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question: {question[0]}")
    print(f"a.  {question[1]}   b. {question[2]}")
    print(f"c.  {question[3]}   d. {question[4]}")
    reply = int(input("Select option 1 - 4: "))
    if reply == question[5]:
        print(f"Correct Answer! You win Rs. {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 320000
    else:
        print(f"Wrong Answer! The correct answer is option {question[5]}")
        break
print(f"You should bring money to home Rs. {money}")
import random

categories = {
    "School": [
        "📚 My homework mysteriously disappeared.",
        "🐶 My dog thought my assignment was a snack.",
        "🚌 I missed the school bus by 10 seconds.",
        "☕ I accidentally spilled juice on my notebook.",
        "📖 I studied the wrong chapter."
    ],

    "Work": [
        "🚗 My car refused to start.",
        "🚦 Every traffic light was red.",
        "☕ I spilled coffee on my keyboard.",
        "📞 My internet stopped working during the meeting.",
        "🖨️ The printer declared a vacation."
    ],

    "Gaming": [
        "🎮 The final boss wouldn't let me leave.",
        "🕹️ I forgot to save my game.",
        "💻 My PC decided to update.",
        "👾 My teammates needed one last match.",
        "🎧 My headset stopped working."
    ],

    "Family": [
        "🐱 My cat was sleeping on my laptop.",
        "👶 I had to babysit my little cousin.",
        "🍽️ Dinner took longer than expected.",
        "🧹 I was helping clean the house.",
        "🚪 I got locked outside."
    ],

    "Funny": [
        "👽 Aliens borrowed my phone.",
        "🦖 A dinosaur blocked the road.",
        "🧙 A wizard cast a 'Late' spell.",
        "🚀 My rocket ran out of fuel.",
        "🐢 I got stuck behind the world's slowest turtle."
    ]
}

history = []
favorites = []


def generate(category):
    excuse = random.choice(categories[category])
    history.append(excuse)
    return excuse


while True:

    print("\n" + "=" * 45)
    print("🎭 ADVANCED EXCUSE GENERATOR")
    print("=" * 45)

    print("1. School Excuse")
    print("2. Work Excuse")
    print("3. Gaming Excuse")
    print("4. Family Excuse")
    print("5. Funny Excuse")
    print("6. Random Category")
    print("7. Generate 3 Excuses")
    print("8. View History")
    print("9. View Favorites")
    print("10. Exit")

    choice = input("\nChoose: ")

    if choice in ["1", "2", "3", "4", "5"]:

        category = list(categories.keys())[int(choice)-1]

        excuse = generate(category)

        print("\n" + "="*40)
        print("Category:", category)
        print("😂", excuse)

        save = input("\nAdd to favorites? (y/n): ").lower()

        if save == "y":
            favorites.append(excuse)
            print("⭐ Added to favorites!")

    elif choice == "6":

        category = random.choice(list(categories.keys()))

        excuse = generate(category)

        print("\n🎲 Random Category:", category)
        print("😂", excuse)

    elif choice == "7":

        print("\n🎉 Here are three excuses:\n")

        for i in range(3):
            category = random.choice(list(categories.keys()))
            excuse = generate(category)
            print(f"{i+1}. [{category}] {excuse}")

    elif choice == "8":

        print("\n📜 Excuse History")

        if history:
            for i, excuse in enumerate(history, 1):
                print(f"{i}. {excuse}")
        else:
            print("No excuses generated yet.")

    elif choice == "9":

        print("\n⭐ Favorite Excuses")

        if favorites:
            for i, excuse in enumerate(favorites, 1):
                print(f"{i}. {excuse}")
        else:
            print("No favorites yet.")

    elif choice == "10":
        print("\n👋 Goodbye!")
        break

    else:
        print("\n❌ Invalid option.")

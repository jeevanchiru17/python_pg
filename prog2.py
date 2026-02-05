from prog2 import Faker

fake = Faker()

# a. List of dictionaries as agents database
agents = []


# Convert to tuple data structure
def convert_to_tuple():
    return tuple(
        (a["ID"], a["Name"], a["Experience"], a["Rank"], a["Missions"]) for a in agents
    )


# b. Generate 100000 synthetic agents
def generate_agents():
    for _ in range(100000):
        agents.append(
            {
                "ID": fake.random_int(min=1000, max=9999),
                "Name": fake.name(),
                "Experience": fake.random_int(min=1, max=20),
                "Rank": fake.word(),
                "Missions": fake.random_int(min=1, max=50),
            }
        )
    print("100000 Agents Generated.")


# Add new agent manually
def add_agent():
    ID = int(input("Enter ID: "))
    Name = input("Enter Name: ")
    Exp = int(input("Experience: "))
    Rank = input("Rank: ")
    Missions = int(input("Missions: "))

    agents.append(
        {"ID": ID, "Name": Name, "Experience": Exp, "Rank": Rank, "Missions": Missions}
    )
    print("Agent Added.")


# Delete agent by ID
def delete_agent(ID):
    for a in agents:
        if a["ID"] == ID:
            agents.remove(a)
            print("Agent Deleted.")
            return
    print("Agent Not Found.")


# Search agent by ID
def search_agent(ID):
    for a in agents:
        if a["ID"] == ID:
            print("Agent Details:", a)
            return
    print("Agent Not Found.")


# c. Menu-driven interface
def menu():
    while True:
        print(
            "\n1. Generate Agents\n2. Add Agent\n3. Delete Agent\n4. Search Agent\n5. Convert to Tuple\n6. Exit"
        )
        ch = int(input("Enter choice: "))

        if ch == 1:
            generate_agents()
        elif ch == 2:
            add_agent()
        elif ch == 3:
            delete_agent(int(input("Enter ID to delete: ")))
        elif ch == 4:
            search_agent(int(input("Enter ID to search: ")))
        elif ch == 5:
            t = convert_to_tuple()
            print("Tuple Data Loaded. Sample:", t[:3])
        else:
            break


menu()

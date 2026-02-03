import matplotlib.pyplot as plt

def load_data():
    data = []
    with open("titanic.csv", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) > 12:
                name = ",".join(parts[3:-8])
                row = parts[:3] + [name] + parts[-8:]
            else:
                row = parts

            data.append(row)
    return data

def display_10():
    line_count = 0
    try:
        with open('titanic.csv', 'r') as file:
            #header = file.readline().strip().split(',')  # Read the header row
            #name_index = header.index('Name')  # Find the index of 'Name' column
        
            for line in file:
                row = line.strip().split(',')
                print(row)
                line_count += 1
                if line_count>=11:
                    break
                #print(row[name_index])
    except FileNotFoundError:
        print("Error: 'titanic.csv' file not found.")
data=('titanic.csv')

def survival_rate(data): 
    header = data[0]
    survived_index = header.index("Survived")

    total_passengers = 0
    total_survived = 0

    for row in data[1:]:
        total_passengers += 1
        if row[survived_index] =="1":
            total_survived += 1

    survival_rate = (total_survived / total_passengers) * 100
    formatted_rate = f"{survival_rate:.2f}"
    return formatted_rate

def gender_survival(data):
    header = data[0]
    survived_index = header.index("Survived")
    gender_index = header.index("Sex")

    total_males = 0
    total_m_survived = 0
    total_females = 0
    total_f_survived = 0

    for row in data[1:]:
        if row[gender_index] == "male":
            total_males += 1
            if row[survived_index] == "1":
                total_m_survived += 1
        elif row[gender_index] == "female":
            total_females += 1
            if row[survived_index] == "1":
                total_f_survived += 1

    if total_males == 0 or total_females == 0:
        return 0.0, 0.0

    m_survival_rate = (total_m_survived / total_males) * 100
    f_survival_rate = (total_f_survived / total_females) * 100

    return m_survival_rate, f_survival_rate

def age_analysis(data):
    header = data[0]
    age_index = header.index("Age")
    survived_index = header.index("Survived")

    total_age = 0
    age_count = 0

    survived_age_total = 0
    survived_count = 0

    nonsurvived_age_total = 0
    nonsurvived_count = 0

    youngest = None
    oldest = None

    for row in data[1:]:
        age = row[age_index].strip()

        if age == "":
            continue  

        age = float(age)

        total_age += age
        age_count += 1

        if youngest is None or age < youngest:
            youngest = age
        if oldest is None or age > oldest:
            oldest = age

        if row[survived_index] == "1":
            survived_age_total += age
            survived_count += 1
        else:
            nonsurvived_age_total += age
            nonsurvived_count += 1

    avg_age = total_age / age_count
    avg_survived_age = survived_age_total / survived_count
    avg_nonsurvived_age = nonsurvived_age_total / nonsurvived_count

    print(f"Average age of all passengers: {avg_age:.2f}")
    print(f"Average age of survivors: {avg_survived_age:.2f}")
    print(f"Average age of non-survivors: {avg_nonsurvived_age:.2f}")
    print(f"Youngest passenger age: {youngest}")
    print(f"Oldest passenger age: {oldest}")

def class_analysis(data):
    header = data[0]
    class_index = header.index("Pclass")
    survived_index = header.index("Survived")
    fare_index = header.index("Fare")

    class_counts = {"1": 0, "2": 0, "3": 0}
    class_survived = {"1": 0, "2": 0, "3": 0}
    class_fare_total = {"1": 0.0, "2": 0.0, "3": 0.0}
    class_fare_count = {"1": 0, "2": 0, "3": 0}

    for row in data[1:]:
        pclass = row[class_index]
        survived = row[survived_index]
        fare = row[fare_index].strip()

        if pclass not in class_counts:
            continue

        class_counts[pclass] += 1

        if survived == "1":
            class_survived[pclass] += 1

        if fare != "":
            class_fare_total[pclass] += float(fare)
            class_fare_count[pclass] += 1

    class_rates = {}
    class_avg_fares = {}

    for pclass in ["1", "2", "3"]:
        class_rates[pclass] = (class_survived[pclass] / class_counts[pclass]) * 100
        class_avg_fares[pclass] = class_fare_total[pclass] / class_fare_count[pclass]

    best_class = max(class_rates, key=class_rates.get)

    
    print("Class Analysis:")
    for pclass in ["1", "2", "3"]:
        print(f"Class {pclass}:")
        print(f"  Survival rate: {class_rates[pclass]:.2f}%")
        print(f"  Average fare: ${class_avg_fares[pclass]:.2f}")

    print(f"\nClass with best survival chances: Class {best_class}")

    
    return class_rates, class_avg_fares, best_class

def family_survival(data):
    header = data[0]
    sibsp_index = header.index("SibSp")
    parch_index = header.index("Parch")
    survived_index = header.index("Survived")

    family_counts = {}
    family_survived = {}

    alone_count = 0
    alone_survived = 0
    family_count = 0
    family_survived_count = 0

    for row in data[1:]:
        sibsp = int(row[sibsp_index])
        parch = int(row[parch_index])
        survived = row[survived_index]

        family_size = sibsp + parch + 1

        if family_size not in family_counts:
            family_counts[family_size] = 0
            family_survived[family_size] = 0

        family_counts[family_size] += 1
        if survived == "1":
            family_survived[family_size] += 1

        if family_size == 1:
            alone_count += 1
            if survived == "1":
                alone_survived += 1
        else:
            family_count += 1
            if survived == "1":
                family_survived_count += 1

    print("Survival Rate by Family Size:")
    for size in sorted(family_counts):
        rate = (family_survived[size] / family_counts[size]) * 100
        print(f"Family Size {size}: {rate:.2f}%")

    alone_rate = (alone_survived / alone_count) * 100
    family_rate = (family_survived_count / family_count) * 100

    print("\nTraveling Comparison:")
    print(f"Traveling alone survival rate: {alone_rate:.2f}%")
    print(f"Traveling with family survival rate: {family_rate:.2f}%")

    if family_rate > alone_rate:
        print("Conclusion: Traveling with family improved survival chances.")
    else:
        print("Conclusion: Traveling alone improved survival chances.")

def visualized_data(data):
    header = data[0]

    survived_index = header.index("Survived")
    gender_index = header.index("Sex")
    age_index = header.index("Age")
    class_index = header.index("Pclass")

    # survival by gender
    male_rate, female_rate = gender_survival(data)

    plt.figure()
    plt.bar(["Male", "Female"], [male_rate, female_rate])
    plt.title("Survival Rate by Gender")
    plt.ylabel("Survival Rate (%)")
    plt.xlabel("Gender")
    plt.show()  


    # age distribution
    ages = []

    for row in data[1:]:
        if row[age_index] != "":
            ages.append(float(row[age_index]))

    plt.figure()
    plt.hist(ages, bins=20)
    plt.title("Age Distribution of Passengers")
    plt.xlabel("Age")
    plt.ylabel("Number of Passengers")
    plt.show()

    #survival by class

    class_rates, _, _ = class_analysis(data)

    plt.figure()
    plt.bar(
        ["Class 1", "Class 2", "Class 3"],
        [class_rates["1"], class_rates["2"], class_rates["3"]]
    )
    plt.title("Survival Rate by Passenger Class")
    plt.ylabel("Survival Rate (%)")
    plt.xlabel("Passenger Class")
    plt.show()

def comprehensive_report(data):
    header = data[0]

    survived_i = header.index("Survived")
    sex_i = header.index("Sex")
    age_i = header.index("Age")
    class_i = header.index("Pclass")

    total_passengers = 0
    total_survivors = 0

    gender_stats = {"male": [0, 0], "female": [0, 0]}
    class_stats = {"1": [0, 0], "2": [0, 0], "3": [0, 0]}
    age_groups = {
        "Child (<18)": [0, 0],
        "Adult (18-60)": [0, 0],
        "Senior (>60)": [0, 0]
    }

    
    profile_counts = {}

    for row in data[1:]:
        total_passengers += 1
        survived = row[survived_i]

        if survived == "1":
            total_survivors += 1

       
        sex = row[sex_i]
        if sex in gender_stats:
            gender_stats[sex][0] += 1
            if survived == "1":
                gender_stats[sex][1] += 1

        
        pclass = row[class_i]
        if pclass in class_stats:
            class_stats[pclass][0] += 1
            if survived == "1":
                class_stats[pclass][1] += 1

       
        age = row[age_i].strip()
        if age != "":
            age = float(age)
            if age < 18:
                group = "Child (<18)"
            elif age <= 60:
                group = "Adult (18-60)"
            else:
                group = "Senior (>60)"

            age_groups[group][0] += 1
            if survived == "1":
                age_groups[group][1] += 1

       
        profile = (sex, pclass)
        if profile not in profile_counts:
            profile_counts[profile] = [0, 0]

        profile_counts[profile][0] += 1
        if survived == "1":
            profile_counts[profile][1] += 1

   
    survival_rate = (total_survivors / total_passengers) * 100

    def rate(stats):
        return (stats[1] / stats[0]) * 100 if stats[0] > 0 else 0

    best_profile = max(
        profile_counts,
        key=lambda p: rate(profile_counts[p])
    )

    
    with open("titanic_comprehensive_report.txt", "w", encoding="utf-8") as file:
        file.write("TITANIC COMPREHENSIVE SURVIVAL REPORT\n")
        file.write("=" * 40 + "\n\n")

        file.write("OVERALL STATISTICS\n")
        file.write(f"Total passengers: {total_passengers}\n")
        file.write(f"Total survivors: {total_survivors}\n")
        file.write(f"Overall survival rate: {survival_rate:.2f}%\n\n")

        file.write("SURVIVAL BY GENDER\n")
        for g in gender_stats:
            file.write(
                f"{g.capitalize()}: {rate(gender_stats[g]):.2f}%\n"
            )
        file.write("\n")

        file.write("SURVIVAL BY CLASS\n")
        for c in class_stats:
            file.write(
                f"Class {c}: {rate(class_stats[c]):.2f}%\n"
            )
        file.write("\n")

        file.write("SURVIVAL BY AGE GROUP\n")
        for group in age_groups:
            file.write(
                f"{group}: {rate(age_groups[group]):.2f}%\n"
            )
        file.write("\n")

        file.write("MOST LIKELY SURVIVOR PROFILE\n")
        file.write(
            f"Gender: {best_profile[0]}, "
            f"Class: {best_profile[1]}\n"
        )

    print("Comprehensive report saved to 'titanic_comprehensive_report.txt'")



def main():
        while True:
            goal=input ('''
        What would you like to do?
        1. Load and display data
        2. Calculate survival rate
        3. Survival by gender
        4. Age analysis
        5. Class based analysis
        6. Family survival patterns
        7. Data visualization
        8. Comprehensive report
                    ''')
            if goal == ("1"):
                print(display_10())
            elif goal == ("2"):
                data = load_data()
                print(survival_rate(data))
            elif goal == "3":
                data = load_data()
                male_rate, female_rate = gender_survival(data)
                print(f"Male survival rate: {male_rate:.2f}%")
                print(f"Female survival rate: {female_rate:.2f}%")
            elif goal == "4":
                data = load_data()
                age_analysis(data)
            elif goal == "5":
                data = load_data()
                class_analysis(data)
            elif goal == "6":
                data = load_data()
                family_survival(data)
            elif goal == "7":
                data = load_data()
                visualized_data(data)
            elif goal == "8":
                data = load_data()
                comprehensive_report(data)


main()
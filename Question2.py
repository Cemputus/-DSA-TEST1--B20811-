#1. Create two separate lists named catholic_martyrs and anglican_martyrs containing the names of Catholic and Anglican martyrs respectively.
catholic_martyrs = ["Achileo Kiwanuka", "Adolphus Ludigo Mukasa", "Ambrosius Kibuuka", "Anatoli Kiriggwajjo", "Andrew Kaggwa", 
                    "Antanansio Bazzekuketta", "Bruno Sserunkuuma", "Charles Lwanga", "Denis Ssebuggwawo Wasswa", "Gonzaga Gonza",
                    "Gyavira Musoke", "James Buuzaabalyaawo", "John Maria Muzeeyi", "Joseph Mukasa Kizito", "Lukka Baanabakintu",
                    "Matiya Mulumba", "Mbaga Tuzinde", "Mugagga Lubowa", "Mukasa Kiriwawanvu", "Nowa Mawaggali", "Ponsiano Ngondwe"]

anglican_martyrs = ["Aaron Lubega", "Apollo Kivebulaya", "Eria Sebukyala", "Fredrick Kizza", "George Kizza", "James Hannington", 
                    "Janani Luwum", "Joseph Balikuddembe", "Kizito", "Mark Kakumba", "Matia Mulumba", "Nuhu Mbegu", 
                    "Robert Munyagayirwa", "Samwiri Mukasa", "Yefusa Namayanja", "Yohana Mukasa", "Yosefu Lugalama", 
                    "Yowana Kitaka", "Yowana Maria Mukasa", "Yowana Mukiibi", "Yusufu Lugalama", "Zakayo Lubega"]



#2.Identify and remove any duplicate names present in both lists.
# Converting the lists to sets
catholic_set = set(catholic_martyrs)
anglican_set = set(anglican_martyrs)

# Finding the intersection of the two sets
common_martyrs = catholic_set.intersection(anglican_set)

# Removing the common names from both lists
catholic_martyrs = list(catholic_set - common_martyrs)
anglican_martyrs = list(anglican_set - common_martyrs)

 #3.Write a function named martyr_count that takes in a martyr's name as an  argument and returns the group (Catholic or Anglican) to which the martyr belongs.
def martyr_count():
    name = input("Enter a martyr's name: ")
    
    if name in catholic_martyrs:
        return "Catholic"
    elif name in anglican_martyrs:
        return "Anglican"
    else:
        return "Unknown"

# Call the function to get the result
group = martyr_count()
if group != "Unknown":
    print(f"The martyr belongs to the {group} group.")
else:
    print("The name is not found in either list of Uganda Martyrs.")

 #4. To determine the group of the martyr named "Kizito", you can call the martyr_count function like this:
 #Call the function to determine the group of the martyr named "Kizito"
group = martyr_count()
if group != "Unknown":
    print(f"The martyr named Kizito belongs to the {group} group.")
else:
    print("The name Kizito is not found in either list of Uganda Martyrs.")
    
    
def matches_uganda_martyrs(name):
    return martyr_count(name) != "Unknown"

# Allow the user to input a name to check
name_to_check = input("Enter a name to check if it matches Uganda Martyrs: ")

result = matches_uganda_martyrs(name_to_check)

if result:
    print(f"{name_to_check} matches a name in either the Catholic or Anglican martyrs list.")
else:
    print(f"{name_to_check} does not match any of the Uganda Martyrs' names.")








#EMMANUEL NSUBUGA
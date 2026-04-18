#Dictionary of words

"""1. Add a Word: Allow users to add new words along with their meanings to the
dictionary.
2. Search for Meaning: Enable users to search for the meaning of a word in the
dictionary.
3. Display All Words: Provide an option to display all words and their meanings
currently stored in the dictionary.
4. Update Meaning: Implement a feature to update the meaning of an existing
word in the dictionary. After updating, display the updated meaning.
5. Delete Word: Implement a feature to delete a word and its meaning from the
dictionary. Confirm the deletion and handle cases where the word doesn't
exist."""

words_dictionary={}
while True:
    print("Dictionary Management System")
    print("1. Add a Word")
    print("2. Search for Meaning")
    print("3. Display All Words")
    print("4. Update Meaning:")
    print("5. Delete Word:")
    print("6. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        word=input(f"Enter word: ").lower()
        meaning=input(f"Enter meaning: ").lower()
        words_dictionary[word]=meaning
        print("Word Added Successfully!")
    elif choice==2:
        search_word=input("Enter word to search: ").lower()
        if search_word in words_dictionary:
            print(f"Meaning: {words_dictionary[search_word]}")
        else:
            print(f"{search_word} word not found...")
    elif choice==3:
        print(f"words and thier meanings: ")
        for word in words_dictionary:
            print(f"{word}: {words_dictionary[word]}")
    elif choice==4:
        exist_word=input("Enter the word to update meaning: ").lower()
        if exist_word in words_dictionary:
            update_meaning=input("Enter new meaning: ")
            words_dictionary[exist_word]=update_meaning
        print("Meaning updated Successfully!")
        print(f"Updated meaning: {words_dictionary[exist_word]}")
    elif choice==5:
        delete_word=input("Enter the word to delete: ").lower()
        if delete_word in words_dictionary:
            words_dictionary.pop(delete_word)
            print("Word Deleted Successfully!")
        else:
            print(f"{delete_word} does not exist to delete")
    else:
        print("Exiting program....")
        break
          
            
        


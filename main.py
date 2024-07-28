import asyncio
# Phonebook
phonebook = {}
async def main():
    while True:
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display Phonebook")
        print("4. Quit")
        print("Enter your choice")
        await asyncio.sleep(1)
        choice = str(input())
        if choice == str(1):
            print("Enter contact name:")
            await asyncio.sleep(1)
            name = input()
            print("Enter contact number:")
            await asyncio.sleep(1)
            number = input()
            phonebook[name] = number
            await asyncio.sleep(1)
        elif choice == str(2):
            print("Enter contact name to search")
            await asyncio.sleep(1)
            name = input()
            if name in phonebook:
                print("Contact number: ", phonebook[name])
            else:
                print("Contact not found.")
                await asyncio.sleep(1)
        elif choice == str(3):
            for name, number in phonebook.items():
                print(name, ":", number)
                await asyncio.sleep(1)
        elif choice == str(4):
            print("Exit...")
            print(phonebook)
            break
        else:
            print("Invalid Choice. Please try again.")
            await asyncio.sleep(1)


#if __name__ == '__main__':

asyncio.run(main())
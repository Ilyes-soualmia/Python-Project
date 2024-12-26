import json 

def main():
    with open("QCM.json", "r") as f:
        data = json.load(f)
    print(data)

main()    
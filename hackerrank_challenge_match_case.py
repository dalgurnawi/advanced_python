def custom_list(prov_list, N):
    command =N.split(" ")[0]
    match command:
        case "insert":
            list_index = int(N.split(" ")[1])
            list_value = int(N.split(" ")[2])
            prov_list.insert(list_index, list_value)
        case "print":
            print(prov_list)
        case "remove":
            remove_value = int(N.split(" ")[1])
            for i in range(len(prov_list)):
                if prov_list[i] == remove_value:
                    prov_list.pop(i)
                    break
        case "append":
            append_value = int(N.split(" ")[1])
            prov_list.append(append_value)
        case "sort":
            prov_list = prov_list.sort()
        case "pop":
            prov_list.pop(-1)
        case "reverse":
            prov_list.reverse()
        case _:
            raise ("Not a valid command!")


if __name__ == '__main__':
    prov_list = []
    N = input()
    print(N)
    for i in range(int(N)):
        N = str(input())
        custom_list(prov_list=prov_list, N=N)
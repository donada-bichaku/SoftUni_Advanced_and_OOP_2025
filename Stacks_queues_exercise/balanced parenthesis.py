expression = input()
not_matched = []
map_parenthesis = {
    "}": "{",
    ")": "(",
    "]": "["
}


for paren in expression:
    if paren in map_parenthesis.values():
        not_matched.append(paren)
    else:
        if not_matched and map_parenthesis[paren] == not_matched.pop(): # if { == {
            continue
        else:
            print("NO")
            break
else:
    if not not_matched:
        print("YES")


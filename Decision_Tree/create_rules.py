from Decision_Tree.decision_tree import DTree


dobj = DTree()
rule_set, consequents= dobj.create_rules()


for i in range(len(rule_set)):
    #print(type(consequents[i]))
    #print(type(rule_set[i]))
    cnt = 0
    c = consequents[i].tolist()[0]
    if(max(c))>10:
        cnt += 1
        print(rule_set[i], consequents[i])
    #print(cnt)


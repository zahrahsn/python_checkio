
ice_dict={
    'classic':['apple','strawberry','pineapple'],
    'mix_strawberry':['strawberry','rasberry','banana'],
    'mix_exotic':['kiwi','pineapple','coffee'],
    'mix_hawayi':['coconout','pineapple','peanut']
}
additioal_list=['jam','chochlatepowder','pistachio']
def make_ice(icename,allergic,additional):
    ice_ingredient=ice_dict[icename]
    # print(ice_ingredient)
    removed=[i for i in ice_ingredient if i in allergic]
    # print(removed)
    for i in additional :
        if i in allergic:
            removed.append(i)
    requested=ice_ingredient+additional        
    final=[i for i in requested if i not in removed]
    return final
   
if __name__=='__main__':
    print("please select your icecream type classic,mix_strawberry,mix_exotic,mix_hawayi")
    icename=input('please select your desired ice cream:')
    allergic=input("let me know if you are allergic to something:").split()
    additional=input('anything to add? jam,chochlatepowder,pistachio:').split()
    final=make_ice(icename,allergic,additional)
    final.sort()
    print(','.join(final))
       
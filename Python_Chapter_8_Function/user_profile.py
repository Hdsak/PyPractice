def build_profile(first,last,**user_info):
    profile={}
    profile['first name']=first
    profile['last name']=last
    for k,v in user_info.items():
        profile[k]=v
    return profile
user_profile=build_profile("Roma",'Mexanik',location='prinston',field='physics')
print(user_profile)
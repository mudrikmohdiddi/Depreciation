print("""
 ____________________________________________
 |      CALCULATION FOR DEPRECIATION        |
 |                                          |
 |      welcom to change depreciation       |
 |                                          |
 |__________________________________________|
""")
j=1
while(8==8):
    method=input("""
     S: sum of year digit method
     L: straigh line method
     R: reducing balance method
     CHOICE METHOD OF DEPRECITION :""")
    if(method.upper()=="S"):
        cost=float(input("\nEnter cost of asset:"))
        year=int(input("\nEnter number of years:"))
        sum_y=year*(year+1)/2
        print("\nDepreciation=cost*Y/sum_years")
        n=0
        m=0
        for i in range(year,0,-1):
            d=cost*i/sum_y
            n+=d
            m+=1
            print(f"\nDepreciation of year {m} ={cost}*{i}/{sum_y}={d}\n\nTotal Depreciation is {n}")
    elif(method.upper()=="L"):
        cost=float(input("\nEnter cost of asset:"))
        year=int(input("\nEnter number of years:"))
        rate=input("Use rate (Y or N):")
        if(rate.upper()=="Y"):
            r=float(input("Enter rate of depreciation:"))
            n=0
            print("\nDepreciation=cost*rate")
            for i in range(1,year+1):
                d=cost*r/100
                n+=d
                print(f"\nDepreciation of year {i} ={cost}*{r}/100={d}\n\nTotal depreciation={n}")
        else:
            try:
                sv=float(input("Enter scrapt value if any:"))
            except ValueError:
                sv=0
            print("Depreciation=(cost-scrapt value)/no of year")
            n=0
            for i in range(1,year+1):
                d=(cost-sv)/year
                n+=d
                print(f"\nDepreciation of year {i} =({cost}-{sv})/{year}={d}\n\nTotal depreciation={n}")
    else:
        print("\nWelcom to reducing balance method\n")
        cost=float(input("\nEnter cost of asset:"))
        year=int(input("\nEnter number of years:"))
        r=float(input("\nEnter rate of depreciation:"))
        n=0
        c=cost
        print("\nDepreciation=(cost-dep_n-1)*Y/rate")
        for i in range(1,year+1):
            d=cost*r/100
            n+=d
            print(f"\nDepreciation of year {i} ={cost}*{r}%={d}\n\nTotal depreciation={n}")
            cost=cost-d
    j+=1
    print(f"Continue with other asset {j}")
    
        
    
    

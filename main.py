print "             Hey there! Here you can view my Python scripts"
print "Following are some of my python scripts, choose which one you want to run: \n\
1. Student ecomes teacher \n\
2. Battleship \n\
3. exam statistics \n "
choose = raw_input("Choose the program to run:")
if choose == '1':
    import studentBecomeTeacher                     #imports the file to run
    studentBecomeTeacher.main()                     #calling main function from the python file
elif choose == '2':
    import battleship
    battleship.main()
elif choose == '3':
    import examStatistics
    examStatistics.main()
else:
    print "Choose correct option (1, 2 or 3)"

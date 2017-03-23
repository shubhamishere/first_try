grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5] #list of grades

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):             				#sum of the grades
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):         				#average of the grades
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):        				#finding grade variance in scores
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score)**2
        total_variance  = variance/float(len(scores))
    return total_variance

def grades_std_deviation(variance):         		#this is how we calculate standard deviation
    return variance**0.5
variance = float(grades_variance(grades))
print grades_std_deviation(variance)            	#Lines below will print every calculated function line by line.
    
print_grades(grades)
print grades_sum(grades)
print grades_average(grades)
print grades_variance(grades)
print grades_std_deviation(variance)

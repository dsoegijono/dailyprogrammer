def get_average(set):
    #TODO round up/down?
    return sum(set)/len(set)

def get_letter_grade(grade):
    if grade < 60:
        return 'F'
    else:
        ret = ''
        if grade < 70:
            ret = 'D'
        elif grade < 80:
            ret = 'C'
        elif grade < 90:
            ret = 'B'
        else:
            ret = 'A'
        if grade % 10 <= 3:
            ret += '-'
        elif grade % 10 >= 7:
            ret += '+'
        return ret

def main():
    filename = raw_input("Please enter input file name. Enter '-m' to input manually.\n> ")
    
    if filename == "-m":
        #TODO
        print "MANUAL INPUT DOESN'T WORK YET!"
    else:
        file = open(filename, 'r')
        gradebook = []
        for line in file:
            l = line.split()
            grades = map(int, l[-5:])
            grades = sorted(grades)
            del l[-5:]
            fullname = ' '.join(l[::-1])
            average = get_average(grades)
            student = { 'name': fullname, 'average': average, 'grades': grades }
            gradebook.append(student)
        gradebook = sorted(gradebook, key=lambda x: x['average'], reverse=True)
        for student in gradebook:
            name = student['name'].ljust(20)
            avg = str(student['average']).rjust(3)
            ltr = get_letter_grade(int(student['average'])).ljust(2)
            grades = " ".join(str(x).rjust(3) for x in student['grades'])
            print name + " (" + avg + "%) (" + ltr + "): " + grades
    
if __name__ == "__main__":
    main()

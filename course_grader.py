def course_grader(test_scores):
    for score in test_scores:
        if score < 50:
            return "fail"
    
    total_score = 0
    for score in test_scores:
        total_score += score
    
    num_score = len(test_scores)
    average_score = total_score / num_score
  
    if average_score >= 70:
        return "pass"
    return "fail"
  
        
         
def main():
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass"
    print(course_grader([60,80,80,70,70]))  # "pass"
if __name__ == "__main__":
    main()

"""
	Coding Problem #2 : Simple ID Scanner

	Problem:
		
		Dave Torro and Micayoi Latuza are two students currently applying at the College of Computer and Information Sciences.
		
		As they thought the interviewing process was finished, Carl The Examiner appeared.
		
		He was known for making coding problems that was defined as "basic", but was actually outright hard, but theoretically possible. 
		
		It was explained during the enrollment process, that once Sir. Carl appeared in the interview process, a special coding exam will
		
		be added before moving to the final stage of enrollment. If the applicant won't be able to answer it their applcation will be considered
		
		void.
		
		The problem is as follows:
		
			Make a program that accepts as Input an Identification Number and the User Information while following these criterias:
			
			Identification Number 
				- Must have a maximum of  12 characters in the Identification Number.
				- Must contain at least 6 digits/integers.
				- Must at least contain 4 characters in the alphabet except the special characters.
			
			User Info:
				Name : No Conditions
				Email : No Conditions
				Phone Number : No Conditions

			Expected Program Flow:
			
			Your program must ask 3 of these pairs initially.
			
			After accepting the inputs, 

			The program will ask for an identification number and will output the corresponding information. (Name, Email, Phone Number)
			
			The program will continue asking the user until a "0" is entered.

							
			Illustrated Program Flow ( You may follow this exact input messages, or make your own.):
			
			Input 3 initial Records:
			
			Identification Number : 23456ABAAA12
			Name : Robert Waltson
			Phone Number: 2222111131323
			Email : asdasdasd@gmail.com
			
			Identification Number : ABAAA1223456
			Name : Richardo Contoro
			Phone Number: 22221111312323323
			Email : zzzzzz23459876@gmail.com
			
			
			Identification Number : ZZZABB987654
			Name : Roberta Waltsonso
			Phone Number: 22221111312323323
			Email : epicguy123459876@gmail.com
			
			Enter an Identification Number: ABAAA1223456
			
			Results: 
			Name : Richardo Contoro
			Phone Number: 22221111312323323
			Email : zzzzzz23459876@gmail.com
			
			Make another query? Enter value except 0 to Continue : 2
			
			Enter an Identification Number: 23456ABAAA12
			
			Results: 
			Name : Robert Waltson
			Phone Number: 2222111131323
			Email : asdasdasd@gmail.com
			
			Make another query? Enter value except 0 to Continue : 0
			
			End of Program.
			
		
		Make the Program that Sir Carl is requesting and pass the interview process of CCIS.

"""


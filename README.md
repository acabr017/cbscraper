# CBScraper


## Access useful student learning information from CollegeBoard's AP Classroom resource to help make you a better teacher. 


CollegeBoard has access to really useful information, such as Big Ideas, Skills, Topics/Sub-topics, that should be easily given to teachers to increase their effectiveness in teaching and reaching all their students in their AP classroom. Being able to see trends and patterns in a classroom is crucial to planning and implimenting better lessons and acheiving better results. 

Since CollegeBoard doesn't easily give us access to these metrics, this project will help you get a CSV file with your students assessment results and how they connect to the Big Ideas, Skills, and other useful metrics. 

* Provide your CB account username and password (nothing is saved, so there is no risk of compromising your account)
* Provide the link to the assessment (Note: Due to how CB codes their Free Response Questions [I only have access to AP Physics currently, so I can't check out AP classes] it is meaningless to scrape the data from FRQ questions, so this tool only looks for Multiple Choice data)
* The tool will open a browser, navigate to the CB webpage, sign in as you and then navigate to the assessment.
* It will then pull the data from the page and output it as a CSV file in the same folder as the source code.  



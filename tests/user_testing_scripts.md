# User Testing Scripts 
## Objectives 
- Verify that the feature meets the specified requirements. 
- Ensure the feature is user-friendly and intuitive for the target audience. 
## Target Audience 
- Users who are familiar with the application and its functionalities. 
- New users who have not interacted with the application before. 
## Features to be Tested 
- User registration process. 
- Customer data retrieval. 
- Feedback submission process. 
## Testing Scripts 
### Script 1: User Registration 
1. Navigate to the registration page. 
2. Fill in the registration form with valid details: 
   - Username: testuser 
   - Password: testpassword 
   - First Name: Test 
   - Last Name: User 
   - Email: testuser@example.com 
   - Credit Card Number: 1234-5678-9012-3456 
3. Submit the form. 
4. Verify that a success message is displayed. 
5. Attempt to register with the same username and verify that an error message is shown. 
### Script 2: Customer Data Retrieval 
1. Log in with the following credentials: 
   - Username: admin 
   - Password: admin123 
2. After logging in, navigate to the customer data retrieval section. 
3. Enter a valid customer ID (e.g., 1). 
4. Submit the request. 
5. Verify that the correct customer data is displayed. 
6. Enter an invalid customer ID and verify that an error message is shown. 
### Script 3: Feedback Submission 
1. Navigate to the feedback form. 
2. Fill in the feedback form with the following details: 
   - Feedback: "The application is user-friendly and easy to navigate." 
3. Submit the feedback. 
4. Verify that a success message is displayed. 
5. Attempt to submit the form without filling in the required fields and verify that appropriate error messages are shown. 
## Questions for Feedback 
1. How easy was it to navigate through the application? 
2. Were there any features that you found confusing or difficult to use? 
3. How would you rate the overall user experience on a scale of 1 to 5? 
4. What improvements would you suggest for the application? 
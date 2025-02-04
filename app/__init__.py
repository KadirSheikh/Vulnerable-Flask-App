from flask import jsonify, render_template 
from app.issues import get_issues  # Importing the get_issues function 
def list_issues(): 
    """ 
    Endpoint to list all issues in the project. 
    """ 
    try: 
        issues = get_issues()  # Retrieve issues from the previously defined function 
        print("Listing issues successfully.") 
        return render_template('issues.html', issues=issues), 200 
    except Exception as e: 
        print("Error in listing issues: {0}".format(e)) 
        return jsonify({'Error': str(e)}), 500 
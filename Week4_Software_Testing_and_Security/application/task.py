
class Task():
    def __init__(self, title, description, due_date):
        """
        Constructor for the Task class.
        
        Initializes a new task with a title, description, and due date.
        The task is created with a default status of 'False' (incomplete).
        
        Args:
        - title (str): The title of the task.
        - description (str): A brief description of the task.
        - due_date (str): The due date of the task, typically in 'dd-mm-yyyy' format.
        """
        
        # Assign the title of the task
        self.title = title
        
        # Assign the description of the task
        self.description = description
        
        # Assign the due date of the task
        self.due_date = due_date
        
        # Task status, initially set to False (indicating incomplete)
        self.status = False

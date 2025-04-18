import shutil
import os

# Define the zip functionality
class ZipGeneratedProjectNode:
    def __init__(self, zip_filename='generated_project',config=None):
        self.zip_filename = zip_filename
    
    def execute(self,input,config=None):
        # Navigate to the root directory from the 'tools' directory
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Go up one level
        
        # Path to the generated project directory (relative path from root)
        generated_project_path = os.path.join(project_root, 'generated_project')
        
        # Create the zip file in the root folder, excluding 'generated_project' from the zip path
        shutil.make_archive(self.zip_filename, 'zip', project_root, 'generated_project')
        
        print(f"Project zipped to: {self.zip_filename}.zip")
        return input  
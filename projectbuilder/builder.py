import logging
import os

class Builder:
    def __init__(self, path_to_project, project_name):
        self.project_root_path = path_to_project
        self.project_name = project_name
        
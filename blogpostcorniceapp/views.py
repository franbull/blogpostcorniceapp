"""
Uses Cornice to expose a RESTful resource. If you implement methods of the
class TaskResource named after the http verbs (get, post, put, delete) then
those will be exposed at eg /tasks/{id}. Methods implemented named eg
collection_post will be exposed at eg /tasks.
"""
from cornice.resource import resource
from cornice.resource import view

from blogpostcorniceapp.models import Task
from blogpostcorniceapp.models import DBSession


@resource(collection_path='/tasks', path='/tasks/{id}')
class TaskResource(object):
    """
    Intended to be decorated as a Cornice 'resource', TaskResource implements a
    RESTful interface for blogpostcorniceapp.models.Task. We don't need to add
    routes for these methods, Cornice will discover them.
    """
    def __init__(self, request):
        self.request = request

    def collection_get(self):
        """Gets task_id and name for all Tasks."""
        return {
            'tasks': [
                {'task_id': task.task_id, 'name': task.name}
                    for task in DBSession.query(Task)
                    ]
            }

    @view(validators=('validate_post',))
    def collection_post(self):
        """Adds a new Task."""
        task = self.request.json
        DBSession.add(Task.from_json(task))

    def get(self):
        """Gets a single Task with task_id in the url."""
        return DBSession.query(Task).get(
                int(self.request.matchdict['id'])).to_json()

    def validate_post(self, request):
        """
        To be used as a Cornice 'validator'. Validates that the Task name is
        unique in the database.
        """
        name = request.json['name']
        num_existing = DBSession.query(Task).filter(Task.name==name).count()
        if num_existing > 0:
            request.errors.add(request.url, 'Non-unique task name.',
                    'There is already a task with this name.')

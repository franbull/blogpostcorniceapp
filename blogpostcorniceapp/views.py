
from cornice.resource import resource

from blogpostcorniceapp.models import Task
from blogpostcorniceapp.models import DBSession


@resource(collection_path='/tasks', path='/tasks/{id}')
class TaskResource(object):
    def __init__(self, request):
        self.request = request

    def collection_get(self):
        return {
            'tasks': [
                {'task_id': task.task_id, 'name': task.name}
                    for task in DBSession.query(Task)
                    ]
            }

    def collection_post(self):
        """Adds a new task."""
        task = self.request.json
        num_existing = DBSession.query(Task).filter(Task.name==task['name']).count()
        if num_existing > 0:
            raise Exception('That task already exists!')
        DBSession.add(Task.from_json(task))

    def get(self):
        return DBSession.query(Task).get(int(self.request.matchdict['id'])).to_json()

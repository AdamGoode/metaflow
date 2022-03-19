
class Current(object):

    def __init__(self):
        self._flow_name = None
        self._run_id = None
        self._step_name = None
        self._task_id = None
        self._origin_run_id = None
        self._namespace = None
        self._username = None
        self._is_running = False

    def _set_env(self,
                 flow_name,
                 run_id,
                 step_name,
                 task_id,
                 origin_run_id,
                 namespace,
                 username):

        self._flow_name = flow_name
        self._run_id = run_id
        self._step_name = step_name
        self._task_id = task_id
        self._origin_run_id = origin_run_id
        self._namespace = namespace
        self._username = username
        self._is_running = True

    def _update_env(self, env):
        for k, v in env.items():
            setattr(self.__class__, k, property(fget=lambda _, v=v: v))

    @property
    def is_running_flow(self):
        return self._is_running

    @property
    def flow_name(self):
        return self._flow_name

    @property
    def run_id(self):
        return self._run_id

    @property
    def step_name(self):
        return self._step_name

    @property
    def task_id(self):
        return self._task_id

    @property
    def origin_run_id(self):
        return self._origin_run_id

    @property
    def pathspec(self):
        return '/'.join((self._flow_name,
                         self._run_id,
                         self._step_name,
                         self._task_id))

    @property
    def namespace(self):
        return self._namespace

    @property
    def username(self):
        return self._username

# instantiate the Current singleton. This will be populated
# by task.MetaflowTask before a task is executed.
current = Current()

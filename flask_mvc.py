import os
import pkgutil


class FlaskMvc:

    def __init__(self, app=None, controllers_package=None):
        self._app = app
        self._models_folder = os.path.join(os.path.abspath('../../../'), 'models')

        #: The folder and package where controllers are.
        self._controllers_package = controllers_package or 'controllers'
        self._controllers_folder = os.path.join(os.path.abspath('../../../'), self._controllers_package)

        if app is not None:
            self.init_app(app)


    def _format_route(self, controller, controllers_package):
        return '{0}.{1}'.format(controllers_package, controller), controller

    def _create_base_struture(self):
        """
            Creates models and controlers packages
        """
        if not os.path.exists(self._models_folder):
            os.makedirs(self._models_folder)
            with open(os.path.abspath(os.path.join(self._models_folder, '__init__.py')), 'w'):
                pass

        if not os.path.exists(self._controllers_folder):
            os.makedirs(self._controllers_folder)
            with open(os.path.abspath(os.path.join(self._controllers_folder, '__init__.py')), 'w'):
                pass

    #: if not controllers package create models package
    def init_app(self, app):

        self._create_base_struture()

        #: List all controllers in the application controllers package and return a list of tuples
        # with (url,# module_name)
        controllers = [self._format_route(module_name, self._controllers_package) for _, module_name, _ in
                       pkgutil.iter_modules([self._controllers_package])]

        #: Register all controllers
        for module_namespace, module_name in controllers:
            blueprint = __import__(module_namespace, globals(), locals(), [module_name], 0)

            self._flask_app.register_blueprint(getattr(blueprint, module_name),
                                               url_prefix='/{0}'.format(module_name))

from conans.client.generators.virtualenv import VirtualEnvGenerator
from conans.client.run_environment import RunEnvironment
from conans import ConanFile


class VirtualRunEnvMultiGenerator(VirtualEnvGenerator):

    def __init__(self, conanfile):
        super(VirtualRunEnvMultiGenerator, self).__init__(conanfile)
        self.venv_name = "conanrunenv"
        run_env = RunEnvironment(conanfile)
        self.env = run_env.vars

    @property
    def content(self):
        tmp = super(VirtualRunEnvMultiGenerator, self).content
        build_type = str(self.conanfile.settings.build_type).lower()
        ret = {}
        for name, value in tmp.items():
            tmp = name.split(".")
            ret["%s_%s_run.%s" % (tmp[0], build_type, tmp[1])] = value

        return ret


class VirtualRunEnvMultiGeneratorPackage(ConanFile):
    name = "VirtualRunEnvMultiGenerator"
    version = "0.1"
    author = "Joaquin Herrero Herrero"
    url = "https://github.com/joaquin-herrero/conan-custom-virtualrunenv_multi-generator.git"
    license = "MIT"
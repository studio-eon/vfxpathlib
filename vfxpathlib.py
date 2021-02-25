import os
import re

SHOTPATH_DEFAULT_FORMAT = '{path}'

class ShotPath:
    def __init__(self, path):
        self.__path = os.path.abspath(str(path))
        self.__dirname , self.__basename = os.path.split(self.__path)
        self.__root , self.__ext = os.path.splitext(self.__basename)


    def __attrs__(self):
        """Replaces format directives with callables to get their values."""
        return {
            'path': self.__path,
            'h': self.hierarchy,
            'p': self.project,
            'e': self.episode,
            'q': self.sequence,
            's': self.shot,
            't': self.task,
            'v': self.version,
            'w': self.wip,
            'vw': self.version_wip,
            'E': self.episode_code,
            'Q': self.sequence_code,
            'S': self.shot_code,
            'V': self.version_code,
            'P': self.publish_code,
            'ext': self.ext
        }

    @property
    def path(self):
        """Item absolute path, if a filesystem item.
        """
        return self.__path
    @property
    def dirname(self):
        return self.__dirname
    @property
    def basename(self):
        return self.__basename
    @property
    def root(self):
        return self.__root
    @property
    def ext(self):
        return self.__ext
    @property
    def publish_root(self):
        result = re.search(r"(\S+_v\d+)", self.__root)
        return result.group(1)


    @property
    def hierarchy(self):
        segments = self.publish_root.split("_")
        size = len(segments)
        if size == 6:
            return "episode-sequence-shot"
        if size == 5:
            return "sequence-shot"
        if size == 4:
            return "shot"
    @property
    def project(self):
        return self.publish_root.split("_")[0]
    @property
    def episode(self):
        if self.hierarchy == "episode-sequence-shot":
            return self.publish_root.split("_")[1]
        else:
            return None
    @property
    def sequence(self):
        if self.hierarchy == "episode-sequence-shot" or self.hierarchy == "sequence-shot":
            return self.publish_root.split("_")[-4]
        else:
            return None
    @property
    def shot(self):
        return self.publish_root.split("_")[-3]
    @property
    def task(self):
        return self.publish_root.split("_")[-2]
    @property
    def version(self):
        return self.publish_root.split("_")[-1]
    @property
    def wip(self):
        result = re.search(r"_(w\d+)", self.__root)
        if result:
            return result.group(1)
    @property
    def version_wip(self):
        if self.wip:
            return "{self.version}_{self.wip}".format(**locals())
        else:
            return self.version

    @property
    def episode_code(self):
        if self.hierarchy == "episode-sequence-shot":
            return "{self.project}_{self.episode}".format(**locals())
        else:
            return None
    @property
    def sequence_code(self):
        if self.hierarchy == "episode-sequence-shot":
            return "{self.project}_{self.episode}_{self.sequence}".format(**locals())
        elif self.hierarchy == "sequence-shot":
            return "{self.project}_{self.sequence}".format(**locals())
        else:
            return None
    @property
    def shot_code(self):
        if self.hierarchy == "episode-sequence-shot":
            return "{self.project}_{self.episode}_{self.sequence}_{self.shot}".format(**locals())
        elif self.hierarchy == "sequence-shot":
            return "{self.project}_{self.sequence}_{self.shot}".format(**locals())
        elif self.hierarchy == "shot":
            return "{self.project}_{self.shot}".format(**locals())
        else:
            return None
    @property
    def version_code(self):
            return "{self.shot_code}_{self.task}_{self.version_wip}".format(**locals())
    @property
    def publish_code(self):
            return "{self.shot_code}_{self.task}_{self.version}".format(**locals())


    def format(self, fmt=SHOTPATH_DEFAULT_FORMAT):
        """Format the stdout string.
        The following directives can be embedded in the format string.

        Directive : Meaning
        'path': self.__path
        'h': hierarchy
        'p': project
        'e': episode
        'q': sequence
        's': shot
        't': task
        'v': version
        'w': wip
        'E': episode_code
        'Q': sequence_code
        'S': shot_code
        'V': version_code
        'P': publish_code
        'ext': ext

        :param fmt: Format string. Default is '{path}'.
        :return: Formatted string.
        """

        atts = self.__attrs__()
        return fmt.format(**atts)
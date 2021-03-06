# -*- coding: utf-8 -*-


class MoodleRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'mdl':
            return 'moodle'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'mdl':
            return 'moodle'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'mdl' and obj2._meta.app_label == 'mdl':
            return True
        return None

    def allow_migrate(self, db, model):
        if model._meta.app_label == 'mdl':
            return False
        return None

# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-16 13:25
from __future__ import unicode_literals

from django.db import migrations

# pinax-notifications-no-scoping is dead, so we side-graded to this project.

# The initial migration in this commit comes from that project, so that our migration operations happen normally.
# The other two migrations added in this commit are so that we can continue to keep this fork up to date
# with the base, and continue to add merges without conflict.

# The initial migration has been massaged a bit from its original (read: added on_delete kwargs) to make
# it compatible with Django>=2 and should not be changed except for required kwarg compatibility in testing

# IMPORTANT the order of the dependencies is important. Our work needs to be done first, so the next merge
# that happens, this merge needs to be first, then the latest canonical migration comes second. Note how
# `0002_auto_20200116_1323.py` is first, and is added in this commit.


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_notifications', '0002_auto_20200116_1323'),
        ('pinax_notifications', '0002_auto_20171003_2006'),
    ]

    operations = [
    ]

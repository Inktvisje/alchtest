__author__ = 'Arjen'
#
# General settings for alchtest
#


# Database connection:
db_file = 'alchtest:alchtest@localhost:5432/alchtest'
db_con = 'postgresql://%s' % db_file

# Echo database queries:
db_echo = False
#!/usr/bin/env python

from __future__ import print_function
import os

from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) \
            if flags else tools.run(flow, store)
DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

FILES = (('Alpha.db', 'application/x-sqlite3'),
         ('Alpha.txt', None),
         )



# folder_id = '0B7LMIjwvjj2cVmhmLVI3T2xvRlE'
# file_metadata = {
#   'name' : 'Alpha.db',
#   'parents': [ folder_id ]
# }
# media = MediaFileUpload('Alpha.db',
#                         mimetype=None,
#                         resumable=True)
# file = drive_service.files().create(body=file_metadata,
#                                     media_body=media,
#                                     fields='id').execute()
# # print "File ID: %s" % (file.get('id'))

for filename, mimeType in FILES:
    metadata = {'name': filename}
    if mimeType:
        metadata['mimeType'] = mimeType
    res = DRIVE.files().create(body=metadata, media_body=filename).execute()
    if res:
        print('Uploaded "%s" (%s)' % (filename, res['mimeType']))

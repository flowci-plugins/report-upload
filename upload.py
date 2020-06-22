import os
import sys
import shutil
from flowci import domain, client

# inputs of plugin
ReportPath = os.path.join(domain.AgentJobDir, client.GetVar('REPORT_PATH'))
ReportName = client.GetVar('REPORT_NAME')
ReportContentType = client.GetVar('REPORT_CONTENT_TYPE')
EntryFile = client.GetVar('REPORT_ENTRY_FILE')

def checkContentType(t):
    valid = {
        domain.ContentTypeHtml: 1,
        domain.ContentTypeJson: 1,
        domain.ContentTypeXml: 1
    }

    return valid.get(t) is not None

def sendReport():
    if not os.path.exists(ReportPath):
        sys.exit("'{}' not existed".format(ReportPath))

    if not checkContentType(ReportContentType):
        sys.exit("Report content type not suported")

    upload = ReportPath
    isZipFile = "false"

    if os.path.isdir(ReportPath):
        zipFileName = os.path.basename(ReportPath)
        upload = shutil.make_archive(zipFileName, 'zip', ReportPath)
        isZipFile = "true"    
        print("zipped.")

    api = client.Client()

    status = api.sendJobReport(
        path=upload, 
        name=ReportName,
        zipped=isZipFile,
        contentType=ReportContentType,
        entryFile=EntryFile
    )

    print("{} report uploaded with status {}".format(ReportPath, status))

sendReport()

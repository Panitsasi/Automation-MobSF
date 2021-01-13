#!/usr/bin/python3

import os
import sys

md5_sample = str(sys.argv[1])

static_report_name = 'strep_' + md5_sample + '.pdf'
dynamic_report_name = 'dyrep_' + md5_sample + '.pdf'

# STATIC REPORT
os.system( f' cp ~/Automation-MobSF/reports/{md5_sample}/Static.pdf ~/Automation-MobSF/run/website/public/static_reports/{static_report_name}')

# DYNAMIC REPORT
os.system( f' cp ~/Automation-MobSF/reports/{md5_sample}/Dynamic.pdf ~/Automation-MobSF/run/website/public/dynamic_reports/{dynamic_report_name}')

print('Reports transfered to server...')
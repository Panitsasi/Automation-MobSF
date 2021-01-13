import converter as con
import mongodb as db
import config
import linker as lk
import threading
import sys
import time

sample_md5=str(sys.argv[1])
static_report = 'static_reports/strep_'+sample_md5 + '.pdf'
dynamic_report = 'dynamic_reports/dyrep_' + sample_md5 + '.pdf'


if __name__ == "__main__":

    converter = con.Converter(config.PATH, config.STATIC_ANALYSIS_DATA)
    converter.add_json_data('static_report',static_report)
    converter.add_json_data('dynamic_report',dynamic_report)
    localDatabase = db.MONGODB(config.CONNECTION_STRING_MONGODB_DATABASE_LOCAL, "MobSF", "Local")
    cloudDatabase = db.MONGODB(config.CONNECTION_STRING_MONGODB_DATABASE_CLOUD, "MobSF", "Cloud")
    link_local = lk.Linker(localDatabase,converter)
    link_cloud = lk.Linker(cloudDatabase, converter)
    link_local.upload()
    link_cloud.upload()


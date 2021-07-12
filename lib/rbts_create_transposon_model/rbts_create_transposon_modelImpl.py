# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os
from Utils.modeluploadUtilClient import modeluploadUtil 
from Utils.funcs import check_output_name
from installed_clients.WorkspaceClient import Workspace
from installed_clients.KBaseReportClient import KBaseReport
#END_HEADER


class rbts_create_transposon_model:
    '''
    Module Name:
    rbts_create_transposon_model

    Module Description:
    A KBase module: rbts_create_transposon_model
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def run_rbts_create_transposon_model(self, ctx, params):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param params: instance of mapping from String to unspecified object
            'standard_model_name' (str): 
            'model_string' (str): 
            'past_end_string' (str): 
            'description' (str):
            'output_name' (str): No spaces
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_rbts_create_transposon_model
        logging.info("Input params:")
        logging.info(params)
        params['shared_folder'] = self.shared_folder
        token = os.environ.get('KB_AUTH_TOKEN', None)
        ws = Workspace(self.ws_url, token=token)
        params['workspace_id'] =  ws.get_workspace_info({'workspace': params['workspace_name']})[0]
        params['ws_obj'] = ws
        params['username'] = ctx['user_id']

        modelf_util  = modeluploadUtil(params)
        result = modelf_util.upload_model()

        text_message = "Finished uploading file \n" + \
                        "{} saved as {} on {}\n".format(result['Name'],
                        result['Type'], result['Date'])
        logging.info(text_message)

        report = KBaseReport(self.callback_url)
        report_info = report.create({'report': {'objects_created':[],
                                                'text_message': params['parameter_1']},
                                                'workspace_name': params['workspace_name']})
        output = {
            'report_name': report_info['name'],
            'report_ref': report_info['ref'],
        }
        #END run_rbts_create_transposon_model

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_rbts_create_transposon_model return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]

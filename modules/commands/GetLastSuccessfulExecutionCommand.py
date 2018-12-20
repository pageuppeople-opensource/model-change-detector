from modules.commands.BaseCommand import BaseCommand


class GetLastSuccessfulExecutionCommand(BaseCommand):
    def __init__(self, db_connection_string, logger=None):
        super().__init__(db_connection_string, logger)

    def execute(self):
        data_pipeline_execution = self.repository.get_last_successful_data_pipeline_execution()
        last_successful_execution_id = ''
        if data_pipeline_execution is None:
            self.logger.debug(f'Could not find last successful data_pipeline_execution')
        else:
            last_successful_execution_id = str(data_pipeline_execution.id)
            self.logger.debug(f'Found last successful data_pipeline_execution to be {str(data_pipeline_execution)}')
        print(last_successful_execution_id)

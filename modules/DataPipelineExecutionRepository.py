from sqlalchemy import desc
from modules.DataPipelineExecutionEntity import DataPipelineExecutionEntity, Base
from modules.BaseObject import BaseObject
from modules.Shared import Constants


class DataPipelineExecutionRepository(BaseObject):
    def __init__(self, session_maker, logger=None):
        super().__init__(logger)
        self.session_maker = session_maker

    def create_schema(self, engine):
        engine.execute(f'CREATE SCHEMA IF NOT EXISTS {Constants.DATA_PIPELINE_EXECUTION_SCHEMA_NAME}')
        Base.metadata.create_all(engine)

    def start_new(self):
        session = self.session_maker()
        data_pipeline_execution = DataPipelineExecutionEntity()
        session.add(data_pipeline_execution)
        session.commit()
        return data_pipeline_execution

    def get_last_successful_data_pipeline_execution(self):
        session = self.session_maker()
        return session.query(DataPipelineExecutionEntity)\
            .filter_by(status=Constants.DataPipelineExecutionStatus.COMPLETED_SUCCESSFULLY)\
            .order_by(desc(DataPipelineExecutionEntity.last_updated_on))\
            .order_by(desc(DataPipelineExecutionEntity.created_on))\
            .first()

    def finish_existing(self, execution_id):
        session = self.session_maker()
        data_pipeline_execution = session.query(DataPipelineExecutionEntity)\
            .filter_by(id=execution_id)\
            .first()
        data_pipeline_execution.status = Constants.DataPipelineExecutionStatus.COMPLETED_SUCCESSFULLY
        session.commit()
        return data_pipeline_execution



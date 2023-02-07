from .database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean, Integer, ForeignKey, ARRAY, Float, Date, DateTime
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE


class Test(Base):
    __tablename__ = 'tests'
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=True)
    published = Column(Boolean, nullable=False, default=True)
    createdAt = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=func.now())
    updatedAt = Column(TIMESTAMP(timezone=True),
                       default=None, onupdate=func.now())


class Campaign(Base):
    __tablename__ = 'campaign'
    campaing_id = Column(Integer, primary_key=True, nullable=False)
    agency = Column(String,  nullable=False)
    campaign_name = Column(String, nullable=False)
    client = Column(String, nullable=False)
    created_by = Column(String, nullable=True)
    modified_by = Column(String, nullable=True)
    modified_date = Column(String, nullable=True)

class Audience(Base): 
    __tablename__ = 'audience'
    audience_id = Column(Integer, primary_key=True, nullable=False)

class DayPartRecurringDay(Base): 
    __tablename__ = 'day_part_recurring_day'
    day_part_recurring_day_id = Column(Integer, primary_key=True, nullable=False)

class DayPartRangeDay(Base): 
    __tablename__ = 'day_part_range_day'
    day_part_range_day_id = Column(Integer, primary_key=True, nullable=False)

class FrequencyCapping(Base): 
    __tablename__ = 'frequency_capping'
    frequency_capping_id = Column(Integer, primary_key=True, nullable=False)

class MetaData(Base): 
    __tablename__ = 'metadata'
    metadata_id = Column(Integer, primary_key=True, nullable=False)
    type = Column(String)

class MetDataDma(Base): 
    __tablename__ = 'metadata_dma'
    metadata_dma_id = Column(Integer, primary_key=True, nullable=False)
    metadata_id = Column(Integer, ForeignKey('metadata.metadata_id'))
    dma_id = Column(String) 

class Geo(Base): 
    __tablename__ = 'geo'
    geo_id = Column(Integer, primary_key=True, nullable=False)
    included = Column(Boolean, nullable=False, server_default='False')

class GeoMetadataID(Base): 
    __tablename__ = 'geo_metadata'
    geo_metadata_id = Column(Integer, primary_key=True, nullable=False)
    geo_id = Column(Integer, ForeignKey('geo.geo_id'))
    metadata_id = Column(Integer, ForeignKey('metadata.metadata_id'))

class GeoZipCode(Base): 
    __tablename__ = 'geo_zipcode'
    geo_zipcode_id = Column(Integer, primary_key=True, nullable=False)
    geo_id = Column(Integer, ForeignKey('geo.geo_id'))
    zipcode = Column(String, nullable=False)

class HaitusDay(Base): 
    __tablename__ = 'haitus_day'
    haitus_day_id = Column(Integer, primary_key=True, nullable=False)

class InventorySource(Base): 
    __tablename__ = 'inventory_source'
    inventory_source_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

class Network(Base): 
    __tablename__ = 'network'
    network_id = Column(Integer, primary_key=True, nullable=False)
    included = Column(Boolean, nullable=False, server_default='False')
    network_ids = Column(ARRAY(String))

class Platform(Base): 
    __tablename__ = 'platform'
    platform_id = Column(Integer, primary_key=True, nullable=False)
    platform_value = Column(String, nullable=False)

class Segment(Base): 
    __tablename__ = 'segment'
    segment_id = Column(Integer, primary_key=True, nullable=False)

class Template(Base): 
    __tablename__ = 'template'
    template_id = Column(Integer, primary_key=True, nullable=False)
    tenant_id = Column(String, nullable=False)

class TemplateExcluded(Base): 
    __tablename__ = 'template_excluded'
    template_exluded_id = Column(Integer, primary_key=True, nullable=False)
    template_id = Column(Integer, ForeignKey('template.template_id'))
    excluded = Column(String, nullable=False)


class TemplateIncluded(Base): 
    __tablename__ = 'template_included'
    template_inluded_id = Column(Integer, primary_key=True, nullable=False)
    template_id = Column(Integer, ForeignKey('template.template_id'))
    included = Column(String, nullable=False)

class Proposal(Base): 
    __tablename__ = 'proposal'
    proposal_id = Column(Integer, primary_key=True, nullable=False)
    partition_id = Column(String, nullable=True)
    sort_id = Column(String, nullable=True)
    addressable = Column(Boolean, nullable=False, server_default='False')
    cpm = Column(Integer, nullable=True)
    created_by = Column(String, nullable=True)
    created_date = Column(String, nullable=True)
    end_date = Column(String, nullable=True)
    gross_budget = Column(Integer, nullable=True)
    group_id = Column(String, nullable=True)
    line_of_business = Column(String, nullable=True)
    max_avails = Column(Boolean, nullable=True, server_default='False')
    modified_by = Column(String, nullable=True)
    modified_date = Column(String, nullable=True)
    name = Column(String, nullable=True)
    non_guaranteed = Column(Boolean, nullable=True, server_default='False')
    pacing = Column(String, nullable=True)
    priority = Column(Integer, nullable=True)
    salesforce_id = Column(String, nullable=True)
    start_date = Column(String, nullable=True, unique=True)

class ProposalAudience(Base): 
    __tablename__ = 'proposal_audience'
    proposal_audience_id = Column(Integer, primary_key=True, nullable=False)
    proposal_id = Column(Integer, ForeignKey('proposal.proposal_id'))
    audience_id = Column(Integer, ForeignKey('audience.audience_id'))

class ProposalDayPartRecurringDay(Base): 
    __tablename__ = 'proposal_day_part_recurring_day'
    proposal_day_part_recurring_day_id = Column(Integer, primary_key=True, nullable=False)
    proposal_id = Column(Integer, ForeignKey('proposal.proposal_id'))
    day_part_recurring_days_id = Column(Integer, ForeignKey('day_part_recurring_day.day_part_recurring_day_id'))

class ProposalDayPartRangeDay(Base): 
    __tablename__ = 'proposal_day_part_range_day'
    proposal_day_part_range_day_id = Column(Integer, primary_key=True, nullable=False)
    proposal_id = Column(Integer, ForeignKey('proposal.proposal_id'))
    day_part_range_day_id = Column(Integer, ForeignKey('day_part_range_day.day_part_range_day_id'))

class ProposalFrequencyCapping(Base): 
    __tablename__ = 'proposal_frequency_capping'
    proposal_frequency_capping_id = Column(Integer, primary_key=True, nullable=False)
    proposal_id = Column(Integer, ForeignKey('proposal.proposal_id'))
    frequency_capping_id = Column(Integer, ForeignKey('frequency_capping.frequency_capping_id'))

class ProposalGeo(Base): 
    __tablename__ = 'proposal_geo'
    proposal_geo_id = Column(Integer, primary_key=True, nullable=False)
    proposal_id = Column(Integer, ForeignKey('proposal.proposal_id'))
    geo_id = Column(Integer, ForeignKey('geo.geo_id'))

class ProposalHaitusDay(Base): 
    __tablename__ = 'proposal_haitus_day'
    proposal_haitus_day_id = Column(Integer, primary_key=True, nullable=False)
    proposal_id = Column(Integer, ForeignKey('proposal.proposal_id'))
    haitus_day_id = Column(Integer, ForeignKey('haitus_day.haitus_day_id'))

class ProposalInventorySource(Base): 
    __tablename__ = 'proposal_inventory_source'
    proposal_inventory_source_id = Column(Integer, primary_key=True, nullable=False)
    proposal_id = Column(Integer, ForeignKey('proposal.proposal_id'))
    inventory_source_id = Column(Integer, ForeignKey('inventory_source.inventory_source_id'))

class ProposalNetwork(Base): 
    __tablename__ = 'proposal_network'
    proposal_network_id = Column(Integer, primary_key=True, nullable=False)
    proposal_id = Column(Integer, ForeignKey('proposal.proposal_id'))
    network_id = Column(Integer, ForeignKey('network.network_id'))

class ProposalPlatform(Base): 
    __tablename__ = 'proposal_platform'
    proposal_platform_id = Column(Integer, primary_key=True, nullable=False)
    proposal_id = Column(Integer, ForeignKey('proposal.proposal_id'))
    plaform_id = Column(Integer, ForeignKey('platform.platform_id'))

class ProposalSegment(Base): 
    __tablename__ = 'proposal_segment'
    proposal_segment_id = Column(Integer, primary_key=True, nullable=False)
    proposal_id = Column(Integer, ForeignKey('proposal.proposal_id'))
    segment_id = Column(Integer, ForeignKey('segment.segment_id'))


class ProposalTemplate(Base): 
    __tablename__ = 'proposal_template'
    proposal_template_id = Column(Integer, primary_key=True, nullable=False)
    proposal_id = Column(Integer, ForeignKey('proposal.proposal_id'))
    template_id = Column(Integer, ForeignKey('template.template_id'))


class Yield(Base): 
    __tablename__ = 'yield'
    yield_id = Column(Integer, primary_key=True, nullable=False)
    proposal_id = Column(Integer, ForeignKey('proposal.proposal_id'), nullable=False)
    availables_to_purchase = Column(Integer, nullable=False)
    gross_availables = Column(Integer, nullable=False)
    net_availables = Column(Integer, nullable=False)

class ProposalRecommendation(Base): 
    __tablename__ = 'proposal_recommendation'
    proposal_recommendation_id = Column(Integer, primary_key=True, nullable=False)
    proposal_id = Column(Integer, ForeignKey('proposal.proposal_id'), nullable=False)
    transaction_id = Column(Integer, nullable=False)
    job_status = Column(String, nullable=False)
    type = Column(String, nullable=False)
    created_date = Column(String, nullable=False)
    yield_id = Column(Integer, ForeignKey('yield.yield_id'), nullable=False)

